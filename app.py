import streamlit as st
from chatbot_core import get_response

st.set_page_config(page_title="MedBot", layout="centered")
st.title("🤖 MedBot - AI Healthcare Assistant")

user_input = st.text_input("Ask me anything medical-related:")

if user_input:
    response = get_response(user_input)
    st.markdown(f"**MedBot:** {response}")


