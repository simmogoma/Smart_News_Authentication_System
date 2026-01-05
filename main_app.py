import streamlit as st
import google.generativeai as genai

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title=4vce wsxa"Smart News Authentication System",
    page_icon="📰",
    layout="centered"
)

# ---------------- GEMINI CONFIG ----------------
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-pro")

# ---------------- UI HEADER ----------------
st.markdown(
    """
    <h1 style="text-align:center;color:#1F4E79;">📰 Smart News Authentication System</h1>
    <p style="text-align:center;color:gray;">
    AI-based system to verify the authenticity of news articles
    </p>
    """,
    unsafe_allow_html=True
)

st.divider()

# ---------------- INPUT SECTION ----------------
st.subheader("🔍 Enter News Content")
news_text = st.text_area(
    label="Paste news text below",
    height=220,
    placeholder="Paste any news article here to check whether it is Fake or Real..."
)

# ---------------- BUTTON ACTION ----------------
if st.button("Verify News", use_container_width=True):
    if news_text.strip() == "":
        st.warning("⚠️ Please enter news content before verification.")
    else:
        with st.spinner("Analyzing news using Artificial Intelligence..."):
            prompt = f"""
            You are an expert AI news fact-checker.

            Analyze the following news text and classify it into one of the categories:
            - Real
            - Fake
            - Uncertain

            Additionally provide:
            1. Confidence percentage
            2. Short explanation (2–3 lines)

            News Text:
            {news_text}

            Respond strictly in the following format:

            Verdict:
            Confidence:
            Explanation:
            """

            response = model.generate_content(prompt)
            result = response.text

        st.success("✅ News Analysis Completed")

        # ---------------- RESULT DISPLAY ----------------
        st.markdown(
            f"""
            <div style="
                background-color:#F4F6F7;
                padding:20px;
                border-radius:10px;
                border-left:6px solid #2874A6;
                font-size:15px;
            ">
            <pre style="white-space:pre-wrap;">{result}</pre>
            </div>
            """,
            unsafe_allow_html=True
        )

# ---------------- FOOTER ----------------
st.divider()
st.markdown(
    """
    <p style="text-align:center;color:gray;font-size:13px;">
    Final Year Project | Python with Artificial Intelligence
    </p>
    """,
    unsafe_allow_html=True
)