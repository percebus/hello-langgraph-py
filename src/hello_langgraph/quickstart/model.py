# SRC: https://docs.langchain.com/oss/python/langgraph/quickstart#1-define-tools-and-model

from langchain.tools import tool
from langchain.chat_models import init_chat_model
from langchain_core.language_models.chat_models import BaseChatModel


oChatModel: BaseChatModel = init_chat_model(
    "claude-sonnet-4-5-20250929",
    temperature=0
)


# Define tools
@tool
def multiply(a: int, b: int) -> int:
    """Multiply `a` and `b`.

    Args:
        a: First int
        b: Second int
    """
    return a * b


@tool
def add(a: int, b: int) -> int:
    """Adds `a` and `b`.

    Args:
        a: First int
        b: Second int
    """
    return a + b


@tool
def divide(a: int, b: int) -> float:
    """Divide `a` and `b`.

    Args:
        a: First int
        b: Second int
    """
    return a / b


# Augment the LLM with tools
tools = [add, multiply, divide]
tools_by_name = {tool.name: tool for tool in tools}
model_with_tools = oChatModel.bind_tools(tools)
