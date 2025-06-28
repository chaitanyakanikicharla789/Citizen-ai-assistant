from ibm_watsonx_ai.foundation_models import Model
from ibm_watsonx_ai.metanames import GenTextParams
from ibm_watsonx_ai import APIClient
import streamlit as st
from textblob import TextBlob

# ✅ Load credentials from Streamlit secrets
api_key = st.secrets["ibm"]["api_key"]
project_id = st.secrets["ibm"]["project_id"]
url = st.secrets["ibm"]["url"]
model_id = st.secrets["ibm"]["model_id"]

# ✅ Setup IBM Watsonx Client
creds = {
    "url": url,
    "apikey": api_key
}
client = APIClient(creds)
client.set.default_project_id(project_id)

# ✅ Generate response using Granite model
def get_watsonx_response(prompt):
    params = {
        GenTextParams.DECODING_METHOD: "greedy",
        GenTextParams.MAX_NEW_TOKENS: 150,
        GenTextParams.TEMPERATURE: 0.7
    }

    try:
        model = Model(
            model_id=model_id,
            params=params,
            client=client
        )
        response = model.generate_text(prompt)
        return response.get("generated_text", "No response generated.")
    except Exception as e:
        return f"Error from Watsonx: {e}"

# ✅ Sentiment Analysis Function
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
