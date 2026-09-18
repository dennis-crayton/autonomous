I wrote this to further my knowledge when working with LLMs.  This program takes in user input via IDE terminal, then sends it to qwen3:8b model being ran inside a docker container on your system.  The output is then sent back and outputted for the user.  We used an empty array to store our messages so we could utilize the json currently stored in memory as a temporary memory for the LLM.  I could easily connect this to a DB but it would just further increase IO delay and does not align with the current scope of what I was trying to accomplish here.  

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
