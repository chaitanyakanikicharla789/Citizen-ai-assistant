import streamlit as st
import json
import os
from ibm_ai import get_watsonx_response, analyze_sentiment

# ✅ Load issues from JSON file
def load_predefined_issues():
    try:
        file_path = os.path.join(os.path.dirname(__file__), "predefined_issues.json")
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f).get("issues", [])
    except FileNotFoundError:
        st.error("❌ 'predefined_issues.json' file not found.")
        return []
    except json.JSONDecodeError:
        st.error("❌ Error parsing 'predefined_issues.json'. Check format!")
        return []

# ✅ Match query to predefined issue
def match_predefined(query, issues):
    query = query.strip().lower()
    for item in issues:
        if item["query"].strip().lower() in query:
            return item["response"]
    return None

# ✅ Main Chat UI
def chat_page():
    st.title("🧠 Citizen Chat Assistant")
    st.markdown("Ask any civic question or report an issue:")

    user_input = st.text_input("💬 Enter your question or issue")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    if user_input:
        issues = load_predefined_issues()
        predefined_response = match_predefined(user_input, issues)

        if predefined_response:
            ai_response = predefined_response
            source = "Predefined"
        else:
            ai_response = get_watsonx_response(user_input)
            source = "Watsonx AI"

        sentiment = analyze_sentiment(user_input)

        # Store in chat history
        st.session_state.chat_history.append({
            "query": user_input,
            "response": ai_response,
            "sentiment": sentiment,
            "source": source
        })

    # ✅ Display full chat history
    for chat in reversed(st.session_state.chat_history):
        st.markdown(f"**🧑‍💬 You:** {chat['query']}")
        st.markdown(f"**🤖 {chat['source']} Response:** {chat['response']}")
        st.markdown(f"**📊 Sentiment:** {chat['sentiment']}")
        st.markdown("---")
