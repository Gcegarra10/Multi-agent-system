import json
from utils import llm, parse_llm_output_json

def extract_job_info(job_text: str) -> dict:
    prompt = f"""
    Eres un extractor de vacantes.  
    Devuelve SOLO un JSON con esta estructura exacta:

    {{
        "title": "",
        "location": "",
        "company": "",
        "work_model": "",
        "experience_required": 0,
        "must_have_skills": [],
        "nice_to_have_skills": [],
        "description": ""
    }}

    Reglas:
    - "experience_required" debe ser un número (años).
    - "must_have_skills" debe contener SOLO skills técnicas explícitamente requeridas.
    - "nice_to_have_skills" debe contener skills deseables para la vacante específica.

    Vacante:
    {job_text}
    """

    output = llm.invoke(prompt)
    text_output = output.content.strip()
    text_output = parse_llm_output_json(text_output)

    try:
        return json.loads(text_output)
    except json.JSONDecodeError as e:
        print("❌ Error parseando JSON")
        return None