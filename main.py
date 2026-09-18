from tools.calculator import add,subtract,multiply,divide
from tools.registry import TOOLS
from ollama import Client


client = Client(host="http://localhost:11434")

# Remove hardcoded content here
messages = [
    {
        "role": "user",
        "content": "Use the add tool to calculate 25 + 37. You must use the tool."
    }
]

response = client.chat(
    model="qwen3:8b",
    messages=messages,
    tools=[add]
)

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


final_response = client.chat(
    model="qwen3:8b",
    messages=messages,
    tools=[add]
)

print("\nFinal Answer:")
print(final_response.message.content)