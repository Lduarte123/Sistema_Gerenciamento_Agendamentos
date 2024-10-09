class UsuarioModel:
    def __init__(self, id=None, nome="",senha="",email="", data_nasc=None, cidade="", sexo=""):
        self.id = id
        self.nome = nome
        self.senha = senha
        self.email = email
        self.data_nasc = data_nasc
        self.cidade = cidade
        self.sexo = sexo

usuario = UsuarioModel(
    nome=nome,
    email=usu,
    senha=senha,
    data_nasc=data_nasc,
    cidade=cidade,
    sexo=sexo)


# #  id = Column(Integer, primary_key=True, autoincrement=True)
#     nome = Column(String, nullable=False)
#     senha = Column(String, nullable=False)
#     email = Column(String, nullable=False)
#     data_nasc = Column(Date, nullable=False)
#     cidade = Column(String, nullable=False)
#     sexo = Column(String,  nullable=False)
