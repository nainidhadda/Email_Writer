import streamlit as st
import openai

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
    client = openai.OpenAI(
        api_key=OPENROUTER_API_KEY,
        base_url="https://openrouter.ai/api/v1"
    )
    response = client.chat.completions.create(
        model="meta-llama/llama-3-70b-instruct",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=400,
        temperature=0.7
    )
    return response.choices[0].message.content.strip()

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