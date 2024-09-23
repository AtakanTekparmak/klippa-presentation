import ell
import openai

from tiny_fnc_engine import FunctionCallingEngine

from utils import create_functions_schema, load_system_prompt, parse_function_calls
from tools import get_weather

# Declare constants
MODEL_NAME = "lmstudio-community/Phi-3.5-mini-instruct-GGUF/Phi-3.5-mini-instruct-Q8_0.gguf"
BASE_URL = "http://localhost:1234/v1"
API_KEY = "test"    
TOOLS_PATH = "tools/tools.py"

# OpenAI client
client = openai.Client(
    api_key=API_KEY,
    base_url=BASE_URL,
)

# TinyFNC engine
engine = FunctionCallingEngine()
engine.add_functions_from_file(TOOLS_PATH)

# Load system prompt
system_prompt = load_system_prompt(create_functions_schema(engine.functions))

@ell.simple(model=MODEL_NAME, client=client)
def my_lmp(prompt: str):
    return [
        ell.system(system_prompt),
        ell.user(prompt)
    ]

def main():
    user_query = input("User: ")
    model_response = my_lmp(user_query)
    #print(f"Model response: {model_response}")
    function_calls = parse_function_calls(model_response)
    #print(f"Function calls: {function_calls}")
    results = engine.parse_and_call_functions(function_calls)
    print(f"Assistant: {results[-1]}")
    
if __name__ == "__main__":
    main()
