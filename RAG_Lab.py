import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.title("📄 Lab 2A: Simple RAG using Cosine Similarity")

st.write("Upload multiple text documents and enter a query to find the most relevant document.")

# Step 1: Upload multiple documents
uploaded_files = st.file_uploader(
    "Upload text documents",
    type=["txt", "md", "py"],
    accept_multiple_files=True
)

# Step 2: Ask user for query
query = st.text_input(
    "Enter your query",
    placeholder="Example: I want to find information on apples"
)

if uploaded_files and query:
    documents = []
    file_names = []

    # Read documents
    for file in uploaded_files:
        content = file.read().decode("utf-8")
        documents.append(content)
        file_names.append(file.name)

    # Step 3: Convert documents to TF-IDF vectors
    vectorizer = TfidfVectorizer()
    doc_vectors = vectorizer.fit_transform(documents)

    # Step 4: Convert query to vector
    query_vector = vectorizer.transform([query])

    # Step 5: Compute cosine similarity
    similarities = cosine_similarity(query_vector, doc_vectors)[0]

    # Find most relevant document
    best_match_index = similarities.argmax()
    best_match_file = file_names[best_match_index]
    best_match_score = similarities[best_match_index]

    # Display results
    st.subheader("🔍 Results")
    st.write("Most Relevant Document:", best_match_file)
    st.write("Cosine Similarity Score:", round(best_match_score, 4))

    # Optional: show all similarity scores
    st.subheader("📊 Similarity Scores")
    for name, score in zip(file_names, similarities):
        st.write(f"{name}: {round(score, 4)}")
