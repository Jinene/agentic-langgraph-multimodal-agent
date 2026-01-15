from langgraph.graph import StateGraph, END
from typing import TypedDict, Optional
from .nodes import router_node, chat_node, tool_node, vision_node

class AgentState(TypedDict):
    input: str
    image: Optional[str]
    route: Optional[str]
    output: Optional[str]

graph = StateGraph(AgentState)

graph.add_node("router", router_node)
graph.add_node("chat", chat_node)
graph.add_node("tool", tool_node)
graph.add_node("vision", vision_node)

graph.set_entry_point("router")

graph.add_conditional_edges(
    "router",
    lambda state: state["route"],
    {
        "chat": "chat",
        "tool": "tool",
        "vision": "vision",
    },
)

graph.add_edge("chat", END)
graph.add_edge("tool", END)
graph.add_edge("vision", END)

agent_graph = graph.compile()
