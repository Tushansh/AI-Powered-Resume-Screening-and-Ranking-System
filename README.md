
# 🧠 AI-Powered Resume Screener & Ranker

An intelligent resume screening and applicant evaluation web app built with **Machine Learning**, **Natural Language Processing (NLP)**, and **Streamlit**. It automatically analyzes resumes (PDF/DOCX), predicts the applicant's job category, extracts relevant skills, and provides actionable feedback to streamline the hiring process for recruiters and HR professionals.

---

## 📌 Features

- 📂 **Upload Resumes** (.pdf, .docx)
- 🧠 **ML-Based Category Prediction**
- 🔍 **Skill Extraction from Resume Text**
- 📊 **Interactive Resume Analysis Dashboard**
- ✅ **Clean & Modern Streamlit UI**
- 🧪 **TF-IDF & Logistic Regression Based Classifier**
- 📥 **Multiple File Support (coming soon)**

---

## 🚀 Demo

Deploy the app instantly with **Streamlit Cloud**:  
[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/your-streamlit-link)

---

## 📸 Screenshots

| Home Page | Result Panel |
|-----------|--------------|
| ![Home](screenshots/home.png) | ![Result](screenshots/result.png) |

---

## 🏗️ Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io/)
- **NLP**: `nltk`, `spacy`
- **ML Model**: `scikit-learn` (TF-IDF + Logistic Regression)
- **Backend**: Python 3
- **Document Parsing**: `PyPDF2`, `python-docx`

---

## 🧰 Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/ai-resume-screener.git
cd ai-resume-screener
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Download necessary NLTK data:

```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
```

Run the app:

```bash
streamlit run app.py
```

---

## 📁 Project Structure

```
├── app.py               # Streamlit app
├── clf.pkl              # Trained ML classifier
├── tfidf.pkl            # TF-IDF Vectorizer
├── encoder.pkl          # Label encoder
├── requirements.txt     # Required Python packages
├── README.md
└── screenshots/         # UI screenshots (optional)
```

---

## 📝 Future Enhancements

- ✅ Resume Score & Quality Meter
- ✅ Grammar Feedback
- ✅ Job Description Matching (Cosine Similarity)
- ✅ Batch Resume Processing (ZIP upload)
- ✅ Downloadable Analysis Reports (PDF)

---

## 🤝 Contributing

Contributions are welcome! Please fork the repo and submit a pull request. For major changes, open an issue first to discuss.

---

## 📄 License

MIT License

---

## 👤 Author

**[Your Name]**  
🔗 [LinkedIn](https://linkedin.com/in/yourprofile) • [GitHub](https://github.com/yourusername)
