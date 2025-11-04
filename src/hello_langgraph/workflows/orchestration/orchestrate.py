from langgraph.types import Send
from langgraph.graph import StateGraph, START, END
from langchain.messages import SystemMessage, HumanMessage
from langgraph.graph.state import CompiledStateGraph
from langchain_core.runnables.graph import Graph

from hello_langgraph.util.render import open_mermaid_image
from hello_langgraph.workflows.model import llmChatModel
from hello_langgraph.workflows.chaining.state import StateTypedDict
from hello_langgraph.workflows.orchestration.planner import planner
from hello_langgraph.workflows.orchestration.states import WorkerStateTypedDict


def generate_plan(state: StateTypedDict):
    """Orchestrator that generates a plan for the report"""

    # Generate queries
    report_sections = planner.invoke(
        [
            SystemMessage(content="Generate a plan for the report."),
            HumanMessage(content=f"Here is the report topic: {state['topic']}"),
        ]
    )

    return {"sections": report_sections.sections}


def write_a_report(state: WorkerStateTypedDict):
    """Worker writes a section of the report"""

    # Generate section
    section = llmChatModel.invoke(
        [
            SystemMessage(
                content="Write a report section following the provided name and description. Include no preamble for each section. Use markdown formatting."
            ),
            HumanMessage(
                content=f"Here is the section name: {state['section'].name} and description: {state['section'].description}"
            ),
        ]
    )

    # Write the updated section to completed sections
    return {"completed_sections": [section.content]}


def concatenate(state: StateTypedDict):
    """Synthesize full report from sections"""

    # List of completed sections
    completed_sections = state["completed_sections"]

    # Format completed section to str to use as context for final sections
    completed_report_sections = "\n\n---\n\n".join(completed_sections)

    return {"final_report": completed_report_sections}


# Conditional edge function to create write_a_report workers that each write a section of the report
def assign_workers(state: StateTypedDict):
    """Assign a worker to each section in the plan"""

    # Kick off section writing in parallel via Send() API
    return [Send("write_a_report", {"section": s}) for s in state["sections"]]


# Build workflow
oStateGraph = StateGraph(StateTypedDict)

# Add the nodes
oStateGraph.add_node("generate_plan", generate_plan)
oStateGraph.add_node("write_a_report", write_a_report)
oStateGraph.add_node("concatenate", concatenate)

# Add edges to connect nodes
oStateGraph.add_edge(START, "generate_plan")
oStateGraph.add_conditional_edges(
    "generate_plan", assign_workers, ["write_a_report"]
)
oStateGraph.add_edge("write_a_report", "concatenate")
oStateGraph.add_edge("concatenate", END)

# Compile the workflow
oCompiledStateGraph: CompiledStateGraph = oStateGraph.compile()

# Show the workflow
oGraph: Graph = oCompiledStateGraph.get_graph()
open_mermaid_image(oGraph)

# Invoke
state = oCompiledStateGraph.invoke({"topic": "Create a report on LLM scaling laws"})

from IPython.display import Markdown
Markdown(state["final_report"])
