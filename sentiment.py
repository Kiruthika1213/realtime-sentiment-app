def analyze_sentiment(text):
    text = text.lower()

    if "love" in text or "amazing" in text or "happy" in text or "good" in text:
        return "positive"
    elif "bad" in text or "worst" in text or "not" in text:
        return "negative"
    else:
        return "neutral"
