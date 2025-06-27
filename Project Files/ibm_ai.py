from ibm_watsonx_ai.foundation_models import ModelInference
from ibm_watsonx_ai.foundation_models.utils.enums import DecodingMethods
from ibm_watsonx_ai import Credentials
import streamlit as st
from textblob import TextBlob  # Only if you're still using TextBlob

# ✅ Load credentials securely from .streamlit/secrets.toml
api_key = st.secrets["api_key"]
project_id = st.secrets["project_id"]
url = st.secrets["url"]

# ✅ Setup IBM Granite model
creds = Credentials(api_key=api_key, url=url)
model = ModelInference(
    model_id="ibm/granite-3-2b-instruct",
    credentials=creds,
    params={
        "decoding_method": DecodingMethods.GREEDY,
        "max_new_tokens": 100
    },
    project_id=project_id
)

# ✅ Get response from Granite
def get_watsonx_response(prompt):
    try:
        response = model.generate(prompt=prompt)
        return response.get("results", [{}])[0].get("generated_text", "No response")
    except Exception as e:
        return f"Error: {str(e)}"

# ✅ Basic Sentiment Analysis (You can improve this further)
def analyze_sentiment(text):
    text = text.lower()
    if any(word in text for word in ['good', 'great', 'happy', 'resolved', 'thank']):
        return 'Positive'
    elif any(word in text for word in ['bad', 'not', 'worst', 'dirty', 'angry', 'problem']):
        return 'Negative'
    else:
        return 'Neutral'