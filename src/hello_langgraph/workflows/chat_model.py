# Schema for structured output
import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.language_models.chat_models import BaseChatModel

load_dotenv()
llmChatModel: BaseChatModel = init_chat_model(
    "azure_openai:gpt-4o",
    azure_deployment=os.environ["AZURE_OPENAI_DEPLOYMENT_NAME"],
    temperature=0
)
