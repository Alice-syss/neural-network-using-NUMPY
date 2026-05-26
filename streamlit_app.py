import os
import streamlit as st
from dotenv import load_dotenv
import anthropic

load_dotenv()

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

SYSTEM_PROMPT = """You are a strict but supportive study buddy. Your job is to help the user actually learn — not just give them answers.

Follow these rules:
1. When the user asks you to explain something — explain it simply, like they are 16 years old
2. When the user says they understood something — quiz them with one question to test it
3. When they answer a quiz question — tell them honestly if they are right or wrong, and why
4. If they are wrong — explain it again differently, then quiz them again
5. Keep responses short and focused. No essays.
6. Remember what topic they are studying throughout the conversation.

You are not a search engine. You are a tutor who actually cares if they learn."""

st.set_page_config(page_title="Study Buddy", page_icon="📚")
st.title("📚 Study Buddy")
st.caption("Tell me what you're studying. I'll explain it, then quiz you.")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

user_input = st.chat_input("What are you studying today?")

if user_input:
    with st.chat_message("user"):
        st.write(user_input)

    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

 
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1000,
        system=SYSTEM_PROMPT,
        messages=st.session_state.messages
    )

    reply = response.content[0].text

    with st.chat_message("assistant"):
        st.write(reply)

    st.session_state.messages.append({
        "role": "assistant",
        "content": reply
    })