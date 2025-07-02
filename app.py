import streamlit as st
import requests

OPENROUTER_API_KEY = "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"

st.title("OpenRouter Email Generator (Llama-3)")

subject = st.text_input("Email Subject")
context = st.text_area("Context/Details")
tone = st.selectbox("Tone", ["formal", "friendly", "apologetic", "persuasive", "concise"])

def generate_email(subject, context, tone):
    prompt = (
        f"Write a {tone} and well-written email based on the following details:\n"
        f"Subject: {subject}\n"
        f"Context: {context}\n"
        f"Email:"
    )
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "meta-llama/llama-3-70b-instruct",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 400,
        "temperature": 0.7
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"].strip()
    else:
        raise Exception(f"OpenRouter API error: {response.text}")

if st.button("Generate Email"):
    if subject and context and tone:
        with st.spinner("Generating..."):
            try:
                email = generate_email(subject, context, tone)
                st.subheader("Generated Email")
                st.write(email)
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please fill in all fields.") 