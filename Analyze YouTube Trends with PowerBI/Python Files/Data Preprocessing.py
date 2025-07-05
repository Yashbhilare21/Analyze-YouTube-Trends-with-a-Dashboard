import pandas as pd
from textblob import TextBlob

# Load original data
df = pd.read_csv("/Users/yashbhilare21/College Folder/Projects/Analyze YouTube Trends with a Dashboard/Analyze YouTube Trends with PowerBI/Dataset/videos-stats.csv")

# Convert 'Published At' to datetime
df["Published At"] = pd.to_datetime(df["Published At"], errors='coerce')

# Replace nulls in numeric columns
for col in ["Views", "Likes", "Comments"]:
    df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0).astype(int)

# Assign Category based on Keyword
def assign_category(keyword):
    keyword = str(keyword).lower()
    if "tech" in keyword or "gadget" in keyword:
        return "Technology"
    elif "music" in keyword or "song" in keyword:
        return "Entertainment"
    elif "news" in keyword or "update" in keyword:
        return "News"
    elif "game" in keyword:
        return "Gaming"
    elif "vlog" in keyword or "lifestyle" in keyword:
        return "Lifestyle"
    elif "education" in keyword or "tutorial" in keyword:
        return "Education"
    else:
        return "Other"

df["Category"] = df["Keyword"].apply(assign_category)

# Add Sentiment column
def get_sentiment(title):
    polarity = TextBlob(str(title)).sentiment.polarity
    if polarity > 0.1:
        return "Positive"
    elif polarity < -0.1:
        return "Negative"
    else:
        return "Neutral"

df["Sentiment"] = df["Title"].apply(get_sentiment)

# Save to new CSV
df.to_csv("processed_videos_stats.csv", index=False)
print("✅ File saved as 'processed_videos_stats.csv'")
