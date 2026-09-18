from tools.calculator import add,subtract,multiply,divide
from tools.registry import TOOLS
from ollama import Client


client = Client(host="http://localhost:11434")

messages = []


while True:
# Remove hardcoded content here
    user_query = input("Enter your request: ")
    
    messages.append(
        {
            "role": "user",
            "content": user_query
        }
    )
    while True:

        response = client.chat(
            model="qwen3:8b",
            messages=messages,
            tools=[add,subtract,multiply,divide]
        )
        messages.append(response.message)

        if not response.message.tool_calls:
            print("\nFinal Answer:")
            print(response.message.content)
            break

        for tool_call in response.message.tool_calls:
            tool_name = tool_call.function.name
            arguments = tool_call.function.arguments

            tool = TOOLS[tool_name]

            result = tool(**arguments)

            print("Tool requested:", tool_name)
            print("Arguments:", arguments)
            print("Result:",result)

            messages.append(response.message)
            messages.append({
                "role":"tool",
                "tool_name":tool_name,
                "content":str(result)
            })