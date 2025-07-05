# 📺 YouTube Trends Dashboard

[![Streamlit](https://img.shields.io/badge/Built%20With-Streamlit-orange?logo=streamlit)](https://streamlit.io/)
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)](https://www.python.org/)

An interactive and insightful dashboard built with **Streamlit** and **Python** to analyze YouTube video trends based on views, likes, comments, publishing dates, sentiment, and categories.


---

## 🔍 Features

✅ View top trending videos by:
- Views
- Likes
- Comments

✅ Visualizations:
- 📈 Daily trends (Views/Likes/Comments)
- 📊 Category-wise total views
- 🥧 Sentiment analysis on video titles

✅ Filter options:
- 🎯 Keyword-based filtering

✅ Built-in enhancements:
- Auto categorization of keywords
- Title sentiment analysis using TextBlob

---

## 🧰 Tech Stack

- **Python**
- **Streamlit**
- **Pandas**
- **Plotly**
- **TextBlob** (for sentiment analysis)

---

## 📁 Project Structure

```
youtube_dashboard/
├── app.py                  # Streamlit dashboard app
├── analysis.py             # Data loading, cleaning, and logic
├── requirements.txt        # All dependencies
├── README.md               # This file
└── data/
    └── videos-stats.csv    # Dataset used for analysis
```

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/youtube-trends-dashboard.git
cd youtube-trends-dashboard
```

### 2️⃣ Create and Activate a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
# OR
venv\Scripts\activate     # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Streamlit App

```bash
streamlit run app.py
```

Then open `http://localhost:8501` in your browser.

---

## 📊 Sample Dataset Fields

| Column        | Description                      |
|---------------|----------------------------------|
| `Title`       | Title of the YouTube video       |
| `Video ID`    | Unique identifier                |
| `Published At`| Date of publication              |
| `Keyword`     | Topic/Tag of the video           |
| `Likes`       | Number of likes                  |
| `Comments`    | Number of comments               |
| `Views`       | Number of views                  |

---

## 🧠 Future Improvements

- 🔎 YouTube API integration for live data
- 🌐 Deploy to Streamlit Cloud
- 🧾 Export filtered data
- 📱 Mobile-friendly layout

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!  

---

## 🙋‍♂️ Author

**Yash Bhilare**  
📧 yashbhilare209@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/yash-bhilare/)

---

> Made with ❤️ using Python and Streamlit