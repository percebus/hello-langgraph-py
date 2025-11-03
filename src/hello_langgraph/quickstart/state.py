# SRC: https://docs.langchain.com/oss/python/langgraph/quickstart#2-define-state

from langchain.messages import AnyMessage
from typing_extensions import TypedDict, Annotated
import operator


class MessagesStateTypedDict(TypedDict):
    messages: Annotated[list[AnyMessage], operator.add]
    llm_calls: int
