from langgraph.graph import StateGraph, MessagesState, START, END

def mock_llm(state: MessagesState):
    return {"messages": [{"role": "ai", "content": "hello world"}]}

oStateGraph = StateGraph(MessagesState)
oStateGraph.add_node(mock_llm)
oStateGraph.add_edge(START, "mock_llm")
oStateGraph.add_edge("mock_llm", END)
oStateGraph = oStateGraph.compile()

oStateGraph.invoke({
    "messages": [
        {"role": "user", "content": "hi!"}
    ]
})
