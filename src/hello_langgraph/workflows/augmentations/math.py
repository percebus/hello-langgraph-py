# Schema for structured output
from langchain_core.runnables.base import Runnable

from hello_langgraph.workflows.model import llmChatModel

# Define a tool
def multiply(a: int, b: int) -> int:
    return a * b

# Augment the LLM with tools
toolsRunnable: Runnable = llmChatModel.bind_tools([multiply])

# Invoke the LLM with input that triggers the tool call
msg = toolsRunnable.invoke("What is 2 times 3?")
print(msg)

# Get the tool call
msg.tool_calls
print(msg.tool_calls)
