from fastapi import FastAPI, Request
import httpx
import os

app = FastAPI()

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_CHAT_ID = int(os.getenv("ADMIN_CHAT_ID"))

@app.post("/send_question/")
async def send_question(request: Request):
    data = await request.json()
    username = data.get("username", "пользователь")
    user_id = data.get("user_id", "unknown")
    question = data.get("question", "")

    message = f"❓ Новый вопрос от @{username} (ID: {user_id}):\n\n{question}"

    async with httpx.AsyncClient() as client:
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        payload = {"chat_id": ADMIN_CHAT_ID, "text": message}
        await client.post(url, json=payload)

    return {"status": "ok"}
