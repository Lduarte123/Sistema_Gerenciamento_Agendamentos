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
    

    def registrar_usuario(self, nome, email, senha, data_nasc, cidade, sexo):
        print(f"Tentando registrar: {nome}, {email}, {data_nasc}, {cidade}, {sexo}")  # Para depuração
        try:
            # Aqui você pode validar e preparar a data, se necessário
            data_nasc_formatada = datetime.strptime(data_nasc, "%d/%m/%Y").date()

            novo_usuario = UsuarioModel(
                nome=nome,
                email=email,
                senha=senha,
                data_nasc=data_nasc_formatada,
                cidade=cidade,
                sexo=sexo
            )
            
            self.session.add(novo_usuario)
            self.session.commit()
            print("Usuário registrado com sucesso.")  # Para depuração
            return True
        except Exception as e:
            print(f"Erro ao registrar usuário: {e}")  # Log do erro
            self.session.rollback()  # Reverter alterações em caso de erro
            return False



        
    def obter_emails_cadastrados(self):
        query = self.session.query(UsuarioModel.email).all()
        emails = [email[0] for email in query]
        return emails

