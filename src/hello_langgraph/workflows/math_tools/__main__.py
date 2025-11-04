# Schema for structured output

from hello_langgraph.workflows.math_tools.chat_model import mathChatModel


def run():
    # Invoke the LLM with input that triggers the tool call
    msg = mathChatModel.invoke("What is 2 times 3?")
    print(msg)

    # Get the tool call
    msg.tool_calls
    print(msg.tool_calls)


if __name__ == "__main__":
    run()
