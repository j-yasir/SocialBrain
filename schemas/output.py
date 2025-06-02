from typing import TypedDict, List, Annotated

class KeywordOutput(TypedDict):
    keywords: List[str]

class PromptOutput(TypedDict):
    post_prompts: Annotated[list[str], "List of post prompts each prompt contains the full prompt and the relevant hashtags"]

class PostOutput(TypedDict):
    title: Annotated[str, "Title of the post"]
    post: Annotated[str, "Content of the post"]
    hashtags: Annotated[str, "Hashtags for the post"]
    image_prompt: Annotated[str, "Well described Image prompt for the post"]