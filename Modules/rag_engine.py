import os
import json
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.docstore.document import Document

CHROMA_DIR = "DB/chroma"

json_path = "Data/Indian_plant_English.json"

def format_floral_entry(entry):
    return json.dumps({
        "type": entry.get("type", "")
        "name": entry.get("name", ""),
        "origin_region": entry.get("origin_region", ""),
        "best_season_to_grow": entry.get("best_season_to_grow", ""),
        "toxicity": entry.get("toxicity", ""),
        "growing_nurturing_instructions": entry.get("growing_nurturing_instructions", "")
    }, indent=2)

def load_and_index_floral_data(json_path):
    with open(json_path, "r", encoding="utf-8") as file:
        plant_data = json.load(file)

    documents = []
    for entry in plant_data:
        content = format_floral_entry(entry)
        documents.append(Document(page_content=content))

    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    db = Chroma.from_documents(documents, embedding=embeddings, persist_directory=CHROMA_DIR)
    db.persist()
    print("✅ Floral data indexed successfully.")


# Retrieve relevant plant data
def retrieve_context(query: str, top_k=3) -> str:
    embeddings = HuggingFaceEmbeddings(model_name='all-MiniLM-L6-v2')
    db = Chroma(persist_directory=CHROMA_DIR, embedding_function=embeddings)
    results = db.similarity_search(query, k=top_k)
    return "\n\n".join([doc.page_content for doc in results])

if __name__ == "__main__":
    print("Indexing your data...")
    load_and_index_floral_data(json_path)
    print("Indexing complete!")

    query = "What are the best seasons to grow Tulsi?"
    result = retrieve_context(query)
    print("Result:\n", result)

