# SRC: https://docs.langchain.com/oss/python/langgraph/quickstart#1-define-tools-and-model
# SRC: https://docs.langchain.com/oss/python/langgraph/quickstart#3-define-model-node

import os

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain.messages import SystemMessage
from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.runnables.base import Runnable

from hello_langgraph.quickstart.tools import tools

# SRC: https://docs.langchain.com/oss/python/langchain/models#initialize-a-model
# os.environ["AZURE_OPENAI_API_KEY"] = "..."
# os.environ["AZURE_OPENAI_ENDPOINT"] = "..."
# os.environ["OPENAI_API_VERSION"] = "2025-03-01-preview"

# Load environment variables from .env file
load_dotenv()


oChatModel: BaseChatModel = init_chat_model("azure_openai:gpt-4o", azure_deployment=os.environ["AZURE_OPENAI_DEPLOYMENT_NAME"], temperature=0)

model_with_tools: Runnable = oChatModel.bind_tools(tools)


def llm_call(state: dict):
    """LLM decides whether to call a tool or not"""

    return {
        "messages": [
            model_with_tools.invoke(
                [SystemMessage(content="You are a helpful assistant tasked with performing arithmetic on a set of inputs.")] + state["messages"]
            )
        ],
        "llm_calls": state.get("llm_calls", 0) + 1,
    }
