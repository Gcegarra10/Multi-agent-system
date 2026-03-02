import json
from utils import llm

def score_cv_job(cv_info: dict, job_info: dict) -> str:
    prompt = f"""
    Eres un evaluador experto de CVs y vacantes.  
    Dado un CV y una vacante, genera un **informe en español**, claro y breve (no demasiado extenso).

    1. **Score global del candidato para esta vacante (0 a 10)**  

    2. **Evaluación detallada**  
    - Educación  
    - Experiencia laboral  
    - Skills técnicas  
    - Idiomas  
    - Otros  

    3. **Skills requeridas y deseables**, indicando si el candidato las cumple (Sí/No).

    4. **Probabilidad de ser admitido en el puesto (0% a 100%)**  
    Regla obligatoria:
    - Si el candidato no cumple los años mínimos de experiencia → probabilidad = 0%.

    5. **Recomendaciones para mejorar el CV respecto a esta vacante.**

    CV:
    {json.dumps(cv_info, ensure_ascii=False)}

    Vacante:
    {json.dumps(job_info, ensure_ascii=False)}
    """

    output = llm.invoke(prompt)
    text_output = output.content.strip()
    return text_output