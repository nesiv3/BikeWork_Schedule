import httpx
from fastapi import HTTPException

async def send_email(email):
    url = "https://api.brevo.com/v3/smtp/email"
    headers = {
        "accept": "application/json",
        "api-key": "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",
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