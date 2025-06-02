from chains.keyword_extractor import get_trending_keywords
from chains.idea_generator import generate_post_prompts
from chains.post_generator import post_generation
from services.media_generator import generate_image

def generate_full_post(user_prompt, tone="informative", num_words=100, generate_image_flag=False):
    # Step 1: Extract trending keywords
    keywords = get_trending_keywords(user_prompt)
    
    # Step 2: Generate post ideas/prompts
    post_prompts = generate_post_prompts(user_prompt, keywords, tone, num_posts=1)
    if not post_prompts:
        return {"error": "Failed to generate post prompts."}
    post_prompt = post_prompts[0]
    
    # Step 3: Generate the post
    title, post, hashtags, image_prompt = post_generation(post_prompt, num_words, tone)
    
    # Step 4: Optionally generate the image
    image_url = None
    if generate_image_flag:
        image_url = generate_image(image_prompt)
    
    return {
        "title": title,
        "content": post,
        "hashtags": hashtags,
        "image_prompt": image_prompt,
        "image_url": image_url
    }