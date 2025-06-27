import streamlit as st
import json
import os
from ibm_ai import get_watsonx_response, analyze_sentiment

def chat_page():
    st.title("🧠 Citizen Chat Assistant")

    # Load predefined issues
    try:
        with open("predefined_issues.json", "r", encoding="utf-8") as f:
            predefined = json.load(f)
    except FileNotFoundError:
        st.error("❌ predefined_issues.json file not found!")
        return

    # Load chat history
    data = {"sentiments": []}
    if os.path.exists("data.json"):
        with open("data.json", "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                st.warning("⚠️ data.json is corrupted. Starting fresh.")

    # UI input
    user_input = st.text_input("💬 Ask the Assistant:")

    if st.button("Submit"):
        if user_input.strip():
            question = user_input.strip()
            answer = None

            # Check predefined answers
            for item in predefined.get("issues", []):
                if item["question"].lower() in question.lower():
                    answer = item["answer"]
                    break

            # If not in predefined, use Watsonx
            if not answer:
                answer = get_watsonx_response(question)

            # Analyze sentiment
            sentiment = analyze_sentiment(question)

            # Save entry
            entry = {"question": question, "answer": answer, "sentiment": sentiment}
            data["sentiments"].append(entry)

            with open("data.json", "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4)

            # Display output
            st.success("✅ Response received!")
            st.markdown(f"**Answer:** {answer}")
            st.markdown(f"🧭 Sentiment: **{sentiment}**")
        else:
            st.warning("⚠️ Please fill out this field before submitting.")

    # Show recent chats
    st.subheader("🕓 Recent Questions")
    if data["sentiments"]:
        for entry in reversed(data["sentiments"][-3:]):
            st.markdown(f"**Q:** {entry['question']}  \n**A:** {entry['answer']}  \n_Sentiment: {entry['sentiment']}_")
    else:
        st.info("No chat history yet.")
