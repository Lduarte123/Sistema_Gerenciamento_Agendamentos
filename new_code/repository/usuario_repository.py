from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from datetime import datetime
from model.models import UsuarioModel, Base  # Importar de models.py

engine = create_engine('postgresql://postgres:123@localhost/postgres')
Base.metadata.create_all(engine)
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
    
    def obter_usuario_por_id(self, usuario_id):
        return self.session.query(UsuarioModel).filter_by(id=usuario_id).first()
    
    def atualizar_usuario(self, usuario_id, nome, email, cidade, sexo, senha):
        """Atualiza os dados do usuário no banco de dados."""
        try:
            usuario = self.session.query(UsuarioModel).filter_by(id=usuario_id).first()
            if usuario:
                usuario.nome = nome
                usuario.email = email
                usuario.cidade = cidade
                usuario.sexo = sexo
                usuario.senha = senha  # Considere hash a senha se necessário

                self.session.commit()  # Confirma as alterações
                return True
            else:
                print("Usuário não encontrado.")  # Para depuração
                return False
        except Exception as e:
            print(f"Erro ao atualizar usuário: {e}")  # Log do erro
            self.session.rollback()  # Reverter alterações em caso de erro
            return False


