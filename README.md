# 🚀 Endee AI Project – Semantic Search & RAG System

## 📌 Project Overview

This project demonstrates a **Retrieval Augmented Generation (RAG)** based AI system using vector embeddings.
It enables **semantic search**, where user queries are matched based on meaning rather than exact keywords.

---

## 🎯 Problem Statement

Traditional search systems rely on keyword matching, which often fails to understand the context of user queries.
This project solves that problem using **vector embeddings and similarity search** to return more relevant results.

---

## 🧠 Key Features

* 🔍 Semantic Search (meaning-based search)
* 🤖 Retrieval Augmented Generation (RAG)
* ⚡ FastAPI backend for API endpoints
* 🧮 Vector embeddings using Sentence Transformers
* 📊 Top-k relevant results retrieval

---

## ⚙️ Tech Stack

* **Python**
* **FastAPI**
* **Sentence Transformers**
* **Endee (Vector Database Concept)**
* **Uvicorn**

---

## 🏗️ System Design

### 🔄 Workflow

1. User enters a query
2. Query is converted into vector embedding
3. Stored documents are also converted into embeddings
4. Similarity search is performed using vector comparison
5. Top relevant results are returned

---

## 📂 Project Structure

```
endee/
 ├── app/
 │   ├── main.py          # FastAPI entry point
 │   ├── rag.py           # RAG logic (search + storage)
 │   ├── embeddings.py    # Embedding generation
 ├── README.md
 ├── requirements.txt
```

---

## 🧠 How Endee is Used

Endee is a **vector database** designed for efficient similarity search.

In this project:

* Text data is converted into embeddings
* Embeddings are stored and compared
* Similarity search is performed to retrieve relevant results

(Current implementation uses in-memory storage, but follows Endee’s vector search principles.)

---

## ▶️ How to Run the Project

### 🔹 Step 1: Clone Repository

```bash
git clone https://github.com/poemsun101/endee.git
cd endee
```

### 🔹 Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### 🔹 Step 3: Run Server

```bash
python -m uvicorn app.main:app --reload
```

---

## 🌐 API Endpoints

### 🏠 Home

```
GET /
```

### 🔍 Ask Query

```
GET /ask?q=your_question
```

### ✅ Example

```
/ask?q=What is AI?
```

---

## 📌 Example Output

```json
{
  "query": "What is AI?",
  "results": [
    "AI is Artificial Intelligence",
    "Machine Learning is part of AI"
  ]
}
```

---

## 🚀 Future Enhancements

* 🔗 Integrate real Endee vector database
* 🌐 Add frontend UI (React / Streamlit)
* 🧠 Improve ranking with advanced models
* 📊 Add analytics dashboard

---

## 🙌 Conclusion

This project demonstrates how **vector databases and embeddings** can significantly improve search systems using AI techniques like RAG.

---

## 📎 Submission

GitHub Repository:
https://github.com/poemsun101/endee

---

⭐ If you like this project, consider giving it a star!
