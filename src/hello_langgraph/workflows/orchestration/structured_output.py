from langchain_core.runnables.base import Runnable

from hello_langgraph.workflows.chat_model import llmChatModel
from hello_langgraph.workflows.orchestration.models.sections import SectionCollection

planner: Runnable = llmChatModel.with_structured_output(SectionCollection)
