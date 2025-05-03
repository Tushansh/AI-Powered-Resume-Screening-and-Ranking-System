import streamlit as st
import pickle
import docx
import PyPDF2
import re
import time

# Load ML models
svc_model = pickle.load(open('clf.pkl', 'rb'))
tfidf = pickle.load(open('tfidf.pkl', 'rb'))
le = pickle.load(open('encoder.pkl', 'rb'))

# Clean text function
def cleanResume(txt):
    cleanText = re.sub('http\S+\s', ' ', txt)
    cleanText = re.sub('RT|cc', ' ', cleanText)
    cleanText = re.sub('#\S+\s', ' ', cleanText)
    cleanText = re.sub('@\S+', '  ', cleanText)
    cleanText = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), ' ', cleanText)
    cleanText = re.sub(r'[^\x00-\x7f]', ' ', cleanText)
    cleanText = re.sub('\s+', ' ', cleanText)
    return cleanText

def extract_text(file):
    ext = file.name.split('.')[-1].lower()
    if ext == 'pdf':
        reader = PyPDF2.PdfReader(file)
        return ' '.join([page.extract_text() or '' for page in reader.pages])
    elif ext == 'docx':
        doc = docx.Document(file)
        return '\n'.join([para.text for para in doc.paragraphs])
    elif ext == 'txt':
        try:
            return file.read().decode('utf-8')
        except:
            return file.read().decode('latin-1')
    else:
        raise ValueError("Unsupported file type")

def predict_category(resume_text):
    cleaned = cleanResume(resume_text)
    vectorized = tfidf.transform([cleaned]).toarray()
    pred = svc_model.predict(vectorized)
    return le.inverse_transform(pred)[0]

def get_category_style(category):
    mapping = {
        'Data Science': ('📊', '#FFD700'),
        'HR': ('🧑‍💼', '#00CED1'),
        'Advocate': ('⚖️', '#B22222'),
        'Arts': ('🎨', '#FF69B4'),
        'Web Designing': ('🌐', '#4B0082'),
        'Mechanical Engineer': ('🔧', '#708090'),
        'Sales': ('💼', '#FF4500'),
        'Health and fitness': ('💪', '#32CD32'),
        'Civil Engineer': ('🏗️', '#4682B4'),
        'Java Developer': ('☕', '#CD5C5C'),
        'Business Analyst': ('📈', '#20B2AA'),
        'Python Developer': ('🐍', '#4169E1'),
        'DevOps Engineer': ('⚙️', '#2E8B57'),
        'Network Security Engineer': ('🔐', '#6A5ACD'),
        'PMO': ('📋', '#DAA520'),
        'Database': ('🗃️', '#5F9EA0'),
        'Testing': ('🧪', '#A52A2A')
    }
    return mapping.get(category, ('🔎', '#87CEFA'))

# Streamlit App
def main():
    st.set_page_config(page_title="AI Resume Screener", page_icon="🧠", layout="wide")

    st.markdown("""
        <style>
        html, body, [class*="css"]  {
            font-family: 'Segoe UI', sans-serif;
            color: #222222;
            background-color: #f0f8ff;
        }
        .card {
            background-color: white;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        }
        .category-box {
            border-radius: 10px;
            padding: 15px;
            color: white;
            font-size: 20px;
            font-weight: 600;
            margin-top: 20px;
        }
        </style>
    """, unsafe_allow_html=True)

    st.sidebar.title("🧾 Resume Screener")
    st.sidebar.markdown("Leverage AI + NLP to instantly categorize resumes into job roles.")
    st.sidebar.info("Supported file types: PDF, DOCX, TXT")
    st.sidebar.caption("Created by Tushansh Bajaj ⚙️")

    st.title("🚀 AI-Powered Resume Screener")
    st.subheader("Upload a resume and instantly get the job category prediction")

    uploaded_file = st.file_uploader("📤 Upload your resume", type=["pdf", "docx", "txt"])

    if uploaded_file:
        if uploaded_file.size > 2 * 1024 * 1024:
            st.error("❌ File too large. Please upload under 2MB.")
            return

        try:
            resume_text = extract_text(uploaded_file)
            col1, col2 = st.columns([2, 1])

            with col1:
                if st.checkbox("📝 Show Extracted Text"):
                    st.text_area("Resume Text", resume_text, height=300)

            with col2:
                st.markdown("### 🎯 Prediction")
                if st.button("🔍 Analyze"):
                    with st.spinner("Processing resume..."):
                        time.sleep(1.5)
                        category = predict_category(resume_text)
                        emoji, color = get_category_style(category)

                        st.markdown(
                            f"<div class='category-box' style='background-color: {color};'>"
                            f"{emoji} Predicted Category: <strong>{category}</strong></div>",
                            unsafe_allow_html=True
                        )
                        st.success("Resume analyzed successfully! ✅")

        except Exception as e:
            st.error(f"⚠️ Error: {e}")

if __name__ == "__main__":
    main()
