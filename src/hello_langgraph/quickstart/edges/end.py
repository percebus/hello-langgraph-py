# SRC: https://docs.langchain.com/oss/python/langgraph/quickstart#5-define-end-logic

from typing import Literal

from langgraph.graph import END

from hello_langgraph.quickstart.state import MessagesStateTypedDict


def should_continue(state: MessagesStateTypedDict) -> Literal["tool_node", END]:
    """Decide if we should continue the loop or stop based upon whether the LLM made a tool call"""

    messages = state["messages"]
    last_message = messages[-1]

    # If the LLM makes a tool call, then perform an action
    if last_message.tool_calls:
        return "tool_node"

    # Otherwise, we stop (reply to the user)
    return END
