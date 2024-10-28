import random
import smtplib
from email.mime.text import MIMEText
from datetime import datetime
from tkinter import simpledialog

class VerificacaoEmail:
    def __init__(self, email_usuario):
        self.email_usuario = email_usuario
        self.codigo = None
        self.timestamp = None

    def gerar_codigo(self):
        self.codigo = random.randint(100000, 999999)
        self.timestamp = datetime.now()
        return self.codigo

    # Email de Verificação
    def enviar_email(self):
        if self.codigo is None:
            raise ValueError("Código não gerado.")
        
        msg = MIMEText(f"Seu código de verificação é: {self.codigo}")
        msg['Subject'] = 'Código de Verificação'
        msg['From'] = 'projetodeagendamentos@gmail.com'
        msg['To'] = self.email_usuario

        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login('projetodeagendamentos@gmail.com', 'xaqh roat ndyq ajol')
            server.send_message(msg)

    def solicitar_codigo_verificacao(self):
        self.gerar_codigo()
        self.enviar_email()
        return simpledialog.askinteger("Código de Verificação", "Digite o código enviado para seu e-mail:")

    def validar_codigo(self, codigo_inserido):
        return codigo_inserido == self.codigo