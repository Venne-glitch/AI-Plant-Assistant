# main.py

from langchain_community.vectorstores import Chroma
from langchain_huggingface.embeddings import HuggingFaceEmbeddings

CHROMA_DIR = "DB/text_chroma"
embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
db = Chroma(persist_directory=CHROMA_DIR, embedding_function=embedding)

print("🌿 Welcome to Plant Assistant!")

while True:
    query = input("Ask about a plant (or type 'exit'): ")
    if query.lower() == 'exit':
        break

    docs = db.similarity_search(query, k=3)
    seen = set()
    print("\n🔎 Answer:\n")
    if not docs:
        print("❌ No plant found related to your query.")
    else:
        for doc in docs:
            content = doc.page_content.strip()
            if content not in seen:
                print(content)
                print("-" * 60)
                seen.add(content)
