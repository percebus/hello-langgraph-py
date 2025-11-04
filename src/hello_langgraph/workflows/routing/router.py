from langchain.messages import HumanMessage, SystemMessage

from hello_langgraph.workflows.routing.state import RoutingStateTypedDict
from hello_langgraph.workflows.routing.structured_output import get_route


def llm_call_router(state: RoutingStateTypedDict):
    """Route the input to the appropriate node"""

    # Run the augmented LLM with structured output to serve as routing logic
    decision = get_route.invoke(
        [
            SystemMessage(content="Route the input to story, joke, or poem based on the user's request."),
            HumanMessage(content=state["input"]),
        ]
    )

    return {"decision": decision.step}
