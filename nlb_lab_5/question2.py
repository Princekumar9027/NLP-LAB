import pandas as pd
import re
from collections import defaultdict
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

import nltk
nltk.download('punkt')
nltk.download('stopwords')

data = {
    "Email Text": [
        "Win money now",
        "Lowest price guaranteed",
        "Cheap meds available",
        "Hello friend how are you",
        "Let’s have lunch tomorrow",
        "Meeting schedule attached",
        "Win a free lottery ticket",
        "See you at the conference",
        "Project deadline reminder",
        "Cheap loans available"
    ],
    "Label": ["Spam","Spam","Spam","Ham","Ham","Ham","Spam","Ham","Ham","Spam"]
}
df = pd.DataFrame(data)

def preprocess(text):
    text = text.lower()
    tokens = word_tokenize(text)
    tokens = [w for w in tokens if w.isalpha()]
    tokens = [w for w in tokens if w not in stopwords.words("english")]
    return tokens

df["tokens"] = df["Email Text"].apply(preprocess)

spam_words = defaultdict(int)
ham_words = defaultdict(int)
spam_count = ham_count = 0

for tokens, label in zip(df["tokens"], df["Label"]):
    if label == "Spam":
        spam_count += 1
        for w in tokens: spam_words[w] += 1
    else:
        ham_count += 1
        for w in tokens: ham_words[w] += 1

vocab = set(list(spam_words.keys()) + list(ham_words.keys()))

def predict(email):
    tokens = preprocess(email)
    p_spam = spam_count / len(df)
    p_ham = ham_count / len(df)

    spam_prob = p_spam
    ham_prob = p_ham

    for w in tokens:
        spam_prob *= (spam_words[w] + 1) / (sum(spam_words.values()) + len(vocab))
        ham_prob *= (ham_words[w] + 1) / (sum(ham_words.values()) + len(vocab))
    
    return "Spam" if spam_prob > ham_prob else "Ham"

df["predicted"] = df["Email Text"].apply(predict)
accuracy = (df["Label"] == df["predicted"]).mean()
print("Accuracy from scratch:", accuracy)