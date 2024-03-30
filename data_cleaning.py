import spacy
from nltk.corpus import stopwords

nlp = spacy.load('en_core_web_sm')
stop_words = set(stopwords.words('english'))


def words_lemm_fast(text):
    doc = nlp(text)
    tokens = [token.text.lower() for token in doc]
    filtered_tokens = [token for token in tokens if token not in stop_words]
    lemmatized_tokens = [token.lemma_ for token in doc if token.text.lower() in filtered_tokens]
    lemmatized_text = ' '.join(lemmatized_tokens)
    return lemmatized_text

import pandas as pd
x=pd.read_csv("Emotion_classify_data.csv")
x['Comment']=x['Comment'].apply(lambda y: words_lemm_fast(y))
x.to_csv('cleaned.csv')