import streamlit as st
import json
import os
from ibm_ai import analyze_sentiment  # your Watsonx sentiment function

def dashboard_page():
    st.title("📊 Citizen Insights Dashboard")

    # Load data
    if os.path.exists("data.json"):
        with open("data.json", "r", encoding="utf-8") as f:
            data = json.load(f)
    else:
        data = {"sentiments": [], "issues": []}

    sentiments = data.get("sentiments", [])
    issues = data.get("issues", [])

    # Sentiment Counts
    pos = sum(1 for s in sentiments if s["sentiment"] == "Positive")
    neu = sum(1 for s in sentiments if s["sentiment"] == "Neutral")
    neg = sum(1 for s in sentiments if s["sentiment"] == "Negative")

    st.subheader("Weekly Sentiment Summary")
    st.write(f"✅ Positive: {pos}")
    st.write(f"😐 Neutral: {neu}")
    st.write(f"❌ Negative: {neg}")

    # New: Enter feedback for sentiment analysis
    st.subheader("💬 Enter Feedback for Sentiment")
    feedback = st.text_area("Enter your feedback here:")
    if st.button("Analyze Feedback") and feedback.strip():
        sentiment = analyze_sentiment(feedback.strip())
        st.info(f"🧠 Detected Sentiment: **{sentiment}**")
        # Save feedback and sentiment
        data["sentiments"].append({
            "question": feedback.strip(),
            "answer": "",
            "sentiment": sentiment
        })
        with open("data.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        st.success("✅ Feedback and sentiment saved!")

    # Report New Issue
    st.subheader("📌 Report a Civic Issue")
    new_issue = st.text_area("Describe your issue:")
    if st.button("Submit Issue") and new_issue.strip():
        issues.append(new_issue.strip())
        data["issues"] = issues
        with open("data.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        st.success("✅ Issue submitted successfully!")

    # Show Issues
    st.subheader("🛠️ Recent Reported Issues")
    if issues:
        for i, issue in enumerate(reversed(issues[-5:]), 1):
            st.markdown(f"{i}. {issue}")
    else:
        st.write("No issues reported yet.")
