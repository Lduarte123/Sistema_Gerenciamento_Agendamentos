from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from tkinter import messagebox
from model.models import UsuarioModel
from util.constantes import Constante
from util.data_base_cfg import Config
from model.models import Base
import customtkinter as ctk

constante = Constante()
config = Config()


engine = create_engine(config.get_cfg())
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

class UsuarioRepository:
    def __init__(self):
        self.session = Session()

    def validar_usuario(self, email, senha):
        usuario = self.session.query(UsuarioModel).filter(UsuarioModel.email == email, UsuarioModel.senha == senha).first()
        return usuario
    
    def registrar_usuario(self, nome, email, senha, data_nasc, cidade, sexo, tipo):
        try:
            data_nasc_formatada = datetime.strptime(data_nasc, "%d/%m/%Y").date()

            novo_usuario = UsuarioModel(
                nome=nome,
                email=email,
                senha=senha,
                data_nasc=data_nasc_formatada,
                cidade=cidade,
                sexo=sexo,
                tipo=tipo
            )
            
            self.session.add(novo_usuario)
            self.session.commit()
            print(constante.get_mensagem_sucesso_registro())
            return True
        
        except:
            self.session.rollback()
            return False

    def obter_emails_cadastrados(self):
        query = self.session.query(UsuarioModel.email).all()
        emails = [email[0] for email in query]
        return emails
    
    def obter_usuario_por_id(self, usuario_id):
        return self.session.query(UsuarioModel).filter_by(id=usuario_id).first()
    
    def atualizar_usuario(self, usuario_id, nome, email, cidade, sexo, senha):
        try:
            usuario = self.session.query(UsuarioModel).filter_by(id=usuario_id).first()
            if usuario:
                usuario.nome = nome
                usuario.email = email
                usuario.cidade = cidade
                usuario.sexo = sexo
                usuario.senha = senha 
                self.session.commit()
                messagebox.showinfo("Sucesso", "Perfil atualizado com sucesso.")
                return True
            else:
                print(constante.get_mensagem_usuario_nao_encontrado()) 
                messagebox.showerror("Erro", constante.get_mensagem_usuario_nao_encontrado())

                return False
        except:
            self.session.rollback()
            messagebox.showerror("Erro", "Ocorreu um erro ao atualizar o perfil. Tente novamente.")
            return False
    
    def obter_usuario_logado_email(self, usuario_id):
        usuario = self.session.query(UsuarioModel).filter_by(id=usuario_id).first()
        return usuario.email if usuario else None
    
    def checar_tipo(self, usuario_id):
        return self.session.query(UsuarioModel).filter_by(tipo='admin', id=usuario_id).first() is not None
    
    def listar_usuarios(self, pagina=1, itens_por_pagina=20):
        """
        Retorna uma lista de usuários, com paginação.
        
        :param pagina: número da página para paginação (default 1)
        :param itens_por_pagina: quantidade de itens por página (default 20)
        :return: Lista de usuários da página solicitada
        """
        try:
            # Calculando o offset para a paginação
            offset = (pagina - 1) * itens_por_pagina
            
            # Realiza a consulta com a limitação de itens e o offset para paginação
            usuarios = self.session.query(UsuarioModel).offset(offset).limit(itens_por_pagina).all()
            
            return usuarios
        except Exception as e:
            print(f"Erro ao listar usuários: {e}")
            return []

