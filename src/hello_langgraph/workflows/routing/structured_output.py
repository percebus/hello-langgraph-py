from pydantic import BaseModel, Field
from typing_extensions import Literal
from hello_langgraph.workflows.model import llmChatModel


# Schema for structured output to use as routing logic
class Route(BaseModel):
    step: Literal["poem", "story", "joke"] = Field(
        None, description="The next step in the routing process"
    )


# Augment the LLM with schema for structured output
get_route = llmChatModel.with_structured_output(Route)
