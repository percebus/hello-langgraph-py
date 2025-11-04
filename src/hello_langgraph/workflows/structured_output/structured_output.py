# Schema for structured output
from langchain_core.runnables.base import Runnable

from hello_langgraph.workflows.chat_model import llmChatModel
from hello_langgraph.workflows.structured_output.models.query import SearchQuery

# Augment the LLM with schema for structured output
get_search_results: Runnable = llmChatModel.with_structured_output(SearchQuery)
