# main.py
import subprocess
import sys
from pathlib import Path

project_root = Path(__file__).resolve().parent
app_path = project_root / "app" / "1_Home_page.py"

subprocess.run([sys.executable, "-m", "streamlit", "run", str(app_path)])













"""if __name__ == "__main__":
    orch = Orchestrator()

    results = orch.run_matching_pipeline(
        cv_filename="MiguelAngelHuamani_CV_Maverick.pdf",
        similarity_k=2
    )

    for r in results:
        print("\n================================")
        print(f"Vacante: {r['job_file']}")
        print(f"Similaridad FAISS: {r['similarity_score']:.4f}")
        print("Evaluación:")
        print(r["evaluation"])


"""
"""
# ---------------------------
# Inicialización embeddings
# ---------------------------
embeddings = OllamaEmbeddings(model="nomic-embed-text")
vector_agent = VectorAgent(embeddings)

# ---------------------------
# Ejemplo: CV y Vacantes
# ---------------------------
cv_data = extract_cv_info_from_pdf("cvs/MiguelAngelHuamani_CV_Maverick.pdf")
job_texts = [open("vacantes/job1.txt").read(), open("vacantes/job2.txt").read(), open("vacantes/job3.txt").read()]
vector_agent.add_jobs(job_texts, extract_job_info)

# ---------------------------
# Búsqueda por similitud
# ---------------------------
query = "Machine Learning, Python, NLP, LLMs, MLOps"
# Buscar los K más similares
results = vector_agent.search(str(cv_data), k=2)

all_evaluations = []

for res in results:
    job_id = res["id"]          # índice de la vacante
    similarity = res["score"]   # score FAISS

    index = int(job_id.replace("job_", "")) - 1
    job_data = extract_job_info(job_texts[index])

    cv_vs_job_eval = score_cv_job(cv_data, job_data)

    all_evaluations.append({
        "job_id": job_id,
        "similarity_score": similarity,
        "evaluation": cv_vs_job_eval
    })

# Mostrar resultados
for ev in all_evaluations:
    print("\n==============================")
    print(f"VACANTE {ev['job_id']} — Similaridad FAISS: {ev['similarity_score']:.4f}")
    print(ev["evaluation"])
    
"""
