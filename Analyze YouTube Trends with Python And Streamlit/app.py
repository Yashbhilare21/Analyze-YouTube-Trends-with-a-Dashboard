import streamlit as st
import plotly.express as px
from analysis import load_data, top_videos_by_views, top_videos_by_likes, top_videos_by_comments, daily_metrics

st.set_page_config(layout="wide", page_title="YouTube Trends Dashboard")
st.title("📺 YouTube Trends Dashboard")

df = load_data()

# Sidebar Filters
st.sidebar.header("Filters")
keyword_filter = st.sidebar.selectbox("Select Keyword", ["All"] + sorted(df["Keyword"].unique().tolist()))
if keyword_filter != "All":
    df = df[df["Keyword"] == keyword_filter]

# Show Metrics
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Top Videos by Views")
    st.dataframe(top_videos_by_views(df)[['Title', 'Views']])

with col2:
    st.subheader("Top Videos by Likes")
    st.dataframe(top_videos_by_likes(df)[['Title', 'Likes']])

with col3:
    st.subheader("Top Videos by Comments")
    st.dataframe(top_videos_by_comments(df)[['Title', 'Comments']])

# Line Chart for Daily Trends
st.subheader("📈 Daily Metrics Over Time")
metrics_df = daily_metrics(df).reset_index()
fig = px.line(metrics_df, x='Published At', y=['Views', 'Likes', 'Comments'], markers=True)
st.plotly_chart(fig, use_container_width=True)

# Pie Chart - Sentiment Distribution
st.subheader("💬 Sentiment Distribution")
sentiment_counts = df['Sentiment'].value_counts()
fig_sentiment = px.pie(values=sentiment_counts.values, names=sentiment_counts.index, title="Video Title Sentiment")
st.plotly_chart(fig_sentiment, use_container_width=True)

# Bar Chart - Views by Category
st.subheader("📂 Category-wise Total Views")
category_views = df.groupby("Category")["Views"].sum().reset_index().sort_values(by="Views", ascending=False)
fig_category = px.bar(category_views, x="Category", y="Views", title="Total Views per Category")
st.plotly_chart(fig_category, use_container_width=True)