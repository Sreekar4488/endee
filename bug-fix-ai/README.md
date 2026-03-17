# 🔧 Bug Fix Suggestion AI

## 📌 Overview
Bug Fix Suggestion AI is an intelligent system that helps developers find solutions for programming errors. It uses semantic search and vector embeddings to match user input errors with similar known issues and suggests appropriate fixes.

---

## 🚀 Features
- Accepts user input (error message)
- Finds top matching bugs using AI
- Suggests relevant solutions
- Displays similarity scores
- Supports multiple result outputs (Top matches)

---

## 🧠 Tech Stack
- Python
- NumPy
- Sentence Transformers
- Endee Vector Database

---

## ⚙️ How It Works
1. Bug data is stored in `bugs.json`
2. Errors are converted into embeddings using AI models
3. Embeddings are stored using Endee
4. User input is converted into embedding
5. System finds most similar bugs using similarity search
6. Top matching results are displayed with solutions

---

## 📂 Project Structure