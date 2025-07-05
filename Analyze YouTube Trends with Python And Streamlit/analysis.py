import pandas as pd
from textblob import TextBlob

def load_data():
    df = pd.read_csv("/Users/yashbhilare21/College Folder/Projects/Analyze YouTube Trends with a Dashboard/Analyze YouTube Trends with Python And Streamlit/Dataset/videos-stats.csv")
    df.drop(columns=["Unnamed: 0"], errors='ignore', inplace=True)
    df['Published At'] = pd.to_datetime(df['Published At'])
    df.fillna(0, inplace=True)

    df = assign_categories(df)
    df = add_sentiment(df)
    return df

def assign_categories(df):
    keyword_to_category = {
        "tech": "Technology",
        "gadgets": "Technology",
        "music": "Entertainment",
        "vlog": "Lifestyle",
        "travel": "Lifestyle",
        "review": "Technology",
        "education": "Education",
        "game": "Gaming",
        "funny": "Entertainment",
        "news": "News",
    }
    df["Category"] = df["Keyword"].apply(lambda k: keyword_to_category.get(str(k).lower(), "Other"))
    return df

def add_sentiment(df):
    def get_sentiment(text):
        blob = TextBlob(str(text))
        polarity = blob.sentiment.polarity
        if polarity > 0.1:
            return "Positive"
        elif polarity < -0.1:
            return "Negative"
        else:
            return "Neutral"
    df["Sentiment"] = df["Title"].apply(get_sentiment)
    return df

def top_videos_by_views(df, n=10):
    return df.sort_values(by='Views', ascending=False).head(n)

def top_videos_by_likes(df, n=10):
    return df.sort_values(by='Likes', ascending=False).head(n)

def top_videos_by_comments(df, n=10):
    return df.sort_values(by='Comments', ascending=False).head(n)

def daily_metrics(df):
    return df.groupby(df['Published At'].dt.date)[['Views', 'Likes', 'Comments']].sum()