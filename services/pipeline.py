from langchain.chains import SequentialChain
from chains.keyword_extractor import get_trending_keywords
from chains.idea_generator import generate_post_prompts
from chains.post_generator import post_generation

def build_langchain_pipeline(num_posts: int, tone: str, num_words: int = 100):
    # Define each step as a function or a LangChain Runnable
    def keywords_chain(inputs):
        return {"keywords": get_trending_keywords(inputs["user_prompt"])}

    def prompts_chain(inputs):
        return {
            "post_prompts": generate_post_prompts(
                inputs["user_prompt"],
                inputs["keywords"],
                tone,
                num_posts
            )
        }

    def posts_chain(inputs):
        posts = []
        for prompt in inputs["post_prompts"]:
            title, post, hashtags, image_prompt = post_generation(prompt, num_words, tone)
            posts.append({
                "title": title,
                "post": post,
                "hashtags": hashtags,
                "image_prompt": image_prompt
            })
        return {"posts": posts}

    # Compose the chains
    chain = SequentialChain(
        chains=[
            keywords_chain,
            prompts_chain,
            posts_chain
        ],
        input_variables=["user_prompt"],
        output_variables=["posts"]
    )
    return chain

# Usage:
# pipeline = build_langchain_pipeline(num_posts=3, tone="casual")
# result = pipeline({"user_prompt": "AI in healthcare"})
# print(result["posts"])