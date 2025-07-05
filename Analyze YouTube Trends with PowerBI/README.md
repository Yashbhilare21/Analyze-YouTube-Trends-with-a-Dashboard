# 📊 YouTube Trends Analyzer

A complete data analysis and business intelligence project that explores YouTube video trends using **Python for data cleaning and enrichment**, and **Power BI for dynamic dashboard visualization**.

---

## 📁 Dataset Used

**`processed_videos_stats.csv`**  
Source: Cleaned and transformed using Python from the original `videos-stats.csv`.

### 🔍 Key Fields:
- `Title` – Video title  
- `Video ID` – Unique YouTube video ID  
- `Published At` – Date video was published  
- `Keyword` – Topic/category keyword  
- `Likes`, `Comments`, `Views` – Engagement metrics  
- `Category` – Mapped from keyword using custom logic  
- `Sentiment` – Derived using text sentiment analysis on video titles

---

## 🧹 Data Cleaning & Feature Engineering (Python)

Python was used for preprocessing using **Pandas** and **TextBlob**:

- ✅ Handled nulls and data types
- ✅ Converted `Published At` to datetime
- ✅ Categorized videos into:
  - Technology, Entertainment, News, Gaming, Lifestyle, Education, etc.
- ✅ Analyzed sentiment of video titles (`Positive`, `Neutral`, `Negative`)
- ✅ Final cleaned file exported as: `processed_videos_stats.csv`

### 📌 Sample Python Workflow

```python
# Sentiment analysis on titles
from textblob import TextBlob

def get_sentiment(title):
    polarity = TextBlob(str(title)).sentiment.polarity
    if polarity > 0.1:
        return "Positive"
    elif polarity < -0.1:
        return "Negative"
    else:
        return "Neutral"

df["Sentiment"] = df["Title"].apply(get_sentiment)
```

---

## 📊 Power BI Dashboard Features

A powerful and interactive Power BI dashboard was built on the cleaned dataset, including:

### ✅ KPI Metrics
- 🎥 Total Videos
- 👁️ Total Views
- ❤️ Total Likes
- 💬 Total Comments

### ✅ Visualizations
- 📈 **Top 10 Videos** by Views, Likes, and Comments
- 📅 **Daily Trends** of Views, Likes, and Comments over time
- 🗂️ **Category-wise View Analysis**
- 😊 **Sentiment Distribution** (Positive, Neutral, Negative)
- 📊 **Category-wise Trends by Year**
- 📤 Keyword and Sentiment Filters for dynamic exploration

> Designed for executives, analysts, and marketers to understand what drives success on YouTube.

---

## 🚀 Technologies Used

- 🐍 **Python**: pandas, textblob (for NLP sentiment analysis)
- 📊 **Power BI**: dynamic filtering, KPI cards, interactive visuals

---

## 📄 Project Highlights

- Mapped keywords into logical categories
- Performed NLP sentiment classification on video titles
- Created multi-dimensional analysis visuals in Power BI
- Delivered clean, documented insights in a presentable PDF/dashboard

---

## 📁 Files Included

| File | Description |
|------|-------------|
| `videos-stats.csv` | Original raw dataset |
| `processed_videos_stats.csv` | Cleaned and enriched version |
| `Youtube Trend Analysis.pbix` | Dashboard PowerBI |
| `Youtube Trend Analysis.pdf` | Dashboard PDF snapshot |
| `README.md` | This file |

---

## 🙋‍♂️ Author

**Yash Bhilare**  
📧 yashbhilare209@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/yash-bhilare/)

---

> 💡 Insight meets action: uncover what makes YouTube videos trend — and why.