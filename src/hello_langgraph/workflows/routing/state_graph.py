from langgraph.graph import END, START, StateGraph
from langgraph.graph.state import CompiledStateGraph

from hello_langgraph.workflows.chat_model import llmChatModel
from hello_langgraph.workflows.routing.router import llm_call_router
from hello_langgraph.workflows.routing.state import RoutingStateTypedDict


# Nodes
def write_a_story(state: RoutingStateTypedDict):
    """Write a story"""

    result = llmChatModel.invoke(state["input"])
    return {"output": result.content}


def write_a_joke(state: RoutingStateTypedDict):
    """Write a joke"""

    result = llmChatModel.invoke(state["input"])
    return {"output": result.content}


def write_a_poem(state: RoutingStateTypedDict):
    """Write a poem"""

    result = llmChatModel.invoke(state["input"])
    return {"output": result.content}


# Conditional edge function to route to the appropriate node
def route_decision(state: RoutingStateTypedDict):
    # Return the node name you want to visit next
    if state["decision"] == "story":
        return "write_a_story"
    elif state["decision"] == "joke":
        return "write_a_joke"
    elif state["decision"] == "poem":
        return "write_a_poem"


# Build workflow
oStateGraph = StateGraph(RoutingStateTypedDict)

# Add nodes
oStateGraph.add_node("write_a_story", write_a_story)
oStateGraph.add_node("write_a_joke", write_a_joke)
oStateGraph.add_node("write_a_poem", write_a_poem)
oStateGraph.add_node("llm_call_router", llm_call_router)

# Add edges to connect nodes
oStateGraph.add_edge(START, "llm_call_router")
oStateGraph.add_conditional_edges(
    "llm_call_router",
    route_decision,
    {  # Name returned by route_decision : Name of next node to visit
        "write_a_story": "write_a_story",
        "write_a_joke": "write_a_joke",
        "write_a_poem": "write_a_poem",
    },
)
oStateGraph.add_edge("write_a_story", END)
oStateGraph.add_edge("write_a_joke", END)
oStateGraph.add_edge("write_a_poem", END)

# Compile workflow
compiled_state_graph: CompiledStateGraph = oStateGraph.compile()
