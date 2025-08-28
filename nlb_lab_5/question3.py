import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

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

X = df["Email Text"]
y = df["Label"]

vectorizer = CountVectorizer(stop_words="english")
X_vec = vectorizer.fit_transform(X)

model = MultinomialNB()
model.fit(X_vec, y)

y_pred = model.predict(X_vec)
print("Accuracy with sklearn:", accuracy_score(y, y_pred))