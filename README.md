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
