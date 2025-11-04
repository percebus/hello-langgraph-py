from textwrap import dedent
from typing import TYPE_CHECKING

from langchain.messages import AIMessage, HumanMessage, SystemMessage
from langgraph.graph import END, START, StateGraph
from langgraph.graph.state import CompiledStateGraph
from langgraph.types import Send

from hello_langgraph.workflows.chat_model import llmChatModel
from hello_langgraph.workflows.orchestration.states import StateTypedDict, WorkerStateTypedDict
from hello_langgraph.workflows.orchestration.structured_output import planner

if TYPE_CHECKING:
    from hello_langgraph.workflows.orchestration.models.sections import Section, SectionCollection


def generate_plan(state: StateTypedDict):
    """Orchestrator that generates a plan for the report"""

    # Generate queries
    report_sections: SectionCollection = planner.invoke(
        [
            SystemMessage(content="Generate a plan for the report."),
            HumanMessage(content=f"Here is the report topic: {state['topic']}"),
        ]
    )

    print("Sections: ")
    print([section.name for section in report_sections.items])

    return {"sections": report_sections.items}


def write_a_report(state: WorkerStateTypedDict):
    """Worker writes a section of the report"""

    # Generate section
    oSection: Section = state["section"]
    oAIMessage: AIMessage = llmChatModel.invoke(
        [
            SystemMessage(
                content=dedent("""
                    Write a report section following the provided name and description.
                    Include no preamble for each section.
                    Use markdown formatting.
                """)
            ),
            HumanMessage(content=f"Here is the section name: {oSection.name} and description: {oSection.description}"),
        ]
    )

    # Write the updated section to completed sections
    return {"completed_sections": [oAIMessage.content]}


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
    # fmt: off
    return [
        Send("write_a_report", {"section": s})
        for s in state["sections"]]
    # fmt: on


# Build workflow
oStateGraph = StateGraph(StateTypedDict)

# Add the nodes
oStateGraph.add_node("generate_plan", generate_plan)
oStateGraph.add_node("write_a_report", write_a_report)
oStateGraph.add_node("concatenate", concatenate)

# Add edges to connect nodes
oStateGraph.add_edge(START, "generate_plan")
oStateGraph.add_conditional_edges("generate_plan", assign_workers, ["write_a_report"])
oStateGraph.add_edge("write_a_report", "concatenate")
oStateGraph.add_edge("concatenate", END)

# Compile the workflow
compiled_state_graph: CompiledStateGraph = oStateGraph.compile()
