import re
import nltk
from nltk.corpus import stopwords   # Common words like is, the, and that add little meaning.
from nltk.stem import WordNetLemmatizer    # Converts words to their base/root form. Eg: running - run

nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("stopwords")
nltk.download("wordnet")

# This files return clean txt

stop_words = set(stopwords.words("english"))    # "What is your return policy?"   -> what is your
print(stop_words)
lemmatizer = WordNetLemmatizer()

def clean_text(text:str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z\s]" ,"", text)
    tokens = nltk.word_tokenize(text)    # "return policy available"
                                       # → ["return", "policy", "available"]
    
    # "customers are returning items"
    # → ["customer", "return", "item"]

    tokens = [
        lemmatizer.lemmatize(word)
        for word in tokens
        if word not in stop_words
    ]

    return " ".join(tokens)   #TF-IDF expects string input, not lists.
    # ["customer", "return", "item"]   -> customer return item