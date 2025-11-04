from pydantic import BaseModel, Field
from typing_extensions import Literal


# Schema for structured output to use as routing logic
class Route(BaseModel):
    step: Literal["poem", "story", "joke"] = Field(None, description="The next step in the routing process")
