from tiny_fnc_engine import FunctionCallingEngine
from src.config import TOOLS_PATH

class ToolCallingEngine:
    """
    Singleton class for ToolCallingEngine.
    """
    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = FunctionCallingEngine()
            cls._instance.add_functions_from_file(TOOLS_PATH)
        return cls._instance

