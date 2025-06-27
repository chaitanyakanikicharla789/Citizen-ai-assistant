import streamlit as st
import json
import os
from ibm_ai import get_watsonx_response, analyze_sentiment

def load_predefined_issues():
    try:
        # Safe path to load JSON file
        file_path = os.path.join(os.path.dirname(__file__), "predefined_issues.json")
        with open(file_path, "r") as f:
            return json.load(f)["issues"]
    except FileNotFoundError:
        st.error("❌ predefined_issues.json file not found!")
        return []
    except json.JSONDecodeError:
        st.error("❌ Error decoding predefined_issues.json. Check its format!")
        return []

def chat_page():
    st.title("🧠 Citizen Chat Assistant")
    st.write("Ask any civic question or report an issue:")

    predefined_issues = load_predefined_issues()

    user_input = st.text_input("💬 Enter your question or issue")

    if st.button("Submit"):
        if user_input.strip() == "":
            st.warning("⚠️ Please enter a question.")
        else:
            # Check for match in predefined issues
            matched = False
            for item in predefined_issues:
                if item["query"].lower() in user_input.lower():
                    st.success("✅ Predefined Response:")
                    st.write(item["response"])
                    matched = True
                    break

            if not matched:
                # Use Watsonx fallback
                response = get_watsonx_response(user_input)
                sentiment = analyze_sentiment(user_input)

                st.success("🤖 AI Response:")
                st.write(response)

                st.info(f"📊 Sentiment: {sentiment}")
