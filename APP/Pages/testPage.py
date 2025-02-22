import streamlit as st
from openai import OpenAI
import ollama

st.title("ChatGPT-like clone")

# Set OpenAI API key from Streamlit secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Set a default model
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
    #     stream = client.chat.completions.create(
    #         model=st.session_state["openai_model"],
    #         messages=[
    #             {"role": m["role"], "content": m["content"]}
    #             for m in st.session_state.messages
    #         ],
    #         stream=True,
    #     )
    #     st.write(type(stream))
    #     response = st.write_stream(stream)

    # st.session_state.messages.append({"role": "assistant", "content": response})

        st.write("---")
        stream = ollama.chat(
            model='qwen2.5:7b',
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )
        st.write([
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ])
        st.write("---")

        # st.write(type(stream))

        def wrapper_stream(stream):
            for message in stream:
                yield message['message']['content']

        response = st.write_stream(wrapper_stream(stream))


    st.session_state.messages.append({"role": "assistant", "content": response})
    # st.session_state.messages.append({"role": "assistant", "content": stream['message']['content']})


theButton = st.button("Test")
if theButton:
    st.snow()
    st.write("Button clicked")
    st.video("https://www.youtube.com/watch?v=iIHBqEj6P94", autoplay=True)

theButton2 = st.button("Test2")
if theButton2:
    st.balloons()
    st.write("Button2 clicked")
    st.video("http://www.psychicbunny.com/video/JohnLoitumaRoss.320.h264.mov", autoplay=True, loop=True)
