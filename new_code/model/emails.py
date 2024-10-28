import random
import smtplib
from email.mime.text import MIMEText
from datetime import datetime, timedelta

class VerificacaoEmail:
    def __init__(self, email_usuario):
        self.email_usuario = email_usuario
        self.codigo = None
        self.timestamp = None

    def gerar_codigo(self):
        self.codigo = random.randint(100000, 999999)
        self.timestamp = datetime.now()
        return self.codigo

    def enviar_email(self):
        if self.codigo is None:
            raise ValueError("Código não gerado.")
        
        msg = MIMEText(f"Seu código de verificação é: {self.codigo}")
        msg['Subject'] = 'Código de Verificação'
        msg['From'] = 'projetodeagendamento@gmail.com'
        msg['To'] = self.email_usuario

        with smtplib.SMTP('smtp.exemplo.com', 587) as server:
            server.starttls()
            server.login('projetodeagendamento@gmail.com', 'pythonmuchbetterthanjava')
            server.send_message(msg)

    def validar_codigo(self, codigo_inserido):
        if self.codigo is None or self.timestamp is None:
            return False
        
        if codigo_inserido == self.codigo and (datetime.now() - self.timestamp) < timedelta(minutes=5):
            return True
        return False
