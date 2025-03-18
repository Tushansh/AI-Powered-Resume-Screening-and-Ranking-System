import streamlit as st
from PyPDF2 import PdfReader
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Function to extract text from PDF
def extract_text_from_pdf(file):
    pdf = PdfReader(file)
    text = ""
    for page in pdf.pages:
        extracted_text = page.extract_text()
        if extracted_text:
            text += extracted_text + " "
    return text.strip()

# Function to rank resumes based on job description
def rank_resumes(job_description, resumes):
    # Combine job description with resumes
    documents = [job_description] + resumes  # Fixed missing assignment
    vectorizer = TfidfVectorizer().fit_transform(documents)
    vectors = vectorizer.toarray()

    # Calculate cosine similarity
    job_description_vector = vectors[0]
    resume_vectors = vectors[1:]
    cosine_similarities = cosine_similarity([job_description_vector], resume_vectors).flatten()

    return cosine_similarities

# Streamlit app
st.title("AI Resume Screening & Candidate Ranking")

st.write("Upload resumes (PDF format) and provide a job description to rank candidates based on relevance.")

# Upload job description
job_description = st.text_area("Enter the Job Description")

# Upload multiple resumes
uploaded_files = st.file_uploader("Upload Resumes (PDF)", accept_multiple_files=True, type=["pdf"])

if st.button("Rank Resumes") and job_description and uploaded_files:
    resume_texts = [extract_text_from_pdf(file) for file in uploaded_files]

    # Rank resumes
    scores = rank_resumes(job_description, resume_texts)

    # Display results
    results = pd.DataFrame({
        "Candidate": [file.name for file in uploaded_files],
        "Relevance Score": scores
    }).sort_values(by="Relevance Score", ascending=False)

    st.write("### Ranked Resumes")
    st.dataframe(results)