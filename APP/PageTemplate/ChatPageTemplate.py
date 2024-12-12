import streamlit as st
import ollama


def ChatPageTemplate(subHeader = None, chatFunction = None, streamSupported = False):

    st.title("LivermoreGPT")
    if subHeader:
        st.subheader(subHeader)

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

            stream = chatFunction();

            if streamSupported:
                response = st.write_stream(stream)
            else:
                response = st.write(stream)

        st.session_state.messages.append({"role": "assistant", "content": response})
