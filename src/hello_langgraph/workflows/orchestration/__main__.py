from langchain_core.runnables.graph import Graph

from hello_langgraph.util.render import open_mermaid_image
from hello_langgraph.workflows.orchestration.state_graph import compiled_state_graph


def run():
    # Show the workflow
    oGraph: Graph = compiled_state_graph.get_graph()
    open_mermaid_image(oGraph)

    # Invoke
    state = compiled_state_graph.invoke({"topic": "Create a report on LLM scaling laws"})

    final_report = state["final_report"]

    # from IPython.display import Markdown
    # Markdown(final_report)
    print(final_report)


if __name__ == "__main__":
    run()
