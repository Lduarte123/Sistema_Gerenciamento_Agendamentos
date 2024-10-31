import random
import smtplib
from email.mime.text import MIMEText
from datetime import datetime
from tkinter import simpledialog
from view.validar_codigo_view import ValidarCodigoWindow
from util.constantes import Constante

constante = Constante()

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
            raise ValueError(constante.get_codigo_nao_gerado())
        
        msg = MIMEText(f"{constante.get_mensagem_email()} {self.codigo}")
        msg['Subject'] = constante.get_assunto_email()
        msg['From'] = constante.get_email_remetente()
        msg['To'] = self.email_usuario

        with smtplib.SMTP(constante.get_smtp_servidor(), constante.get_smtp_porta()) as server:
            server.starttls()
            server.login(constante.get_email_remetente(), constante.get_email_senha())
            server.send_message(msg)

    def solicitar_codigo_verificacao(self, master):
        self.gerar_codigo()
        self.enviar_email()
        
        janela = ValidarCodigoWindow(master, constante.get_titulo_janela(), constante.get_mensagem_janela())
        janela.grab_set()
        master.wait_window(janela) 
        
        return janela.get_result()

    def validar_codigo(self, codigo_inserido):
        if self.codigo is not None and codigo_inserido is not None:
            return str(codigo_inserido) == str(self.codigo)
        return False