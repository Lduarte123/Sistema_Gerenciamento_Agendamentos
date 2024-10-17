class AgendamentoModel:
    def __init__(self, id=None, nome='', data=None, horario=None, local='', descricao='', usuario_id=None):
        self.id = id
        self.nome = nome
        self.data = data
        self.horario = horario
        self.local = local
        self.descricao = descricao  # Atributo opcional
        self.usuario_id = usuario_id
