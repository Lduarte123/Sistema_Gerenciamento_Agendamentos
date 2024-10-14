# controller/app_controller.py

from view.criar_agendamento_view import CriarAgendamentoFrame
from view.visualizar_view import VisualizarFrame
from view.button_frame import ButtonFrame  # Importa a tela de visualização de perfil
from view.login_view import LoginView
from view.registrar_view import RegisterView  # Importa a nova tela de registro
from model.agendamento import AgendamentoModel
from repository.agendamento_repository import AgendamentoRepository
from repository.usuario_repository import UsuarioRepository
from view.visualizar_perfil import VisualizarPerfilFrame

class AppController:
    def __init__(self, root):
        self.root = root
        self.agendamento_model = AgendamentoModel()
        self.agendamento_repository = AgendamentoRepository() 
        self.usuario_repo = UsuarioRepository()
        self.main_frame = None
        self.usuario_id = None  # Adicione esta linha para armazenar o ID do usuário logado
        self.exibir_tela_login()

    def exibir_tela_login(self):
        if self.main_frame:
            self.main_frame.pack_forget()

        self.main_frame = LoginView(self.root, self)
        self.main_frame.pack(fill="both", expand=True)

    def exibir_tela_registro(self):
        if self.main_frame:
            self.main_frame.pack_forget()

        self.main_frame = RegisterView(self.root, self)
        self.main_frame.pack(fill="both", expand=True)

    def registrar_usuario(self, nome, email, senha, data_nasc, cidade, sexo):
        return self.usuario_repo.registrar_usuario(nome, email, senha, data_nasc, cidade, sexo)

    def abrir_tela_principal(self):
        if self.main_frame:
            self.main_frame.pack_forget()

        from view.button_frame import ButtonFrame
        self.main_frame = ButtonFrame(self.root, self)
        self.main_frame.pack(fill="both", expand=True)

    def abrir_criar_agendamento(self):
        if self.main_frame:
            self.main_frame.pack_forget()

        self.main_frame = CriarAgendamentoFrame(self.root, self.agendamento_model, self)
        self.main_frame.pack(fill="both", expand=True)

    def abrir_visualizar_agendamento(self):
        if self.main_frame:
            self.main_frame.pack_forget()

        self.main_frame = VisualizarFrame(self.root, self.agendamento_repository)
        self.main_frame.pack(fill="both", expand=True)

    def abrir_visualizar_perfil(self):
        if self.main_frame:
            self.main_frame.pack_forget()

        if self.usuario_id is not None:  # Verifica se o usuario_id está definido
            self.main_frame = VisualizarPerfilFrame(self.root, self.agendamento_repository, self.usuario_id)  # Ajuste para passar o usuario_id
            self.main_frame.pack(fill="both", expand=True)
        else:
            # Lidar com o caso em que o usuario_id não está definido
            print("Erro: usuario_id não está definido.")

    def validar_login(self, username, senha):
        # Aqui você pode definir o usuario_id após validar o login
        usuario = self.usuario_repo.validar_usuario(username, senha)
        if usuario:
            self.usuario_id = usuario.id  # Supondo que usuario.id retorna o ID do usuário
        return usuario

    def exibir_tela_inicial(self):
        if self.main_frame:
            self.main_frame.pack_forget()

        from view.button_frame import ButtonFrame
        self.main_frame = ButtonFrame(self.root, self)
        self.main_frame.pack(fill="both", expand=True)

    def obter_emails_cadastrados(self):
        """Obtém todos os e-mails cadastrados no banco de dados."""
        return self.usuario_repo.obter_emails_cadastrados()
