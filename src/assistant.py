from src.model import my_lmp
from src.engine import ToolCallingEngine    
from src.utils import parse_function_calls

ENGINE = ToolCallingEngine.get_instance()

def process_user_query(user_query: str) -> str:
    """
    Process user query and return assistant response

    Args:
        user_query (str): User query

    Returns:
        str: Assistant response
    """
    model_response = my_lmp(user_query)
    # Parse function calls or assistant response from model response
    function_calls, success = parse_function_calls(model_response)
    
    if success: 
        results = ENGINE.parse_and_call_functions(function_calls)
        return f"Assistant: {results[-1] if results else 'No results'}"
    else:
        return f"Assistant: {function_calls}"