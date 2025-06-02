from fastapi import FastAPI
from dotenv import load_dotenv
from app.api.v1.endpoints import router
load_dotenv()

app = FastAPI(
    title="SocialBrain API",
    version="1.0",
    description="AI-powered social media content generator."
)

app.include_router(router)
