import streamlit as st
from dotenv import load_dotenv
from agent.graph import agent_graph
import base64

load_dotenv()

st.set_page_config(page_title="Agentic LangGraph Multimodal Agent")
st.title("🤖 Agentic LangGraph Multimodal Agent")

user_input = st.text_input("Ask something:")

uploaded_image = st.file_uploader("Upload an image (optional)", type=["png", "jpg", "jpeg"])

image_url = None
if uploaded_image:
    bytes_data = uploaded_image.getvalue()
    image_url = f"data:image/jpeg;base64,{base64.b64encode(bytes_data).decode()}"

if st.button("Run Agent"):
    if not user_input:
        st.warning("Please enter a question.")
    else:
        state = {
            "input": user_input,
            "image": image_url,
        }
        result = agent_graph.invoke(state)
        st.success("Response:")
        st.write(result["output"])
