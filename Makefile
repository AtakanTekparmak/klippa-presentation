# Set default target
.DEFAULT_GOAL := help

# Variables

## Python
PYTHON := python3
PIP := pip
VENV_NAME := venv

# .env file
ENV_FILE := .env

# Help target
help:
	@echo "Usage: make [target]"
	@echo ""
	@echo "Targets:"
	@echo "  1. install           Install dependencies and set up the environment (should be run first)"
	@echo "  2. run               Run the main.py script"
	@echo "  3. run_interface     Run the fasthtml_app.py script"
	@echo "  4. test              Run all the tests in the tests folder"	
	@echo "  5. clean             Remove the virtual environment and its contents"

# Install dependencies and set up the environment
install: 
	$(PYTHON) -m venv $(VENV_NAME)
	. $(VENV_NAME)/bin/activate && \
	$(PIP) install -r requirements.txt 

# Run the main.py script
run: 
	. $(VENV_NAME)/bin/activate && \
	$(PYTHON) main.py

# Run the fasthtml_app.py script
run_interface:
	. $(VENV_NAME)/bin/activate && \
	$(PYTHON) fasthtml_app.py

# Run all the tests in the tests folder
test:
	. $(VENV_NAME)/bin/activate && \
	pytest tests/

# Clean the virtual environment
clean:
	rm -rf $(VENV_NAME)