# Schema for structured output
from langchain_core.runnables.base import Runnable

from hello_langgraph.workflows.chat_model import llmChatModel
from hello_langgraph.workflows.math_tools.tools.math import multiply

# Augment the LLM with tools
mathChatModel: Runnable = llmChatModel.bind_tools([multiply])
