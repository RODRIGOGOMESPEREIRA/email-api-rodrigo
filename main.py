from fastapi import FastAPI, Form
from pydantic import EmailStr
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = FastAPI()

@app.post("/send-email/")
async def send_email(
    destinatario: EmailStr = Form(...),
    assunto: str = Form(...),
    mensagem: str = Form(...)
):
    remetente = "rodrigogp@dr.com"
    senha = "SUA_SENHA_DO_MAIL.COM"

    msg = MIMEMultipart()
    msg['From'] = remetente
    msg['To'] = destinatario
    msg['Subject'] = assunto
    msg.attach(MIMEText(mensagem, 'plain'))

    with smtplib.SMTP("smtp.mail.com", 587) as server:
        server.starttls()
        server.login(remetente, senha)
        server.send_message(msg)

    return {"status": "Email enviado com sucesso"}
