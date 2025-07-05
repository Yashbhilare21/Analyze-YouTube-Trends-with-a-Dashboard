# 📊 YouTube Trends Analysis Project With A Dashboard

Welcome to the YouTube Trends Analysis repository! This project explores patterns in YouTube video performance using two powerful approaches:

- 📌 **Power BI Dashboard** for executive-level reporting
- 🌐 **Streamlit Web App** for interactive, browser-based insights

Created using **Python for data preprocessing** and **TextBlob for sentiment analysis**, the dataset is enriched and visualized through dynamic dashboards.

---

## 🧠 Objective

To analyze YouTube video trends using engagement metrics (likes, comments, views), categorize content by themes (Technology, Gaming, etc.), and apply NLP sentiment analysis to video titles — helping creators and marketers understand what makes content trend.

---

## 🗂️ Repository Structure

| Folder | Description |
|--------|-------------|
| [`PowerBI-Version`](./PowerBI-Version) | Cleaned dataset + Power BI dashboard for interactive insights |
| [`Streamlit-Version`](./Streamlit-Version) | Interactive Streamlit app using Plotly, TextBlob, and Pandas |

---

## 🚀 Project Features

### ✅ Common Across Both Versions
- Sentiment analysis of video titles using **TextBlob**
- Auto-categorization of videos by **keywords**
- Analysis based on views, likes, comments, and publishing date

---

### 📊 Power BI Version
> 📂 [`PowerBI-Version`](./PowerBI-Version)

- KPI Cards: 🎥 Total Videos, ❤️ Likes, 👁️ Views, 💬 Comments
- Trend visuals: Top 10 videos by views/likes/comments
- Category-wise analysis
- Sentiment distribution
- Keyword filters and drill-downs

**Technologies:** Python, Pandas, TextBlob, Power BI  
**Output:** `.pbix` file + PDF snapshot

---

### 🌐 Streamlit Web App
> 📂 [`Streamlit-Version`](./Streamlit-Version)

- Interactive dashboard hosted via **Streamlit**
- Visualizations using **Plotly**
- Real-time filters by keyword
- Sentiment pie chart + category-wise trends

**Technologies:** Python, Streamlit, Pandas, Plotly, TextBlob  
**Run Locally:**

```bash
cd Streamlit-Version
pip install -r requirements.txt
streamlit run app.py
```

## 📁 Dataset Details

| Column        | Description                              |
|---------------|------------------------------------------|
| `Title`       | Title of the video                       |
| `Video ID`    | Unique YouTube identifier                |
| `Published At`| Upload date                              |
| `Keyword`     | Main topic or tag                        |
| `Likes`       | Total likes                              |
| `Comments`    | Total comments                           |
| `Views`       | Total views                              |
| `Category`    | Inferred category (Tech, News, etc.)     |
| `Sentiment`   | Positive / Neutral / Negative            |

---

## 🧠 Future Enhancements

- 🔗 Integrate with **YouTube Data API** for live data  
- ☁️ Deploy Streamlit app to **Streamlit Cloud**  
- 📤 Export options for filtered data  
- 📱 Responsive layout for mobile access  

---

## 🙋‍♂️ Author

**Yash Bhilare**  
📧 yashbhilare209@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/yash-bhilare/)
