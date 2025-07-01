# 🌿 Plant Assistant

**Plant Assistant** is a local AI-powered plant query system that helps you ask natural-language questions about Indian-origin plants using a combination of textual plant data and vector similarity search. It follows the **Model-Control-View (MCV)** architecture.

---

## 📐 MCV Architecture

### 🧠 Model (`text_indexing.py`, `Indian_plants_English.json`)
- Holds the core **plant knowledge** in text format.
- Embeds each plant's data using **HuggingFace sentence-transformers**.
- Stores indexed embeddings into a local **Chroma vector store**.

### 🕹️ Control (`main.py`)
- Acts as the controller that:
  - Receives user queries.
  - Loads the vector DB.
  - Performs similarity search.
  - Formats and returns relevant results.

### 🖥️ View (Terminal/CLI)
- Command-line interface for:
  - Uploading user questions.
  - Viewing AI-generated plant answers.

---

## 🚀 Features

- ✅ Local-first: No internet needed after setup
- 🌱 Indian origin plant focus
- 💬 Natural language querying
- 📦 Lightweight architecture (LangChain + ChromaDB + HuggingFace)

---

## 📁 Folder Structure

Flower_Plants/
│
├── main.py # Controller (CLI interface)
│
├── Modules/
│ ├── text_indexing.py # Model: Embeds & stores plant data
│
├── Data/
│ ├── Indian_plants_English.json # Plant dataset
│
├── DB/
│ ├── text_chroma/ # Chroma vector store
│
└── README.md # Documentation
