from fastapi import FastAPI, HTTPException
import httpx

app = FastAPI(title="SaaS Billing API Gateway")

DJANGO_API_URL = "http://127.0.0.1:8000/api/billing"

# Helper function to fetch data from Django
async def fetch_from_django(endpoint: str):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(f"{DJANGO_API_URL}/{endpoint}/")
            response.raise_for_status()
            return response.json()
        except httpx.HTTPError as e:
            raise HTTPException(status_code=500, detail=str(e))

@app.get("/plans/")
async def get_plans():
    return await fetch_from_django("plans")

@app.get("/subscriptions/")
async def get_subscriptions():
    return await fetch_from_django("subscriptions")

@app.get("/invoices/")
async def get_invoices():
    return await fetch_from_django("invoices")

@app.get("/payments/")
async def get_payments():
    return await fetch_from_django("payments")
