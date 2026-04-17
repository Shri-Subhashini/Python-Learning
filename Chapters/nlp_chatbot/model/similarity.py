from sklearn.metrics.pairwise import cosine_similarity   # measure how similar two vectors are; 0 -> no similarity; 1 -> identical meaning

def find_best_match(user_vector, faq_vectors):

    # Computes cosine similarity between:
    # 1 user vector
    # Every FAQ vector
    scores = cosine_similarity(user_vector, faq_vectors)   # Compares user query vector with every FAQ vector. Produces similarity scores ; scores = [[0.82, 0.12, 0.05]]
    best_index = scores.argmax()    # Returns index of highest similarity value. Eg: scores = [[0.82, 0.12, 0.05]]; beat_index = 0
    best_score = scores[0][best_index]   # scores[0][0] → 0.82
    return best_index, best_score

# best_index - Which FAQ question matched best
# best_score - How confident the match is