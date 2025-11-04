from typing import TYPE_CHECKING

from hello_langgraph.workflows.structured_output.structured_output import get_search_results

if TYPE_CHECKING:
    from hello_langgraph.workflows.structured_output.models.query import SearchQuery


def run():
    # Invoke the augmented LLM
    output: SearchQuery = get_search_results.invoke("How does Calcium CT score relate to high cholesterol?")
    print(output)


if __name__ == "__main__":
    run()
