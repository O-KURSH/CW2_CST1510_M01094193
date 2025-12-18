import streamlit as st

st.title("Chat with GPT-5.2")

prompt = st.chat_input("Ask me anything")

reply = st.chat_message('user').markdown(prompt)