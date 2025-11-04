import io
from typing import TYPE_CHECKING

from langchain_core.runnables.graph import Graph
from PIL import Image

if TYPE_CHECKING:
    from PIL.ImageFile import ImageFile


def open_mermaid_image(graph: Graph) -> None:
    png: bytes = graph.draw_mermaid_png()
    oBytesIO = io.BytesIO(png)
    oImageFile: ImageFile = Image.open(oBytesIO)
    oImageFile.show()  # Opens in default image viewer
