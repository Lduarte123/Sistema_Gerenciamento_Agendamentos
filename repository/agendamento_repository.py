from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from model.models import AgendamentoModel
from util.constantes import Constante
from util.data_base_cfg import Config
from model.models import Base

constante = Constante()
config = Config()

engine = create_engine(config.get_cfg())
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

class AgendamentoRepository:
    def __init__(self):
        self.session = Session()

    def salvar_agendamento(self, agendamento):
        try:
            data = datetime.strptime(agendamento.data, "%d-%m-%Y").date()
        except ValueError:
            data = agendamento.data

        try:
            horario = datetime.strptime(agendamento.horario, "%H:%M").time()
        except ValueError:
            horario = agendamento.horario

        novo_agendamento = AgendamentoModel(
            nome=agendamento.nome,
            data=data,
            horario=horario,
            local=agendamento.local,
            descricao=agendamento.descricao,
            usuario_id=agendamento.usuario_id,
            status = "Ativo"
        )

        self.session.add(novo_agendamento)
        self.session.commit()

    def listar_agendamentos(self):
        return self.session.query(AgendamentoModel).all()

    def atualizar_agendamento(self, agendamento_atualizado):
        agendamento_existente = self.session.query(AgendamentoModel).filter_by(id=agendamento_atualizado.id).first()

        agendamento_existente.nome = agendamento_atualizado.nome
        agendamento_existente.data = agendamento_atualizado.data
        agendamento_existente.horario = agendamento_atualizado.horario
        agendamento_existente.local = agendamento_atualizado.local
        agendamento_existente.descricao = agendamento_atualizado.descricao

        self.session.commit()

    def excluir_agendamento(self, agendamento_id):
        agendamento = self.session.query(AgendamentoModel).filter_by(id=agendamento_id).first()
        self.session.delete(agendamento)
        self.session.commit()

    def fechar_conexao(self):
        self.session.close()

    def listar_agendamentos_por_usuario(self, usuario_id):
        return self.session.query(AgendamentoModel).filter(AgendamentoModel.usuario_id == usuario_id).all()

    def cancelar_agendamento(self, agendamento_id):
        agendamento = self.session.query(AgendamentoModel).filter_by(id=agendamento_id).first()
        agendamento.status = constante.get_status_cancelado()
        self.session.commit()

    def obter_agendamentos_por_termo(self, termo):
        return self.session.query(AgendamentoModel).filter(
            AgendamentoModel.nome.ilike(f"%{termo}%")
        ).all()

