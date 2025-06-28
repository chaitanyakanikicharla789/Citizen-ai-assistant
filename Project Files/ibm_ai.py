from ibm_watsonx_ai.foundation_models import ModelInference
from ibm_watsonx_ai.foundation_models.utils.enums import DecodingMethods
from ibm_watsonx_ai import Credentials
import streamlit as st
from textblob import TextBlob  # Optional for better sentiment classification

# ✅ Load credentials from Streamlit secrets
api_key = st.secrets["ibm"]["api_key"]
project_id = st.secrets["ibm"]["project_id"]
url = st.secrets["ibm"]["url"]
model_id = st.secrets["ibm"]["model_id"]

# ✅ Setup Watsonx Granite model
creds = Credentials(api_key=api_key, url=url)

model = ModelInference(
    model_id=model_id,
    credentials=creds,
    params={
        "decoding_method": DecodingMethods.GREEDY,
        "max_new_tokens": 150,
        "temperature": 0.7
    },
    project_id=project_id
)

# ✅ Get response from IBM Watsonx model
def get_watsonx_response(prompt):
    try:
        response = model.generate(prompt=prompt)
        return response.get("results", [{}])[0].get("generated_text", "No response generated.")
    except Exception as e:
        return f"Error from Watsonx: {str(e)}"

# ✅ Sentiment analysis using keywords and TextBlob
def analyze_sentiment(text):
    text = text.lower()
    if any(word in text for word in ['good', 'great', 'happy', 'resolved', 'thank']):
        return 'Positive'
    elif any(word in text for word in ['bad', 'not', 'worst', 'dirty', 'angry', 'problem']):
        return 'Negative'
    else:
        try:
            polarity = TextBlob(text).sentiment.polarity
            if polarity > 0.2:
                return "Positive"
            elif polarity < -0.2:
                return "Negative"
            else:
                return "Neutral"
        except:
            return "Neutral"
