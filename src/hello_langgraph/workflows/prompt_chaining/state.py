from typing_extensions import TypedDict


# Graph state
class StateTypedDict(TypedDict):
    topic: str
    joke: str
    improved_joke: str
    final_joke: str
