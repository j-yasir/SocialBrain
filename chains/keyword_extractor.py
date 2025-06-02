from langchain.prompts import load_prompt
from schemas.output import KeywordOutput
from models.llm import get_llm

def get_trending_keywords(user_prompt: str) -> list[str]:
    llm = get_llm()
    template = load_prompt("prompts/keyword_prompt_template.json")
    structured_keywords_model = llm.with_structured_output(KeywordOutput, method="function_calling")
    formatted_prompt = template.format(user_prompt=user_prompt)
    result = structured_keywords_model.invoke(formatted_prompt)
    if isinstance(result, dict) and "keywords" in result:
        return result["keywords"]
    else:
        print("Error: Unexpected result format or missing 'keywords' key.")
        return []