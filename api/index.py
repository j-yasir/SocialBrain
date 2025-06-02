from vercel_fastapi import VercelFastAPI
from app.main import app

vercel_app = VercelFastAPI(app)