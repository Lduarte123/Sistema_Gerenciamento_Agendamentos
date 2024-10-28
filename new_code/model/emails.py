import random
import smtplib
from email.mime.text import MIMEText
from datetime import datetime
from tkinter import simpledialog
from view.validar_codigo_view import ValidarCodigoWindow


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

    def solicitar_codigo_verificacao(self, master):
        self.gerar_codigo()
        self.enviar_email()
        
        janela = ValidarCodigoWindow(master, "Código de Verificação", "Digite o código enviado para seu e-mail:")
        janela.grab_set()
        master.wait_window(janela) 
        

        return janela.get_result()

    def validar_codigo(self, codigo_inserido):
        if self.codigo is not None and codigo_inserido is not None:
            return str(codigo_inserido) == str(self.codigo)
        return False
    