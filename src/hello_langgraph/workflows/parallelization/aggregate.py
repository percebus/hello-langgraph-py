from typing import Any

from langgraph.graph import StateGraph, START, END
from langgraph.graph.state import CompiledStateGraph
from langchain_core.runnables.graph import Graph

from hello_langgraph.util.render import open_mermaid_image
from hello_langgraph.workflows.model import llmChatModel
from hello_langgraph.workflows.parallelization.state import StateTypedDict


# Nodes
def write_a_joke(state: StateTypedDict):
    """First LLM call to generate initial joke"""

    msg = llmChatModel.invoke(f"Write a joke about {state['topic']}")
    return {"joke": msg.content}


def write_a_story(state: StateTypedDict):
    """Second LLM call to generate story"""

    msg = llmChatModel.invoke(f"Write a story about {state['topic']}")
    return {"story": msg.content}


def write_a_poem(state: StateTypedDict):
    """Third LLM call to generate poem"""

    msg = llmChatModel.invoke(f"Write a poem about {state['topic']}")
    return {"poem": msg.content}


def aggregator(state: StateTypedDict):
    """Combine the joke and story into a single output"""

    combined = f"Here's a story, joke, and poem about {state['topic']}!\n\n"
    combined += f"STORY:\n{state['story']}\n\n"
    combined += f"JOKE:\n{state['joke']}\n\n"
    combined += f"POEM:\n{state['poem']}"
    return {"combined_output": combined}


# Build workflow
oStateGraph = StateGraph(StateTypedDict)

# Add nodes
oStateGraph.add_node("write_a_joke", write_a_joke)
oStateGraph.add_node("write_a_story", write_a_story)
oStateGraph.add_node("write_a_poem", write_a_poem)
oStateGraph.add_node("aggregator", aggregator)

# Add edges to connect nodes
oStateGraph.add_edge(START, "write_a_joke")
oStateGraph.add_edge(START, "write_a_story")
oStateGraph.add_edge(START, "write_a_poem")
oStateGraph.add_edge("write_a_joke", "aggregator")
oStateGraph.add_edge("write_a_story", "aggregator")
oStateGraph.add_edge("write_a_poem", "aggregator")
oStateGraph.add_edge("aggregator", END)
oCompiledStateGraph: CompiledStateGraph = oStateGraph.compile()


# Show workflow
oGraph: Graph = oCompiledStateGraph.get_graph()
open_mermaid_image(oGraph)

# Invoke
state: dict[str, Any] | Any = oCompiledStateGraph.invoke({"topic": "cats"})
print(state["combined_output"])
