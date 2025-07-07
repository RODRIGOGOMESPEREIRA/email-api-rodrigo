from fastapi import FastAPI, Form, File, UploadFile
from pydantic import EmailStr
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "online"}

@app.post("/send-email/")
async def send_email(
    destinatario: EmailStr = Form(...),
    assunto: str = Form(...),
    mensagem: str = Form(...),
    anexo: UploadFile = File(None)
):
    remetente = os.getenv("EMAIL_ADDRESS")
    senha = os.getenv("EMAIL_PASSWORD")

    msg = MIMEMultipart()
    msg['From'] = remetente
    msg['To'] = destinatario
    msg['Subject'] = assunto
    msg.attach(MIMEText(mensagem, 'plain'))

    if anexo:
        conteudo = await anexo.read()
        parte = MIMEApplication(conteudo, Name=anexo.filename)
        parte['Content-Disposition'] = f'attachment; filename="{anexo.filename}"'
        msg.attach(parte)

    with smtplib.SMTP("smtp.mail.com", 587) as server:
        server.starttls()
        server.login(remetente, senha)
        server.send_message(msg)

    return {"status": "Email enviado com sucesso"}
