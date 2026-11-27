import streamlit as st
import google.generativeai as genai

# अपनी Google Gemini API key यहाँ डालो
API_KEY = "AQ.Ab8RN6K0pPLuP0_Jonf1q9CERE0Mu6H2v-qYYDHsNzfT9dWZcg"

genai.configure(api_key=API_KEY)

# टेस्ट फाइल में जो मॉडल का नाम आया था, वो यहाँ लिखो (जैसे 'gemini-1.5-flash' या 'gemini-pro')
model = genai.GenerativeModel('gemini-3.8-flash')

st.set_page_config(page_title="Tanmay Ai", page_icon="🤖")
st.title("🤖 Tanmay Ai Chat Assistant")

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Hello! Main Tanmay hoon. Aap mujhse kuch bhi pooch sakte hain."}]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Yahan apna sawal likhein..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Tanmay soch raha hai..."):
            try:
                response = model.generate_content(prompt)
                reply = response.text
                st.markdown(reply)
                st.session_state.messages.append({"role": "assistant", "content": reply})
            except Exception as e:
                st.error(f"Error aa gaya: {e}")