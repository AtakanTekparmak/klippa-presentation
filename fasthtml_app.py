from fasthtml.common import *
from src.assistant import Assistant
from src.utils import format_function_calls

# Declare constants
PORT = 5013

# Set up the app, including daisyui and tailwind for the chat component
hdrs = (picolink, Script(src="https://cdn.tailwindcss.com"),
    Link(rel="stylesheet", href="https://cdn.jsdelivr.net/npm/daisyui@4.11.1/dist/full.min.css"))
app = FastHTML(hdrs=hdrs, cls="p-4 max-w-lg mx-auto")

# Set up the assistant
assistant = Assistant.get_instance()

# Chat message component (renders a chat bubble)
def ChatMessage(msg, user):
    bubble_class = "chat-bubble-primary" if user else 'chat-bubble-secondary'
    chat_class = "chat-end" if user else 'chat-start'
    return Div(cls=f"chat {chat_class}")(
               Div('user' if user else 'assistant', cls="chat-header"),
               Div(msg, cls=f"chat-bubble {bubble_class}"),
               Hidden(msg, name="messages")
           )

# The input field for the user message. Also used to clear the
# input field after sending a message via an OOB swap
def ChatInput():
    return Input(name='msg', id='msg-input', placeholder="Type a message",
                 cls="input input-bordered w-full", hx_swap_oob='true')

# The main screen
@app.get
def index():
    # Small note below title that says "Warning: The assistant is a bit slow
    warning = Div(cls="alert alert-warning shadow-lg")(
        "Warning: The assistant is a bit slow"
    )
    # Create a form that sends the message to the send function
    page = Form(hx_post=send, hx_target="#chatlist", hx_swap="beforeend")(
           Div(id="chatlist", cls="chat-box h-[73vh] overflow-y-auto"),
               Div(cls="flex space-x-2 mt-2")(
                   Group(ChatInput(), Button("Send", cls="btn btn-primary"))
               )
           )
    return Titled('Chatbot Demo', warning, page)

# Handle the form submission
@app.post
def send(msg: str, messages: list[str] = None):
    if not messages:
        messages = []
    messages.append(msg.rstrip())
    
    # Use the Assistant class to process the message
    response, function_calls = assistant.process_message(msg.rstrip())

    # If there are function calls, format the final response
    if function_calls:
        return (
            ChatMessage(msg, True),    # The user's message
            ChatMessage(format_function_calls(function_calls), False), # The chatbot's response
            ChatMessage(response, False), # The chatbot's response
            ChatInput()
        ) # And clear the input field via an OOB swap
    else:
        return (
            ChatMessage(msg, True),    # The user's message
            ChatMessage(response, False), # The chatbot's response
            ChatInput() # And clear the input field via an OOB swap
        )

serve(port=PORT)
