def metadata_filter(documents, **filters):
    result = []
    for doc in documents:
        metadata = doc.get("metadata", {})
        if all(metadata.get(k) == v for k, v in filters.items()):
            result.append(doc)
    return result

def retrieval_quality(retrieved_ids, relevant_ids):
    retrieved = set(retrieved_ids)
    relevant = set(relevant_ids)
    precision = len(retrieved & relevant) / len(retrieved) if retrieved else 0
    recall = len(retrieved & relevant) / len(relevant) if relevant else 0
    return {"precision": precision, "recall": recall}
