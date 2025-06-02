from langchain.prompts import load_prompt
from schemas.output import PostOutput
from models.llm import get_llm

def post_generation(post_prompt, num_words, tone):
    llm = get_llm()
    post_gen_template = load_prompt("prompts/post_generation_template.json")
    structured_post_model = llm.with_structured_output(PostOutput, method="function_calling")
    formatted_post_gen_prompt = post_gen_template.format(
        post_prompt=post_prompt,
        num_words=num_words,
        tone=tone
    )
    result = structured_post_model.invoke(formatted_post_gen_prompt)
    return (
            result.get("title", ""),
            result.get("post", ""),
            result.get("hashtags", ""),
            result.get("image_prompt", "")
        )