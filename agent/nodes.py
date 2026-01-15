from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage
from .prompts import ROUTER_PROMPT, CHAT_PROMPT, VISION_PROMPT
from .tools import calculator

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

def router_node(state):
    user_input = state["input"]
    response = llm.invoke(
        [HumanMessage(content=ROUTER_PROMPT + "\n\nUser input: " + user_input)]
    )
    return {"route": response.content.strip().lower()}

def chat_node(state):
    response = llm.invoke(
        [HumanMessage(content=CHAT_PROMPT + "\n\n" + state["input"])]
    )
    return {"output": response.content}

def tool_node(state):
    result = calculator(state["input"])
    return {"output": f"Tool result: {result}"}

def vision_node(state):
    image = state["image"]
    response = llm.invoke(
        [
            HumanMessage(
                content=[
                    {"type": "text", "text": VISION_PROMPT + "\n" + state["input"]},
                    {"type": "image_url", "image_url": image},
                ]
            )
        ]
    )
    return {"output": response.content}
