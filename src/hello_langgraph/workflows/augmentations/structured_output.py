# Schema for structured output
from pydantic import BaseModel, Field
from langchain_core.runnables.base import Runnable

from hello_langgraph.workflows.chat_model import llmChatModel

class SearchQuery(BaseModel):
    search_query: str = Field(None, description="Query that is optimized web search.")
    justification: str = Field(
        None, description="Why this query is relevant to the user's request."
    )


# Augment the LLM with schema for structured output
oRunnable: Runnable = llmChatModel.with_structured_output(SearchQuery)

# Invoke the augmented LLM
output = oRunnable.invoke("How does Calcium CT score relate to high cholesterol?")

print(output)
