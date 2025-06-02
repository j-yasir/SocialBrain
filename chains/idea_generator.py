from langchain.prompts import load_prompt
from schemas.output import PromptOutput
from models.llm import get_llm

def generate_post_prompts(user_prompt, keywords, tone, num_posts):
    llm = get_llm()
    post_template = load_prompt("prompts/post_prompt_template.json")
    structured_prompts_model = llm.with_structured_output(PromptOutput, method="function_calling")
    formatted_post_prompt = post_template.format(
        user_prompt=user_prompt,
        keywords=keywords,
        tone=tone,
        num_posts=num_posts
    )
    result = structured_prompts_model.invoke(formatted_post_prompt)
    return result["post_prompts"]