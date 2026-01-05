import streamlit as st
import openai

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Smart News Authentication System",
    page_icon="📰",
    layout="centered"
)

# ---------------- API KEY CONFIG ----------------
# API key from Streamlit Secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

# ---------------- UI HEADER ----------------
st.markdown(
    """
    <h1 style="text-align:center;color:#1F4E79;">📰 Smart News Authentication System</h1>
    <p style="text-align:center;color:gray;">
    Verify whether a news article is Fake or Real using AI
    </p>
    """,
    unsafe_allow_html=True
)

st.divider()

# ---------------- INPUT SECTION ----------------
st.subheader("🔍 Enter News Content")
news_text = st.text_area(
    "Paste the news text here:",
    height=220,
    placeholder="Enter news article to verify..."
)

# ---------------- VERIFY BUTTON ----------------
if st.button("Verify News", use_container_width=True):
    if news_text.strip() == "":
        st.warning("⚠️ Please enter news content.")
    else:
        with st.spinner("Analyzing news using AI..."):
            prompt = f"""
            You are an expert AI fact-checker.

            Analyze the following news text and classify it into:
            - Real
            - Fake
            - Uncertain

            Also provide:
            1. Confidence percentage
            2. Short explanation (2-3 lines)

            News Text:
            {news_text}

            Respond strictly in this format:

            Verdict:
            Confidence:
            Explanation:
            """
            
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=prompt,
                max_tokens=200,
                temperature=0
            )
            result = response.choices[0].text.strip()

        st.success("✅ Analysis Complete")

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
    Final Year Project | Python with AI
    </p>
    """,
    unsafe_allow_html=True
)