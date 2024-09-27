# Presentation Demo

### Beyond RAG and Single Tool Calls: What Chained Tool Calling (and Agents) Can Do For You 

#### presented by Atakan Tekparmak

#### uses [tiny_fnc_engine](https://github.com/AtakanTekparmak/tiny_fnc_engine) for tool calling backend

## Requirements

- Python 3.10+
- pip
- make
- Any local LLM inference provider that is OpenAI compatible ([ollama](https://ollama.com/), [LMStudio](https://lmstudio.ai/) etc.)

## Setup and Usage

### The Presentation

1. Serve `Presentation/index.html` in any way you like 

### Chat Interface Demo

1. Serve any local model you want in an OpenAI compatible API format (I use NousResearch/Hermes-3-Llama-3.1-8B)
2. Go to `src/config.py` and set the `MODEL_NAME`, `BASE_URL`, and `API_KEY` variables
3. Run `make install` to install the dependencies
4. Run `make run` to start the CLI or `make run_interface` to start the chat interface
