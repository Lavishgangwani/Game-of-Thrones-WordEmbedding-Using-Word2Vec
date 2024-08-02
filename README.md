---

# Game of Thrones Word Embedding Using Word2Vec

Welcome to the **Game of Thrones Word Embedding Using Word2Vec** project! This repository contains a Streamlit web application that uses a Word2Vec model to perform various natural language processing (NLP) tasks on text data related to Game of Thrones. 

## Project Overview

The goal of this project is to build and deploy a Word2Vec model to analyze and understand text data by performing tasks such as:
- Finding the most similar words to a given input word.
- Identifying words that do not match within a given set.
- Calculating the similarity between two words.

The model is trained on text data related to Game of Thrones to generate meaningful word embeddings that capture semantic relationships between words.

## Live Demo

You can try out the application live here: [Game of Thrones Word2Vec App](https://game-of-thrones-word2vec-lavishgw22.streamlit.app/)

## Features

- **Most Similar Words**: Enter a word and get a list of words that are most similar to it based on the trained Word2Vec model.
- **Doesn't Match**: Input a list of words to find the word that doesn’t fit well with the others.
- **Word Similarity**: Calculate and display the similarity score between two words.

## Installation

To set up this project locally, follow these steps:

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/Lavishgangwani/Game-of-Thrones-WordEmbedding-Using-Word2Vec.git
   cd Game-of-Thrones-WordEmbedding-Using-Word2Vec
   ```

2. **Install Required Packages:**

   You need to have Python installed. Then, install the required packages using pip:

   ```bash
   pip install -r requirements.txt
   ```

   If you do not have a `requirements.txt` file, you can manually install the necessary packages:

   ```bash
   pip install streamlit gensim nltk
   ```

3. **Run the Streamlit App:**

   Start the Streamlit server with:

   ```bash
   streamlit run app.py
   ```

   This will open the application in your web browser.

## Usage

Once the application is running, you can interact with it through the sidebar options:

- **Most Similar Words**: Enter a word to find its most similar words.
- **Doesn't Match**: Input a list of words to find the one that does not fit.
- **Word Similarity**: Enter two words to calculate their similarity.

## Model Details

The Word2Vec model used in this project was trained with the following parameters:
- **Window Size**: 10
- **Minimum Count**: 2
- **Epochs**: 10

This model is designed to capture semantic relationships between words based on the Game of Thrones text corpus.

## Contributing

If you would like to contribute to this project, please fork the repository, make your changes, and submit a pull request.

## Contact

For any questions or inquiries, feel free to reach out via email at [lavishgangwani22@gmail.com](mailto:lavishgangwani22@gmail.com).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---