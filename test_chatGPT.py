
from openai import OpenAI
import streamlit as st

client = OpenAI(api_key="")

if 'messages' not in st.session_state:
    st.session_state.messages = []


for message in st.session_state.messages:
    st.chat_message(message["role"]).markdown(message['content'])



prompt = st.chat_input('Enter your prompt')

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message('user').markdown(prompt)


    completion = client.chat.completions.create(
    model="gpt-5.2",
    messages=st.session_state.messages
    )

    reply = completion.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": reply})
    st.chat_message('assistant').markdown(reply)

