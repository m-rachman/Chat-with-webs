import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage
from src import get_vectorstore_from_url,get_response


# app config
st.set_page_config(page_title="Chat with websites", page_icon="asset/alien_008.jpg")
st.title("Chat with websites")


website_url = st.text_input("Website URL",
                                placeholder='https://en.wikipedia.org/wiki/Artificial_intelligence') 

if website_url is None or website_url == "":
        st.info("Please provide a website URL and hit enter")

else:
    # session state
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = [
            AIMessage(content="Hello. How can I help you?"),
        ]
    if "vector_store" not in st.session_state:
        st.session_state.vector_store = get_vectorstore_from_url(website_url) 

    user_query = st.chat_input("Type your message here...")
    
    if user_query is not None and user_query != "":
        response = get_response(user_query)
        # input chat
        st.session_state.chat_history.append(HumanMessage(content=user_query))
        # output chat
        st.session_state.chat_history.append(AIMessage(content=response))

    # conversation
    for message in st.session_state.chat_history:
        if isinstance(message, AIMessage):
            with st.chat_message("AI",avatar='asset/alien_008.jpg'):
                st.write(message.content)
        elif isinstance(message, HumanMessage):
            with st.chat_message("Human",avatar='asset/human.jpg'):
                st.write(message.content)
