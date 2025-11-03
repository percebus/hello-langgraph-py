from IPython.display import Image, display

from langchain_core.runnables.graph import Graph


def display_mermaid_image(graph: Graph) -> None:
    """Display Mermaid diagram in Jupyter."""
    png: bytes = graph.draw_mermaid_png()
    pngImage = Image(png)
    display(pngImage)
