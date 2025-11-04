from langgraph.graph import END, START, StateGraph
from langgraph.graph.state import CompiledStateGraph

from hello_langgraph.workflows.chaining.state import StateTypedDict
from hello_langgraph.workflows.chat_model import llmChatModel


# Nodes
def generate_joke(state: StateTypedDict):
    """First LLM call to generate initial joke"""

    msg = llmChatModel.invoke(f"Write a short joke about {state['topic']}")
    return {"joke": msg.content}


def check_punchline(state: StateTypedDict):
    """Gate function to check if the joke has a punchline"""

    # Simple check - does the joke contain "?" or "!"
    if "?" in state["joke"] or "!" in state["joke"]:
        return "Pass"
    return "Fail"


def improve_joke(state: StateTypedDict):
    """Second LLM call to improve the joke"""

    msg = llmChatModel.invoke(f"Make this joke funnier by adding wordplay: {state['joke']}")
    return {"improved_joke": msg.content}


def polish_joke(state: StateTypedDict):
    """Third LLM call for final polish"""
    msg = llmChatModel.invoke(f"Add a surprising twist to this joke: {state['improved_joke']}")
    return {"final_joke": msg.content}


# Build workflow
oStateGraph = StateGraph(StateTypedDict)

# Add nodes
oStateGraph.add_node("generate_joke", generate_joke)
oStateGraph.add_node("improve_joke", improve_joke)
oStateGraph.add_node("polish_joke", polish_joke)

# Add edges to connect nodes
oStateGraph.add_edge(START, "generate_joke")
oStateGraph.add_conditional_edges("generate_joke", check_punchline, {"Fail": "improve_joke", "Pass": END})

oStateGraph.add_edge("improve_joke", "polish_joke")
oStateGraph.add_edge("polish_joke", END)

# Compile
compiled_state_graph: CompiledStateGraph = oStateGraph.compile()
