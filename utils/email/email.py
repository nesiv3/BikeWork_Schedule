import httpx
import os
from dotenv import load_dotenv
from fastapi import HTTPException



load_dotenv()
BREVO_API_KEY = os.getenv("BREVO_API_KEY")

async def send_email(email):
    url = "https://api.brevo.com/v3/smtp/email"
    headers = {
        "accept": "application/json",
        "api-key": BREVO_API_KEY,
        "content-type": "application/json"
    }
    payload = {
        "sender": {
            "name": email.sender_name,
            "email": email.sender_email
        },
        "to": [
            {
                "email": email.recipient_email,
                "name": email.recipient_name
            }
        ],
        "subject": email.subject,
        "htmlContent": email.html_content
    }
    async with httpx.AsyncClient() as client:
        response = await client.post(url, headers=headers, json=payload)
        if response.status_code != 201:
            raise HTTPException(status_code=response.status_code, detail=response.text)