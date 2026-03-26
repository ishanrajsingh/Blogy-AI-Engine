import streamlit as st
import requests

st.set_page_config(page_title="Blogy AI Engine", layout="wide")

st.title("🚀 Blogy AI Engine")

keyword = st.text_input("Enter Keyword")

if st.button("Generate Blog"):
    with st.spinner("Generating SEO Blog..."):
        res = requests.post(
            "http://localhost:8000/generate-blog",
            json={"keyword": keyword}
        )

        data = res.json()

        st.subheader("📊 SEO Metrics")
        st.json(data["seo"])

        st.subheader("🧠 Keyword Analysis")
        st.json(data["keywords"])

        st.subheader("✍️ Blog Output")
        st.markdown(data["blog"], unsafe_allow_html=True)