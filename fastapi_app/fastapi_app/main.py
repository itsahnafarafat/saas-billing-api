from fastapi import FastAPI, HTTPException
import httpx

app = FastAPI(title="SaaS Billing API Gateway")

DJANGO_API_URL = "http://127.0.0.1:8000/api/billing"  # Update if using another host

@app.get("/plans/")
async def get_plans():
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(f"{DJANGO_API_URL}/plans/")
            response.raise_for_status()
            return response.json()
        except httpx.HTTPError as e:
            raise HTTPException(status_code=500, detail=str(e))

@app.get("/subscriptions/")
async def get_subscriptions():
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(f"{DJANGO_API_URL}/subscriptions/")
            response.raise_for_status()
            return response.json()
        except httpx.HTTPError as e:
            raise HTTPException(status_code=500, detail=str(e))
