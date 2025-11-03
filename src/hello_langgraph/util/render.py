import io

from PIL import Image
from PIL.ImageFile import ImageFile
from langchain_core.runnables.graph import Graph


def open_mermaid_image(graph: Graph) -> None:
    png: bytes = graph.draw_mermaid_png()
    oBytesIO = io.BytesIO(png)
    oImageFile: ImageFile = Image.open(oBytesIO)
    oImageFile.show()  # Opens in default image viewer
