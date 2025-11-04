from typing import Annotated, TypedDict
import operator

# Graph state
from hello_langgraph.workflows.orchestration.sections import Section


class StateTypedDict(TypedDict):
    topic: str  # Report topic
    sections: list[Section]  # List of report sections
    completed_sections: Annotated[
        list, operator.add
    ]  # All workers write to this key in parallel
    final_report: str  # Final report


# Worker state
class WorkerStateTypedDict(TypedDict):
    section: Section
    completed_sections: Annotated[list, operator.add]
