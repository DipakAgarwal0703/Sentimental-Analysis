import spacy
import nltk
import re
from nltk.corpus import stopwords

# Load spaCy model
nlp = spacy.load('en_core_web_sm')
# Set of stop words
stop_words = set(stopwords.words('english'))

def text_pass(text):
    doc = nlp(text)
    
    # Tokenize, lowercase, remove punctuation, spaces, and special characters
    tokens = [token.text.lower() for token in doc if not token.is_punct and not token.is_space]
    
    # Filter out stop words
    filtered_tokens = [token for token in tokens if token not in stop_words]
    
    # Remove special characters from tokens
    cleaned_tokens = [re.sub(r'[^a-zA-Z0-9]', '', token) for token in filtered_tokens]
    
    # Remove any empty strings resulting from the previous step
    cleaned_tokens = [token for token in cleaned_tokens if token]
    
    # Lemmatize the cleaned tokens
    lemmatized_tokens = [token.lemma_ for token in doc if token.text.lower() in cleaned_tokens]
    lemmatized_text = ' '.join(lemmatized_tokens)
    
    return lemmatized_text

def words_lemm_fast(text_list):
    processed_texts = []
    for text in text_list:
        processed_texts.append(text_pass(text))
    return processed_texts
