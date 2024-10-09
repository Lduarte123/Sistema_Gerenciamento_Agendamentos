from sqlalchemy import Column, Integer, String, Date, Time
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine
from datetime import datetime

Base = declarative_base()

class AgendamentoModel(Base):
    __tablename__ = 'agendamentos'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    data = Column(Date, nullable=False)
    horario = Column(Time, nullable=False)
    local = Column(String, nullable=False)
    descricao = Column(String, nullable=True)

# Criando a engine e a sessão do banco de dados
engine = create_engine('postgresql://postgres:123@localhost/postgres')
Session = sessionmaker(bind=engine)

class AgendamentoRepository:
    def __init__(self):
        self.session = Session()

    def salvar_agendamento(self, agendamento):
        try:
            data = datetime.strptime(agendamento.data, "%d-%m-%Y").date()  # Forçando a conversão de string para date
        except ValueError:
            data = agendamento.data  # Se já for um date, usaremos diretamente

        try:
            horario = datetime.strptime(agendamento.horario, "%H:%M").time()  # Forçando a conversão de string para time
        except ValueError:
            horario = agendamento.horario  # Se já for um time, usaremos diretamente

        # Criando a instância do modelo
        novo_agendamento = AgendamentoModel(
            nome=agendamento.nome,
            data=data,
            horario=horario,
            local=agendamento.local,
            descricao=agendamento.descricao
        )

        self.session.add(novo_agendamento)
        self.session.commit()

    def listar_agendamentos(self):
        return self.session.query(AgendamentoModel).all()

    def atualizar_agendamento(self, agendamento_atualizado):
        agendamento_existente = self.session.query(AgendamentoModel).filter_by(id=agendamento_atualizado.id).first()

        # Atualizando os campos, assumindo que o agendamento existe
        agendamento_existente.nome = agendamento_atualizado.nome
        agendamento_existente.data = agendamento_atualizado.data
        agendamento_existente.horario = agendamento_atualizado.horario
        agendamento_existente.local = agendamento_atualizado.local
        agendamento_existente.descricao = agendamento_atualizado.descricao

        self.session.commit()

    def excluir_agendamento(self, agendamento_id):
        # Encontrando o agendamento pelo ID e excluindo
        agendamento = self.session.query(AgendamentoModel).filter_by(id=agendamento_id).first()
        self.session.delete(agendamento)
        self.session.commit()

    def fechar_conexao(self):
        self.session.close()
