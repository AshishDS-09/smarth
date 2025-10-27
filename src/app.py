import streamlit as st # type: ignore
from api.query_handler import answer_question


st.title("Project Samarth - Intelligent Q&A on Agriculture")

user_question = st.text_input("Ask your question about India's agriculture:")

if user_question:
    with st.spinner("Fetching answer..."):
        answer, sources = answer_question(user_question)
        st.markdown("### Answer")
        st.write(answer)
        st.markdown("### Sources")
        for src in sources:
            st.write(f"- {src}")
