import streamlit as st
import pandas as pd
from data_stream import stream_data
from sentiment import analyze_sentiment

st.set_page_config(page_title="Realtime Social Media Analytics", layout="wide")
st.title("📊 Realtime Social Media Analytics Dashboard")

data = []
placeholder = st.empty()

for post in stream_data():
    sentiment = analyze_sentiment(post["post"])
    post["sentiment"] = sentiment
    data.append(post)

    df = pd.DataFrame(data)

    with placeholder.container():
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Live Feed")
            st.dataframe(df.tail(5))

        with col2:
            st.subheader("Sentiment Distribution")
            st.bar_chart(df["sentiment"].value_counts())
