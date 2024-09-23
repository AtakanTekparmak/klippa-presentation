import ell
from src.config import MODEL_NAME
from src.client import OpenAIClient
from src.utils import create_functions_schema, load_system_prompt
from src.engine import ToolCallingEngine

# Get instance of the engine
ENGINE = ToolCallingEngine.get_instance()

# Load system prompt
SYSTEM_PROMPT = load_system_prompt(create_functions_schema(ENGINE.functions))

@ell.simple(model=MODEL_NAME, client=OpenAIClient.get_instance())
def my_lmp(prompt: str):
    return [
        ell.system(SYSTEM_PROMPT),
        ell.user(prompt)
    ]