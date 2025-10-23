import streamlit as st # type: ignore
from src.api.query_handler import answer_question

st.title("Project Samarth - Intelligent Q&A on Agriculture & Climate")

user_question = st.text_input("Ask your question about India's agriculture and climate:")

if user_question:
    with st.spinner("Fetching answer..."):
        answer, sources = answer_question(user_question)
        st.markdown("### Answer")
        st.write(answer)
        st.markdown("### Sources")
        for src in sources:
            st.write(f"- {src}")
