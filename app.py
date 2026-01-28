import streamlit as st

st.title("📄 Token Estimator App")

st.write("Upload a text file to estimate word count and tokens.")

# Function to estimate tokens
def estimate_tokens(char_count):
    return char_count // 4 # returns an integer value modue dividing by 4

# File uploader responsible for uploading text files
uploaded_file = st.file_uploader("Upload a text file", type=["txt"])

if uploaded_file is not None:
    # Read file content which is uploaded by decoding it to utf-8
    content = uploaded_file.read().decode("utf-8")

    # Character count
    char_count = len(content)

    # Word count
    word_count = len(content.split())

    # Token estimation
    token_count = estimate_tokens(char_count)

    # Display results
    st.subheader("📊 File Analysis")
    st.write("Word Count:", word_count)
    st.write("Character Count:", char_count)
    st.write("Estimated Tokens:", token_count)

    # Warning for large files which have more than 4000 characters
    if char_count > 4000:
        st.warning("⚠️ Warning: File contains more than 4000 characters!")
