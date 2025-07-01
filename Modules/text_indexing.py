# Modules/text_indexing.py
import os
import json
from langchain_community.vectorstores import Chroma
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from langchain_core.documents import Document

CHROMA_DIR = "DB/text_chroma"
JSON_PATH = "Data/Indian_plants_English.json"

def index_textual_plants(json_path):
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    documents = []
    for plant in data:
        content = f"""\ 
Name: {plant.get("name", "")}
Origin/Region: {plant.get("origin_region", "")}
Best Season to Grow: {plant.get("best_season_to_grow", "")}
Toxicity: {plant.get("toxicity", "")}
Growing & nurturing Instructions: {plant.get("growing_nuturing_instructions", "")}
"""
        documents.append(Document(
            page_content=content.strip(),
            metadata={"name": plant.get("name", "").lower()}
        ))

    embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    db = Chroma.from_documents(documents=documents, embedding=embedding, persist_directory=CHROMA_DIR)
    print("✅ Text-only data indexed successfully.")

if __name__ == "__main__":
    index_textual_plants(JSON_PATH)
