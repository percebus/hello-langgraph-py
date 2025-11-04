from hello_langgraph.workflows.chat_model import llmChatModel
from hello_langgraph.workflows.routing.models.route import Route


# Augment the LLM with schema for structured output
get_route = llmChatModel.with_structured_output(Route)
