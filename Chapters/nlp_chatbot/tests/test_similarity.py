import numpy as np 
from model.similarity import find_best_match

def test_similarity():
    user_vector = np.array([[1,0]])
    faq_vectors = np.array([[1,0], [0,1]])
    index, score = find_best_match(user_vector, faq_vectors)
    assert index == 0
    assert score == 1.0

    