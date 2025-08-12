import nltk
from nltk.corpus import brown
from nltk.tokenize import word_tokenize

nltk.download('brown')
nltk.download('punkt')
nltk.download('punkt_tab')

category = 'news'
words_in_category = brown.words(categories=category)

text_str = ' '.join(words_in_category)

tokens = word_tokenize(text_str)

print(f"Category Selected: {category}")
print("First 20 Tokens:", tokens[:20])
print(f"Total Tokens: {len(tokens)}")