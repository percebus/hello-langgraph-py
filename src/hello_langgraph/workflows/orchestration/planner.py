from hello_langgraph.workflows.model import llmChatModel
from hello_langgraph.workflows.orchestration.sections import Sections


planner = llmChatModel.with_structured_output(Sections)
