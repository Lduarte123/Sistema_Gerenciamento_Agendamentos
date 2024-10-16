from sqlalchemy import Column, Integer, String, Date, Time, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class UsuarioModel(Base):
    __tablename__ = 'usuarios'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    senha = Column(String, nullable=False)
    email = Column(String, nullable=False)
    data_nasc = Column(Date, nullable=False)
    cidade = Column(String, nullable=False)
    sexo = Column(String, nullable=False)

    # Relacionamento com Agendamento
    agendamentos = relationship('AgendamentoModel', back_populates='usuario', cascade="all, delete-orphan")


class AgendamentoModel(Base):
    __tablename__ = 'agendamentos'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    data = Column(Date, nullable=False)
    horario = Column(Time, nullable=False)
    local = Column(String, nullable=False)
    descricao = Column(String, nullable=True)
    
    # Chave estrangeira para Usuario
    usuario_id = Column(Integer, ForeignKey('usuarios.id', ondelete='CASCADE'), nullable=False)
    usuario = relationship('UsuarioModel', back_populates='agendamentos')
