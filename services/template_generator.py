from langchain_core.prompts import PromptTemplate
import os

PROMPT_DIR = os.path.join(os.path.dirname(__file__), "../prompts")

# Ensure the prompts directory exists
os.makedirs(PROMPT_DIR, exist_ok=True)

prompt1 = PromptTemplate(
    validate_template=True,
    input_variables=["user_prompt"],
    template="""
    You are a social media trend analyst. Given a user prompt, your job is to extract
    the most trending keywords, hashtags, and related tags that people are searching or using online.

    Rules:
    - Focus on keywords that are popular in 2025.
    - Include hashtags that are trending on Facebook, X, TikTok, Instagram, Linkedin and YouTube.
    - Return exactly 25 items as a list.
    - Don't include explanations, only output the tags or keywords.

    User Prompt: "{user_prompt}"

    Trending Keywords:
    """
)

prompt1.save(os.path.join(PROMPT_DIR, "keyword_prompt_template.json"))





# Prompt for generating post prompts
# prompt2 = PromptTemplate(
#     template="""
# You are a creative social media strategist and Prompt Engineer.

#     Based on the following:
#     - User Topic: {user_prompt}
#     - Trending Keywords: {keywords}
#     - Tone: {tone}
#     - Number of Posts: {num_posts}

#     Generate {num_posts} UNIQUE and engaging social media post prompts.

#     Rules:
#     - Incorporate multiple trending keywords into each post idea (at least 2 per post)
#     - Match the tone: {tone}
#     - Write breifly about the post structure and things to include (7 sentences max)
#     - Include a separate line with 7-10 hashtags
#     - Each post should be unique and not repetitive.
#     - specify that the post is a text based social media post.

#     Format:
#     1. prompt: ...
#        Hashtags: ...

#     Start now.
# """,
#     input_variables=["user_prompt", "keywords", "tone", "num_posts"],
#     validate_template=True,
# )

prompt2 = PromptTemplate(
    template="""
You are a seasoned social media strategist and Prompt Engineer tasked with generating high-quality **text-based social media post ideas** for a content creation pipeline.

Based on:
- **User Topic**: {user_prompt}
- **Trending Keywords**: {keywords}
- **Tone**: {tone}
- **Number of Post Ideas to Generate**: {num_posts}

Your objective is to generate {num_posts} **detailed and unique post ideas** that serve as excellent blueprints for full content generation.

Each post idea should:
- Clearly describe the **post structure** (e.g., hook, main content, call-to-action)
- Include **at least two trending keywords**
- Match the **{tone}** consistently throughout
- Stay within **7 sentences**
- Be **concrete, descriptive**, and not abstract or vague
- Be **unique** from the others
- End with a new line of **7–10 relevant hashtags**

---
**Format Example**:
Start with a compelling question about climate anxiety. Share a statistic from the latest UK climate report. Emphasize the urgency for renewable energy adoption. Present solar and wind energy as key solutions. End with a motivational call to take action. Mention a notable initiative or campaign in GB. Wrap with a relatable, hopeful note.
#ClimateAction #UKClimate #SolarPower #WindEnergy #ClimateHope #GreenFuture #EcoFriendly #ActNow #Sustainability #Renewables

Start now.
""",
    input_variables=["user_prompt", "keywords", "tone", "num_posts"],
    validate_template=True,
)

prompt2.save(os.path.join(PROMPT_DIR, "post_prompt_template.json"))
 




# Prompt for generating social media posts
post_generation_template = PromptTemplate(
    template="""
You are a professional social media content creator.

    Based on the following:
    - Post Prompt: {post_prompt}
    - Number of Words: {num_words}
    - Tone: {tone}

    Generate a high-quality social media post.

    Rules:
    - Ensure the post adheres to the specified tone: {tone} and {post_prompt}.
    - The post should be {num_words} words.
    - Include a call-to-action (CTA) at the end of the post.
    - Use engaging language to capture the audience's attention.
    - If applicable, include 3-5 relevant hashtags at the end of the post.

    Also Generate a well designed image prompt for the post.
    - The image prompt should be visually appealing and relevant to the post content.
    - Include details about colors, style, and any specific elements to include in the image.
    - The image prompt should be suitable for platforms like Instagram, Facebook, or Twitter.
    - The image prompt should be 2-4 sentences.

    Format:
    Post: ...
    Hashtags: ...
    image prompt: ...

    Start now.
""",
    input_variables=["post_prompt", "num_words", "tone"],
    validate_template=True,
)



post_generation_template = PromptTemplate(
    template="""
You are a professional social media content creator.

Your task is to generate a high-quality **text-based social media post** and a matching **AI image prompt** for visual platforms like Instagram, Twitter, or Facebook.

Input:
- **Post Idea Prompt**: {post_prompt}
- **Target Length**: {num_words} words
- **Tone**: {tone}

---

### 📝 Post Requirements:
- The post must **strictly follow the tone**: {tone}
- Total length: approx. {num_words} words
- The post must include the following structure:
  - **Hook**: A compelling first line to capture attention
  - **Main Body**: Expand on the idea with value, insights, or storytelling
  - **CTA**: A strong, clear call-to-action that invites engagement (comment, share, learn more, etc.)
- Ensure alignment with the original post prompt ({post_prompt})
- Use **engaging, human, and impactful language**
- End with 3–5 **highly relevant hashtags** (no generic fillers)

---

### 🖼️ Image Prompt Requirements:
- Generate a **separate AI image prompt** based directly on the content and emotion of the post.
- It should clearly describe:
  - **Scene setting** (what’s happening visually)
  - **Key elements** to include (objects, actions, expressions)
  - **Style** (photorealistic, flat illustration, minimalist, retro, etc.)
  - **Mood/Colors** that match the tone
- The prompt should be **2–4 vivid, descriptive sentences**.
- It must be suitable for generating visuals via AI tools like DALL·E or Midjourney.

---

### 📌 Output Format:
Respond **only** in the following structured Python dictionary format (no extra text):

```python
PostOutput = {{
    "title": "<Title of the post>",
    "post": "<Full social media post content>",
    "hashtags": "<Comma-separated or space-separated hashtags>",
    "image_prompt": "<Well-described and relevant image prompt>"
}}

Now begin.
""",
    input_variables=["post_prompt", "num_words", "tone"],
    validate_template=True,
)


post_generation_template.save(os.path.join(PROMPT_DIR, "post_generation_template.json"))