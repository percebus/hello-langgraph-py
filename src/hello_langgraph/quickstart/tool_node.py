# SRC: https://docs.langchain.com/oss/python/langgraph/quickstart#4-define-tool-node

from langchain.messages import ToolMessage

from hello_langgraph.quickstart.tools import tools_by_name

def tool_node(state: dict):
    """Performs the tool call"""

    result = []
    for tool_call in state["messages"][-1].tool_calls:
        tool = tools_by_name[tool_call["name"]]
        observation = tool.invoke(tool_call["args"])
        oToolMessage = ToolMessage(content=observation, tool_call_id=tool_call["id"])
        result.append(oToolMessage)

    return {"messages": result}
