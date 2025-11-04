from typing import TYPE_CHECKING

from hello_langgraph.util.render import open_mermaid_image
from hello_langgraph.workflows.chaining.state_graph import compiled_state_graph

if TYPE_CHECKING:
    from langchain_core.runnables.graph import Graph


def run():
    # Show workflow
    oGraph: Graph = compiled_state_graph.get_graph()
    open_mermaid_image(oGraph)

    # Invoke
    state = compiled_state_graph.invoke({"topic": "cats"})
    print("Initial joke:")
    print(state["joke"])
    print("\n--- --- ---\n")
    if "improved_joke" in state:
        print("Improved joke:")
        print(state["improved_joke"])
        print("\n--- --- ---\n")

        print("Final joke:")
        print(state["final_joke"])
    else:
        print("Joke failed quality gate - no punchline detected!")


if __name__ == "__main__":
    run()
