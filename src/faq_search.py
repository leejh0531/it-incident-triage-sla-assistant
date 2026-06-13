from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def search_related_faq(query: str, faq_df, top_k: int = 3):
    faq_df = faq_df.copy()
    faq_df["search_text"] = faq_df["question"].fillna("") + " " + faq_df["answer"].fillna("")

    documents = faq_df["search_text"].tolist()
    documents.append(query)

    vectorizer = TfidfVectorizer(stop_words="english")
    vectors = vectorizer.fit_transform(documents)

    query_vector = vectors[-1]
    faq_vectors = vectors[:-1]

    similarities = cosine_similarity(query_vector, faq_vectors).flatten()
    faq_df["similarity"] = similarities

    results = faq_df.sort_values("similarity", ascending=False).head(top_k)

    return results[["faq_id", "category", "question", "answer", "related_team", "similarity"]]