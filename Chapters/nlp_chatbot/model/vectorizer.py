from sklearn.feature_extraction.text import TfidfVectorizer  # text -> numbers

def build_vectorizer(questions):
    vectorizer = TfidfVectorizer()   # Creates a TF-IDF model without training yet
    vectors = vectorizer.fit_transform(questions)
    #  fit -> Learns vocabulary from questions; Compute IDF values; ['return', 'policy', 'track', 'order', 'refund']
    #  transform -> Converts each sentence into numeric vector. Output is matrix ; 
    # Sentence	return	policy	track	order	refund
    # Q1	0.71	0.71	0	0	0
    # Q2	0	0	0.71	0.71	0
    # Q3	0	0	0	0	1
    print(f"Vectorizer: {vectorizer}")
    print(f"Vectors: {vectors}")
    return vectorizer, vectors

    # vectorizer is a trained language understanding machine.
