import streamlit as st
from textblob import TextBlob

# Custom CSS for Modern UI 🎨
st.markdown("""
<style>
/* Main Background Gradient */
.stApp {
    background: linear-gradient(135deg, #0f2027 0%, #203a43 50%, #2c5364 100%);
    color: white;
}

/* 1. Hide default white header */
[data-testid="stHeader"] {
    background-color: transparent;
}

/* Title & Subtitle */
h1 {
    color: #00d2ff !important;
    text-align: center;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
}
.stMarkdown p {
    font-size: 18px;
    text-align: center;
    color: #e0e0e0;
}

/* 2. Input Label Text Color */
label, .stTextArea label p {
    color: #00d2ff !important;
    font-size: 16px !important;
    font-weight: bold;
}

/* Text Area */
.stTextArea textarea {
    border-radius: 15px;
    border: 2px solid #00d2ff;
    background-color: rgba(255, 255, 255, 0.95);
    color: #000;
}

/* Button */
.stButton>button {
    width: 100%;
    border-radius: 25px;
    background-color: #ff4b4b;
    color: white;
    font-size: 18px;
    font-weight: bold;
    border: none;
    padding: 10px;
    transition: 0.3s;
}
.stButton>button:hover {
    background-color: #ff1c1c;
    transform: scale(1.02);
}

/* 3. Output Message (Alert) Styling */
[data-testid="stAlert"] {
    background-color: rgba(0, 0, 0, 0.6) !important;
    border-radius: 10px;
    border-left: 5px solid #00d2ff;
}
[data-testid="stAlert"] * {
    color: white !important;
}
</style>
""", unsafe_allow_html=True)

# Rest of the Web App Logic 🧠
st.title("Sentiment Analysis Web App 🎭")
st.write("Enter your text below to know if it's Positive, Negative, or Neutral!")

user_input = st.text_area("Enter your text here:", height=150)

if st.button("Analyze Sentiment"):
    if user_input:
        blob = TextBlob(user_input)
        score = blob.sentiment.polarity
        
        if score > 0:
            st.success(f"🌟 Result: Positive Sentiment (Score: {score:.2f})")
        elif score < 0:
            st.error(f"😔 Result: Negative Sentiment (Score: {score:.2f})")
        else:
            st.info(f"😐 Result: Neutral Sentiment (Score: {score:.2f})")
    else:
        st.warning("Please enter some text first!")