from langchain.chat_models import init_chat_model
import regex as re


llm = init_chat_model("ollama:llama2:latest", temperature=0)

def parse_llm_output_json(text: str) -> str:
    match = re.search(r"\{(?:[^{}]|(?R))*\}", text)
    return match.group().strip() if match else None