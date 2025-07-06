from fastapi import FastAPI, Form
from pydantic import EmailStr
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

@app.post("/send-email/")
async def send_email(
    destinatario: EmailStr = Form(...),
    assunto: str = Form(...),
    mensagem: str = Form(...)
):
    remetente = os.getenv("EMAIL_PASSWORD")
    senha = os.getenv("EMAIL_PASSWORD") # variável .env
        
    msg = MIMEMultipart()
    msg['From'] = remetente
    msg['To'] = destinatario
    msg['Subject'] = assunto
    msg.attach(MIMEText(mensagem, 'plain'))

    with smtplib.SMTP("smtp.mail.com", 587) as server:
        server.starttls("2147Rogope$"))
        server.login(remetente, senha)
        server.send_message(msg)

    return {"status": "Email enviado com sucesso"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
