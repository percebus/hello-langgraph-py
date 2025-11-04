from typing import TYPE_CHECKING

from hello_langgraph.util.render import open_mermaid_image
from hello_langgraph.workflows.routing.state_graph import compiled_state_graph

if TYPE_CHECKING:
    from langchain_core.runnables.graph import Graph


def run():
    # Show the workflow
    oGraph: Graph = compiled_state_graph.get_graph()
    open_mermaid_image(oGraph)

    # Invoke
    state = compiled_state_graph.invoke({"input": "Write me a joke about cats"})
    print(state["output"])


if __name__ == "__main__":
    run()
