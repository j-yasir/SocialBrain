import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables (including OPENAI_API_KEY)
load_dotenv()

client = OpenAI()

def generate_image(prompt: str, size: str = "1024x1024", quality: str = "standard", n: int = 1) -> str:
    """
    Generate an image using OpenAI's DALL-E 3 model.

    Args:
        prompt (str): The prompt describing the image.
        size (str): The size of the image (default "1024x1024").
        quality (str): The quality of the image (default "standard").
        n (int): Number of images to generate (default 1).

    Returns:
        str: The URL of the generated image.
    """
    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size=size,
        quality=quality,
        n=n
    )
    return response.data[0].url