import streamlit as st
import PageTemplate.ChatPageTemplate as ChatPageTemplate
from openai import OpenAI

# Set OpenAI API key from Streamlit secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])


def chatFunction():
    stream = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": m["role"], "content": m["content"]}
            for m in st.session_state.messages
        ],
        stream=True,
    )
    return stream

ChatPageTemplate.ChatPageTemplate(
    subHeader="LivermoreGPT with GPT-4o via OpenAI",
    chatFunction=chatFunction,
    streamSupported=True
)