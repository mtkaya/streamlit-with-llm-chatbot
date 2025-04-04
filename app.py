import streamlit as st
import requests

st.set_page_config(page_title="Streamlit with LLM ChatBot", layout="wide")
st.title("🤖 Streamlit with LLM ChatBot")

model = st.selectbox("Model Seçin", ["llama3", "phi3", "mistral"])
user_input = st.text_input("Sorunuzu yazın:")

if st.button("Gönder") and user_input:
    response = requests.post("http://localhost:8000/sohbet", json={
        "soru": user_input,
        "model": model
    })
    yanit = response.json().get("yanit", "")
    st.write(f"✉️ Yanıt: {yanit}")

