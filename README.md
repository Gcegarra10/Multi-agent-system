# Multi-agent-system
Multi-agent RAG system for autonomous CV analysis, semantic job matching using FAISS, and automated scoring with LLMs.

# Accenture AI Challenge Finalist Project 🚀
This advanced system leverages a Multi-Agent Architecture and Retrieval-Augmented Generation (RAG) to automate the alignment between professional talent and job opportunities. It transforms unstructured PDF data into structured, actionable insights using LLMs and vector embeddings.

# 🏗️ System Architecture
The engine is divided into three specialized agent layers that ensure scalability, precision, and explainability:

1. Extraction & Data Integrity Agent 📄
Technology: OCR powered by doctr and schema validation via Pydantic.

Function: Processes PDF resumes to extract education, technical skills, and experience years with a guaranteed JSON output format.

Logic: Implements weighted experience calculations, accounting for internships and academic projects.

2. Semantic Vector Agent 🔍
Technology: FAISS (Facebook AI Similarity Search) and OllamaEmbeddings.

Function: Indexes job vacancies and performs high-dimensional semantic searches to find the "conceptual distance" between a candidate and a role.

Advantage: Moves beyond keyword matching by understanding the context and relationships between different technologies.

3. Expert Scoring Agent ⚖️
Technology: Advanced reasoning using Llama 2.

Function: Generates a comprehensive report including a Global Compatibility Score (0-10) and a probability of success.

Business Rules: Enforces strict filtering; if "Must-Have" requirements are not met, the admission probability is automatically set to 0%.
