def hybrid_score(dense_score: float, keyword_score: float, dense_weight=0.6):
    keyword_weight = 1 - dense_weight
    return dense_weight * dense_score + keyword_weight * keyword_score

if __name__ == "__main__":
    print(hybrid_score(0.80, 0.95))
