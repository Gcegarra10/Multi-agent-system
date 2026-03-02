# Multi-agent-system
Multi-agent RAG system for autonomous CV analysis, semantic job matching using FAISS, and automated scoring with LLMs.
This project features an advanced Multi-Agent RAG (Retrieval-Augmented Generation) System designed to automate the alignment between professional profiles and job opportunities. Developed for the Accenture AI Challenge, the system transforms unstructured PDF data into structured, actionable insights using LLMs, vector embeddings, and rigorous data validation.

🏗️ System Architecture
The solution is built on a modular, agentic framework where specialized components collaborate to ensure precision and scalability:

Extraction Agent (OCR & Structured Output): Utilizes doctr for optical character recognition and Pydantic to enforce data schemas, ensuring that education, experience, and skills are parsed into reliable JSON formats.

Vector Agent (Semantic Search): Implements FAISS (Facebook AI Similarity Search) to index job vacancies. It performs high-dimensional semantic searches to find matches based on context rather than just keywords.

Scoring Agent (Reasoning & Evaluation): An LLM-driven agent that analyzes the "Must Have" and "Nice to Have" requirements. It calculates a compatibility score (0-10) and applies business logic (e.g., minimum experience filters) to generate human-readable recommendations.

🛠️ Tech Stack
Orchestration: LangChain.

Language Model: Llama 2 via Ollama.

Vector Database: FAISS.

Data Integrity: Pydantic Models.

UI/Interface: Streamlit.

📈 Financial Industry Relevance
While applied to recruitment, this architecture is highly transferable to Global Asset Allocation:

Unstructured Data Processing: The same logic used to parse CVs can be applied to extracting financial KPIs from quarterly earnings reports.

Portfolio Similarity: The vector indexing approach allows for identifying assets with similar risk/return profiles across global markets.

Automated Due Diligence: The scoring agent demonstrates how to automate the checking of investment mandates and regulatory constraints.

🚀 Key Features
Automated Parsing: Extracts years of experience, technical skills, and educational background from PDFs.

Strict Business Rules: Includes logic to discard candidates if they don't meet the "must-have" experience criteria.

Explainable AI: Provides a detailed report justifying why a candidate fits or does not fit a specific role.
