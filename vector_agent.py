# vector_agent.py
import faiss
from langchain_community.vectorstores import FAISS
from langchain_community.docstore.in_memory import InMemoryDocstore

class VectorAgent:
    def __init__(self, embeddings):
        embedding_dim = len(embeddings.embed_query("hello world"))
        index = faiss.IndexFlatL2(embedding_dim)
        self.store = FAISS(
            embedding_function=embeddings,
            index=index,
            docstore=InMemoryDocstore(),
            index_to_docstore_id={},
        )

    def add_jobs(self, job_texts, extractor):
        import json
        for i, job_text in enumerate(job_texts):
            info_json = extractor(job_text)
            json_text = json.dumps(info_json, ensure_ascii=False)

            # Añadimos metadata explícita
            metadata = {"id": f"job_{i+1}"}

            self.store.add_texts(
                [json_text],
                metadatas=[metadata],
                ids=[f"job_{i+1}"]
            )

        print("Vacantes insertadas correctamente en FAISS 🎉")

    def search(self, query, k=1):
        results = self.store.similarity_search_with_score(query, k=k)

        parsed_results = []

        for doc, score in results:
            print("-----------")
            print("ID:", doc.metadata.get("id", "N/A"))
            print("Score:", float(score))
            print("Contenido:", doc.page_content)

            parsed_results.append({
                "id": doc.metadata.get("id", "N/A"),
                "score": float(score),
                "content": doc.page_content
            })

        return parsed_results