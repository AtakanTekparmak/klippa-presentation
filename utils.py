from typing import Any, Callable, Dict
import inspect
import json

# Declare constants
SYSTEM_PROMPT_PATH = "static/system_prompt.txt"

def create_functions_schema(functions: Dict[str, Callable]) -> str:
    """
    Creates the functions schema for the prompt.
    """
    functions_schema = []
    for name, function in functions.items():
        try:
            annotations = function.__annotations__
            parameters = {
                param: annotations.get(param, Any).__name__
                for param in inspect.signature(function).parameters
                if param != 'return'
            }
            returns = [{"name": f"{name}_output", "type": annotations.get('return', Any).__name__}]
            
            metadata = {
                "name": name,
                "description": function.__doc__.replace('\\n', '\n') if function.__doc__ else "",
                "parameters": {"properties": parameters, "required": list(parameters.keys())},
                "returns": returns
            }
            functions_schema.append(metadata)
        except Exception as e:
            print(f"Error creating metadata for function {name}: {str(e)}")

    return json.dumps(functions_schema, indent=2, ensure_ascii=False)

def load_system_prompt(
        functions_schema: str,
        file_path: str = SYSTEM_PROMPT_PATH
    ) -> str:
    """
    Loads the system prompt from the specified file.
    """
    def replace_functions_schema(content: str) -> str:
        return content.replace("{{functions_schema}}", functions_schema)
    
    try:
        with open(file_path, "r") as file:
            return replace_functions_schema(file.read())
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return ""
    
def parse_function_calls(content: str) -> str:
    """
    Parses the function calls from the content.
    """
    between_tags = content.split("<|function_calls|>")[1].split("<|end_function_calls|>")[0]
    try:
        return json.loads(between_tags)
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON from function calls")
        return []