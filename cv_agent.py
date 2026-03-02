# cv_agent.py
import json, regex as re
from pydantic import BaseModel
from typing import List, Optional, Union
from doctr.io import DocumentFile
from doctr.models import ocr_predictor

from utils import llm, parse_llm_output_json

class EducationEntry(BaseModel):
    institution: str
    degree: str
    graduation_date: Optional[str] = None
    expected_graduation: Optional[str] = None

class CVInfo(BaseModel):
    name: Optional[str]
    contact: Optional[str]
    location: Optional[str]
    experience_years: Optional[float]
    experience_summary: Optional[str]
    education: List[EducationEntry] = []
    skills: List[str] = []
    languages: List[str] = []
    other_info: Optional[Union[str, list]] = None


def extraer_texto(pdf_path: str) -> str:
    model = ocr_predictor(pretrained=True)
    doc = DocumentFile.from_pdf(pdf_path)
    result = model(doc)

    texto = ""
    for page in result.pages:
        for block in page.blocks:
            if hasattr(block, "lines"):
                for line in block.lines:
                    texto += " ".join([w.value for w in line.words]) + "\n"
        texto += "\n"
    return texto

def extract_cv_info_from_pdf(pdf_path: str) -> dict:
    cv_text = extraer_texto(pdf_path)
    prompt = f"""
    Eres un extractor profesional de CVs.  
    Analiza el siguiente CV y devuelve SOLO un JSON con EXACTAMENTE esta estructura:

    {{
        "name": "",
        "contact": "",
        "location": "",
        "experience_years": 0,
        "experience_summary": "",
        "experience": [
            "Job title at Company (Duration) - resumen de 1-2 frases incluyendo tecnologías usadas (LLMs, NLP, RAG, AWS, Python, etc.)"
        ],
        "education": [
            "Degree at Institution (Year)"
        ],
        "skills": ["Python", "AWS", "PyTorch", "..."],
        "languages": ["English", "Spanish"],
        "other_info": ""
    }}

    REGLAS OBLIGATORIAS:

    1. **El campo "experience" ES OBLIGATORIO.**  
    Debe extraer:  
    - trabajos  
    - prácticas  
    - TFG / capstone  
    - proyectos relevantes  
    - investigaciones  
    - colaboraciones  
    Aunque sean académicos.

    2. Resume cada experiencia en 1–2 frases incluyendo tecnologías concretas:  
    ✔ LLMs  
    ✔ LangChain / RAG  
    ✔ AWS  
    ✔ PyTorch / TensorFlow  
    ✔ Docker  
    ✔ Kubernetes  
    ✔ ML pipelines  
    (Si aparecen en el CV)

    3. **experience_years** debe excluir proyectos académicos, pero incluir:  
    - trabajo real  
    - freelancing real  
    - prácticas (computan como 0.1–0.5 años cada una)

    4. **skills SOLO contiene skills técnicas.**  
    ❌ No incluir idiomas  
    ❌ No incluir soft skills  
    ✔ Incluir AWS aunque no haya proyecto asociado

    5. Si un skill aparece pero no se menciona un proyecto asociado → indícalo igualmente.

    6. Si detectas GPA, nota media, certificaciones, premios → ponlos en "other_info".

    7. Devuelve SOLO JSON válido.

    CV completo:
    {cv_text}
    """
    output = llm.invoke(prompt)
    text_output = output.content.strip()
    text_output = parse_llm_output_json(text_output)
    
    try:
        data = json.loads(text_output)
        return data
    except json.JSONDecodeError:
        print("❌ Error parseando JSON")
        return None