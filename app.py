import streamlit as st
from gensim.models import Word2Vec
import pickle
import nltk

# Download NLTK data
nltk.download('punkt')

# Load your pickled model
with open('word2vec_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Function to predict the most similar words
def get_most_similar(word, topn=5):
    try:
        return model.wv.most_similar(word, topn=topn)
    except KeyError:
        return "Word not in vocabulary!"

# Function to find the word that doesn't match
def get_doesnt_match(words):
    try:
        return model.wv.doesnt_match(words)
    except KeyError:
        return "One or more words not in vocabulary!"

# Function to calculate similarity between two words
def get_similarity(word1, word2):
    try:
        return model.wv.similarity(word1, word2)
    except KeyError:
        return "One or both words not in vocabulary!"

# Streamlit app design
def main():
    st.title("Game of Thrones Themed Word Predictor")
    st.write("© Lavish Gangwani")

    # Setting the background image
    page_bg_img = '''
    <style>
    body {
        background-image: url('https://hdqwalls.com/wallpapers/winter-is-coming.jpg');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        margin: 0;
        height: 100vh;
    }
    .stApp {
        background: rgba(0, 0, 0, 0.7); /* Semi-transparent background for the app */
        border-radius: 10px; /* Optional: add rounded corners */
        padding: 2rem; /* Optional: add padding */
        color: white; /* Text color for contrast */
    }
    h1, h2, h3, h4, h5, h6 {
        color: white; /* Ensure headers are white */
    }
    .css-1v3fvcr {
        color: white; /* Ensure sidebar text color is white */
    }
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)

    st.header("Word Prediction with Gensim")

    # Sidebar for user input
    st.sidebar.title("Choose Your Prediction")
    option = st.sidebar.selectbox("Select an option:", ["Most Similar", "Doesn't Match", "Word Similarity"])

    if option == "Most Similar":
        word = st.sidebar.text_input("Enter a word:")
        if st.sidebar.button("Predict"):
            result = get_most_similar(word)
            st.write("Most similar words to ", word, ":")
            if isinstance(result, str):
                st.write(result)
            else:
                for res in result:
                    st.write(f"{res[0]}: {res[1]:.4f}")

    elif option == "Doesn't Match":
        words = st.sidebar.text_area("Enter words separated by commas:").split(',')
        words = [word.strip() for word in words]
        if st.sidebar.button("Find"):
            result = get_doesnt_match(words)
            st.write("The word that doesn't match is:", result)

    elif option == "Word Similarity":
        word1 = st.sidebar.text_input("Enter the first word:")
        word2 = st.sidebar.text_input("Enter the second word:")
        if st.sidebar.button("Calculate"):
            result = get_similarity(word1, word2)
            if isinstance(result, str):
                st.write(result)
            else:
                st.write(f"Similarity between {word1} and {word2}: {result:.4f}")

if __name__ == "__main__":
    main()
