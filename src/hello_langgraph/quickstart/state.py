# SRC: https://docs.langchain.com/oss/python/langgraph/quickstart#2-define-state

import operator

from langchain.messages import AnyMessage
from typing_extensions import Annotated, TypedDict


class MessagesStateTypedDict(TypedDict):
    messages: Annotated[list[AnyMessage], operator.add]
    llm_calls: int
