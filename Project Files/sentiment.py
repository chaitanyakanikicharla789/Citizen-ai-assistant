def analyze_sentiment(text):
    text = text.lower()
    if any(word in text for word in ['good', 'great', 'happy', 'resolved', 'thank']):
        return 'positive'
    elif any(word in text for word in ['bad', 'not', 'worst', 'dirty', 'angry', 'problem']):
        return 'negative'
    else:
        return 'neutral'
