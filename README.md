# Smart Document Assistant using RAG + Endee

## 🚀 Problem Statement

Users often struggle to extract meaningful information from large documents such as PDFs, notes, or research papers. Traditional keyword-based search is inefficient and does not provide context-aware answers.

---

## 💡 Solution

This project implements a **Retrieval-Augmented Generation (RAG)** system using the **Endee Vector Database**. It allows users to query documents in natural language and receive accurate, context-based answers.

---

## ⚙️ Tech Stack

* Python
* Endee (Vector Database)
* Sentence Transformers (Embeddings)
* NumPy / Pandas
* Streamlit (optional UI)

---

## 🧠 How It Works

1. Input document is split into smaller chunks
2. Each chunk is converted into embeddings
3. Embeddings are stored in Endee vector database
4. User query is converted into embedding
5. Endee retrieves most relevant chunks
6. Retrieved data is used to generate final answer

---

## 🗂️ Project Structure

```
Smart-RAG-Endee/
│
├── embeddings.py      # Handles embedding generation
├── rag.py             # Core RAG pipeline logic
├── main.py            # Entry point of the application
├── requirements.txt   # Dependencies
├── README.md          # Project documentation
```

---

## 🔥 How Endee is Used

Endee is used as a **vector database** to:

* Store document embeddings
* Perform similarity search
* Retrieve relevant data efficiently for answering queries

---

## ▶️ Setup Instructions

### 1. Clone the repository

```
git clone https://github.com/Ajaykodthiwada/Smart-RAG-Endee.git
cd Smart-RAG-Endee
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Run the project

```
python main.py
```

---

## 📌 Example Usage

**Input:**

```
What is Artificial Intelligence?
```

**Output:**

```
Artificial Intelligence is the simulation of human intelligence in machines...
```

---

## 📸 Output

(Add a screenshot here if possible to improve presentation)

---

## ✅ Features

* Semantic search using embeddings
* Retrieval-Augmented Generation (RAG)
* Efficient vector search using Endee
* Simple and modular code structure

---

## 🚀 Future Improvements

* Add Streamlit-based UI
* Support multiple documents
* Improve answer generation using advanced LLMs
* Deploy as a web application

---

## 👨‍💻 Author

Ajay Kodthiwada
