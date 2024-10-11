# controller/app_controller.py

from view.criar_agendamento_view import CriarAgendamentoFrame
from view.visualizar_view import VisualizarFrame
from view.login_view import LoginView
from view.registrar_view import RegisterView  # Importa a nova tela de registro
from model.agendamento import AgendamentoModel
from repository.agendamento_repository import AgendamentoRepository
from repository.usuario_repository import UsuarioRepository
from view.button_frame import  ButtonFrame


class AppController:
    def __init__(self, root):
        self.root = root
        self.agendamento_model = AgendamentoModel()
        self.agendamento_repository = AgendamentoRepository() 
        self.usuario_repo = UsuarioRepository()
        self.main_frame = None
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

    def validar_login(self, username, senha):
        return self.usuario_repo.validar_usuario(username, senha)

    def exibir_tela_inicial(self, usuario):
        if self.main_frame:
            self.main_frame.pack_forget()

        self.main_frame = ButtonFrame(self.root, self, usuario)  # Passe o objeto do usuário
        self.main_frame.pack(fill="both", expand=True)

    def obter_emails_cadastrados(self):
        """Obtém todos os e-mails cadastrados no banco de dados."""
        return self.usuario_repo.obter_emails_cadastrados()
    
    def exibir_informacoes_usuario(self, usuario_id):
        usuario = self.usuario_repo.obter_usuario_por_id(usuario_id)
        if usuario:
            ButtonFrame(self.master, self, usuario)  # Passa o objeto do usuário
        else:
            print("Usuário não encontrado.")
