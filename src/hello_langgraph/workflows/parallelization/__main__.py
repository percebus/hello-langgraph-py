from typing import TYPE_CHECKING, Any

from hello_langgraph.util.render import open_mermaid_image
from hello_langgraph.workflows.parallelization.state_graph import compiled_state_graph

if TYPE_CHECKING:
    from langchain_core.runnables.graph import Graph


def run():
    # Show workflow
    oGraph: Graph = compiled_state_graph.get_graph()
    open_mermaid_image(oGraph)

    # Invoke
    state: dict[str, Any] | Any = compiled_state_graph.invoke({"topic": "cats"})
    print(state["combined_output"])


if __name__ == "__main__":
    run()
