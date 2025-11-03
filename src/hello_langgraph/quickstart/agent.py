# SRC: https://docs.langchain.com/oss/python/langgraph/quickstart#6-build-and-compile-the-agent

from langgraph.graph import StateGraph, START, END
from langgraph.graph.state import CompiledStateGraph
from langchain_core.runnables.graph import Graph

from hello_langgraph.quickstart.state import MessagesStateTypedDict
from hello_langgraph.quickstart.model import llm_call
from hello_langgraph.quickstart.tool_node import tool_node
from hello_langgraph.quickstart.edges.end import should_continue
from hello_langgraph.util.render import open_mermaid_image

# Build workflow
oStateGraph = StateGraph(MessagesStateTypedDict)

# Add nodes
oStateGraph.add_node("llm_call", llm_call)
oStateGraph.add_node("tool_node", tool_node)

# Add edges to connect nodes
oStateGraph.add_edge(START, "llm_call")
oStateGraph.add_conditional_edges(
    "llm_call",
    should_continue,
    ["tool_node", END]
)
oStateGraph.add_edge("tool_node", "llm_call")

# Compile the agent
oCompiledStateGraph: CompiledStateGraph = oStateGraph.compile()

# Show the agent
oGraph: Graph = oCompiledStateGraph.get_graph(xray=True)
open_mermaid_image(oGraph)

# Invoke
from langchain.messages import HumanMessage
messages = [HumanMessage(content="Add 3 and 4.")]
messages = oCompiledStateGraph.invoke({"messages": messages})
for m in messages["messages"]:
    m.pretty_print()
