import streamlit as st
import PageTemplate.ChatPageTemplate as ChatPageTemplate
import ollama
from streamlit import subheader

def chatFunction():
    stream = ollama.chat(
        model='qwen2.5:7b',
        messages=[
            {"role": m["role"], "content": m["content"]}
            for m in st.session_state.messages
        ],
        stream=True,
    )

    def wrapper_stream(stream):
        for message in stream:
            yield message['message']['content']

    return wrapper_stream(stream)

ChatPageTemplate.ChatPageTemplate(
    subHeader="LivermoreGPT with Qwen2.5:7b via Ollama",
    chatFunction=chatFunction,
    streamSupported=True
)
