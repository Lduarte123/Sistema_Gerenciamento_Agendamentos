from config import create_connection
from sqlalchemy import Column, Integer, String, Date, Time
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine
from datetime import datetime

Base = declarative_base()

class UsuarioModel(Base):
    __tablename__ = 'usuarios'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    senha = Column(String, nullable=False)
    email = Column(String, nullable=False)
    data_nasc = Column(Date, nullable=False)
    cidade = Column(String, nullable=False)
    sexo = Column(String,  nullable=False)


engine = create_engine('postgresql://postgres:postgres@localhost/senac')
Session = sessionmaker(bind=engine)


class UsuarioRepository:
    def __init__(self):
        self.session = Session()

    def validar_usuario(self, email, senha):
        usuario = self.session.query(UsuarioModel).filter(UsuarioModel.email == email, UsuarioModel.senha == senha).first()
        return usuario
    

    def registrar_usuario(self, usuario):
        try:
            data_nasc = datetime.strptime(usuario.data_nasc, "%d-%m-%Y").date()
        except ValueError:
            data_nasc = usuario.data_nasc

        novo_usuario = UsuarioModel(
            nome=usuario.nome,
            email=usuario.email,
            senha=usuario.senha,
            data_nasc=data_nasc,
            cidade=usuario.cidade,
            sexo=usuario.sexo
        )

        self.session.add(novo_usuario)
        self.session.commit()

        
    def obter_emails_cadastrados(self):
        query = self.session.query(UsuarioModel.email).all()
        emails = [email[0] for email in query]
        return emails

