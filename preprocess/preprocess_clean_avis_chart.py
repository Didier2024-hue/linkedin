#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
- Nettoyage du texte
- Génération d’un nuage de mots (Wordcloud)
- Détection automatique de thèmes avec LDA
- Analyse simple de sentiments avec TextBlob
"""

import os
import re
import string
import warnings
import pandas as pd
import matplotlib
matplotlib.use("Agg")  
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from gensim import corpora, models
from textblob import TextBlob
import nltk
import spacy

# --------📁 Configuration des dossiers--------
BASE_DIR = "/home/datascientest/cde"
DATA_DIR = os.path.join(BASE_DIR, "data", "processed")
RESOURCES_DIR = os.path.join(DATA_DIR, "resources")
NLTK_DIR = os.path.join(RESOURCES_DIR, "nltk_data")

os.makedirs(NLTK_DIR, exist_ok=True)
os.environ["NLTK_DATA"] = NLTK_DIR
nltk.data.path.append(NLTK_DIR)
nltk.download("stopwords", download_dir=NLTK_DIR, quiet=True)

# --------🧠 Chargement de Spacy + stopwords--------
nlp = spacy.load("fr_core_news_sm")
stopwords_fr = set(nltk.corpus.stopwords.words("french"))
stopwords_en = set(nltk.corpus.stopwords.words("english"))
custom_stopwords = {
    'être', 'avoir', 'faire', 'aller', 'venir', 'très', 
    'je', 'tu', 'il', 'elle', 'on', 'nous', 'vous', 'ils', 'elles',
    'ce', 'cet', 'cette', 'ces', 'tout', 'tous', 'toute', 'toutes',
    'comme', 'alors', 'alor', 'alorsque', 'du', 'du coup', 'donc', 
    'car', 'parce', 'parce que', 'puis', 'ensuite', 'après',
    'chronopost', 'temu', 'tesla', 'vinted',
    'un', 'une', 'des', 'le', 'la', 'les', 'au', 'aux', 'de', 'du', 'd\'',
    'mon', 'ton', 'son', 'ma', 'ta', 'sa', 'mes', 'tes', 'ses',
    'leur', 'leurs', 'notre', 'votre', 'nos', 'vos',
    'en', 'y', 'avec', 'sans', 'plus','sur', 'sous', 'dans', 'chez', 'etc'
}
all_stopwords = stopwords_fr.union(stopwords_en).union(custom_stopwords)

# --------🧹 Fonction de nettoyage et lemmatisation--------
def preprocess_text(text):
    if not isinstance(text, str):
        return ""
    text = text.lower()
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"\d+", "", text)
    text = re.sub(r"\b\w{1,2}\b", "", text)  # supprime mots très courts
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = re.sub(r"\s+", " ", text).strip()

    doc = nlp(text)
    lemmas = [
        token.lemma_.lower() for token in doc
        if token.lemma_.lower() not in all_stopwords and
        len(token.lemma_) > 2 and
        not token.is_punct and
        not token.is_space
    ]
    return " ".join(lemmas)

# --------🌥️ Génération du wordcloud--------
def generate_wordcloud(text, output_path):
    wc = WordCloud(width=1000, height=500, background_color="white").generate(text)
    plt.figure(figsize=(14, 7))
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.title("Nuage de mots – Avis clients", fontsize=16)
    plt.savefig(output_path, bbox_inches="tight")
    plt.close()
    print("✅ Wordcloud sauvegardé.")

# --------🧠 Détection de thèmes LDA--------
def lda_topic_modeling(texts, output_path, num_topics=5, num_words=6):
    tokenized = [text.split() for text in texts]
    dictionary = corpora.Dictionary(tokenized)
    corpus = [dictionary.doc2bow(tokens) for tokens in tokenized]
    lda = models.LdaModel(corpus, num_topics=num_topics, id2word=dictionary, passes=15, random_state=42)

    plt.figure(figsize=(12, num_topics * 1.5))
    plt.axis("off")
    plt.title("Thèmes détectés (LDA)", fontsize=14)

    lines = []
    for i, topic in lda.show_topics(num_topics=num_topics, num_words=num_words, formatted=False):
        mots = ", ".join([mot for mot, _ in topic])
        lines.append(f"Thème {i + 1} : {mots}")

    plt.text(0, 1, "\n\n".join(lines), fontsize=12, va="top", family="monospace")
    plt.savefig(output_path, bbox_inches="tight")
    plt.close()
    print("✅ Thèmes LDA sauvegardés.")

# --------📊 Histogramme de sentiment--------
def sentiment_analysis(texts, output_path):
    sentiments = [TextBlob(t).sentiment.polarity for t in texts]
    plt.figure(figsize=(10, 5))
    plt.hist(sentiments, bins=20, edgecolor="black")
    plt.title("Distribution des sentiments", fontsize=14)
    plt.xlabel("Score de sentiment (de -1 à +1)")
    plt.ylabel("Nombre d’avis")
    plt.grid(True)
    plt.savefig(output_path, bbox_inches="tight")
    plt.close()
    print("✅ Histogramme des sentiments sauvegardé.")

# --------🚀 Exécution principale--------
def main():
    input_file = os.path.join(DATA_DIR, "preprocessed_clean_avis_avec_sentiments.csv")
    df = pd.read_csv(input_file)

    print("📥 Chargement des avis...")
    df["commentaire_preprocessed"] = df["commentaire"].apply(preprocess_text)

    print("🔄 Génération des visualisations...")
    all_text = " ".join(df["commentaire_preprocessed"].dropna().tolist())
    generate_wordcloud(all_text, os.path.join(DATA_DIR, "wordcloud.png"))
    lda_topic_modeling(df["commentaire_preprocessed"].dropna().tolist(), os.path.join(DATA_DIR, "lda_topics.png"))
    sentiment_analysis(df["commentaire_preprocessed"].dropna().tolist(), os.path.join(DATA_DIR, "sentiment_hist.png"))

    print("🎉 Terminé ! Visualisations prêtes.")

if __name__ == "__main__":
    main()
