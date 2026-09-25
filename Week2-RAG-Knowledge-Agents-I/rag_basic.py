from pathlib import Path

def load_documents():
    root = Path(__file__).parents[1] / "rag" / "knowledge"
    return list(root.rglob("*.md"))

if __name__ == "__main__":
    docs = load_documents()
    print("Knowledge documents:")
    for doc in docs:
        print("-", doc)
