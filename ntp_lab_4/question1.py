import nltk
import re
from nltk.corpus import brown
from collections import Counter

nltk.download("brown")
nltk.download("punkt")

sentences = brown.sents(categories="news")

text = " ".join([" ".join(sent) for sent in sentences])

text = text.lower()

text = re.sub(r"[^\w\s]", "", text)

sent_tokens = nltk.sent_tokenize(text)

word_tokens = nltk.word_tokenize(text)

vocab = set(word_tokens)

print("Total sentences:", len(sent_tokens))
print("Total words:", len(word_tokens))
print("Vocabulary size:", len(vocab))