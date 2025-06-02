from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional

from chains.keyword_extractor import get_trending_keywords
from chains.idea_generator import generate_post_prompts
from chains.post_generator import post_generation
from services.media_generator import generate_image
from services.quick_post import generate_full_post

router = APIRouter()

# Pydantic model for user input to most endpoints
class UserInput(BaseModel):
    prompt: str
    num_posts: int = 1
    tone: Optional[str] = "informative"
    num_words: int = 50
    generate_image: bool = False

# Endpoint: Extract trending keywords from user prompt
@router.post("/get_keywords")
def get_keywords(input: UserInput):
    if not input.prompt:
        raise HTTPException(status_code=400, detail="Prompt is required")
    keywords = get_trending_keywords(input.prompt)
    return {"keywords": keywords}

# Endpoint: Generate post prompts/ideas using keywords and user preferences
@router.post("/generate_post_prompts")
def post_prompts(input: UserInput ):
    if not input.prompt:
        raise HTTPException(status_code=400, detail="Prompt is required")
    
    keywords = get_trending_keywords(input.prompt)
    prompts = generate_post_prompts(input.prompt, keywords, input.tone, input.num_posts)
    return {"post_prompts": prompts , "keywords": keywords}

# Endpoint: Generate full posts (and optionally images) from prompts
@router.post("/generate_posts")
def posts(input: UserInput, prompts: List[str] = []):
    if not input.prompt:
        raise HTTPException(status_code=400, detail="Prompt is required")
    posts = []
    for prompt in prompts:
        title, post, hashtags, image_prompt = post_generation(prompt, input.num_words, input.tone)
        post_data = {
            "title": title,
            "content": post,
            "hashtags": hashtags,
            "image_prompt": image_prompt
        }
        if input.generate_image:
            image_url = generate_image(image_prompt)
            post_data["image_url"] = image_url
        posts.append(post_data)
    return {"posts": posts}

# Endpoint: Generate a complete post (keywords, idea, post, and optional image) in one call
@router.post("/quick_post")
def quick_post(
    prompt: str,
    tone: str = "informative",
    num_words: int = 100,
    generate_image: bool = False
):
    """
    Generate a complete social media post (keywords, idea, post, and optional image) in one call.
    """
    result = generate_full_post(
        user_prompt=prompt,
        tone=tone,
        num_words=num_words,
        generate_image_flag=generate_image
    )
    return result