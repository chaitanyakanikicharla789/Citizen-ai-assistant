import streamlit as st
import json
import os
from ibm_ai import get_watsonx_response, analyze_sentiment

def load_predefined_issues():
    try:
        file_path = os.path.join(os.path.dirname(__file__), "predefined_issues.json")
        with open(file_path, "r") as f:
            return json.load(f)["issues"]
    except:
        return []

def chat_page():
    st.title("🧠 Citizen Chat Assistant")
    st.write("Ask any civic question or report an issue:")

    predefined_issues = load_predefined_issues()
    user_input = st.text_input("💬 Enter your question or issue", key="chat_input")

    # ✅ This is the missing part — Submit Button
    if st.button("Submit"):
        if user_input.strip() == "":
            st.warning("⚠️ Please enter a question.")
        else:
            # ✅ Check if it matches predefined
            for issue in predefined_issues:
                if issue["query"].lower() in user_input.lower():
                    st.success("✅ Predefined Response:")
                    st.write(issue["response"])
                    sentiment = analyze_sentiment(user_input)
                    st.info(f"📊 Sentiment: {sentiment}")
                    return

            # ✅ Otherwise get Watsonx response
            response = get_watsonx_response(user_input)
            sentiment = analyze_sentiment(user_input)

            st.success("🤖 Watsonx AI Response:")
            st.write(response)
            st.info(f"📊 Sentiment: {sentiment}")
