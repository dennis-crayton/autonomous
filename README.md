I wanted some baseline knowledge of working with LLMs and allowing them to use customized functions in my code based on the user's query.  Here is a simple illustration of that, the current query is hardcoded for addition while using an add() function as a tool.  But this represents the potential and use case something like this has.

## Steps to run:
Initialize a Virtual Environment
Activate the Environment

do:
  pip install ollama
  ollama pull qwen3:8b

Run these commands in powershell terminal inside IDE:
  docker run -d --gpus=all -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
  docker exec -it ollama ollama pull qwen3:8b

To run use:
  python main.py
