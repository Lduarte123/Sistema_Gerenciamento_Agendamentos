from view.criar_agendamento_view import CriarAgendamentoFrame
from view.visualizar_view import VisualizarFrame
from view.janela_principal_view import MainFrame
from view.login_view import LoginView
from view.registrar_view import RegisterView
from model.models import AgendamentoModel
from repository.agendamento_repository import AgendamentoRepository
from repository.usuario_repository import UsuarioRepository
from view.visualizar_perfil import VisualizarPerfilFrame
from util.constantes import Constante

constante = Constante()

class AppController:
    def __init__(self, root):
        self.root = root
        self.agendamento_model = AgendamentoModel()
        self.agendamento_repository = AgendamentoRepository() 
        self.usuario_repo = UsuarioRepository()
        self.main_frame = None
        self.usuario_id = None
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

        self.main_frame = MainFrame(self.root, self)
        self.main_frame.pack(fill="both", expand=True)

    def abrir_criar_agendamento(self):
        if self.main_frame:
            self.main_frame.pack_forget()

        self.main_frame = CriarAgendamentoFrame(self.root, self.agendamento_model, self, self.usuario_id)
        self.main_frame.pack(fill="both", expand=True)


    def abrir_visualizar_agendamento(self):
        if self.main_frame:
            self.main_frame.pack_forget()

        self.main_frame = VisualizarFrame(self.root, self.agendamento_repository, self.usuario_id)
        self.main_frame.pack(fill="both", expand=True)

    def abrir_visualizar_perfil(self):
        if self.main_frame:
            self.main_frame.pack_forget()

        if self.usuario_id is not None:
            usuario_info = self.usuario_repo.obter_usuario_por_id(self.usuario_id)
            if usuario_info:
                self.main_frame = VisualizarPerfilFrame(self.root, usuario_info)
                self.main_frame.pack(fill="both", expand=True)
            else:
                print(constante.get_erro_usuario_nao_encontrado())
        else:
            print(constante.get_erro_usuario_id_nao_definido())


            
    def validar_login(self, username, senha):
        usuario = self.usuario_repo.validar_usuario(username, senha)
        if usuario:
            self.usuario_id = usuario.id
        return usuario

    def exibir_tela_inicial(self):
        if self.main_frame:
            self.main_frame.pack_forget()

        self.main_frame = MainFrame(self.root, self)
        self.main_frame.pack(fill="both", expand=True)

    def obter_emails_cadastrados(self):
        return self.usuario_repo.obter_emails_cadastrados()
    
    def usuario_logado_email(self):
        usuario_id = self.usuario_id
        return self.usuario_repo.obter_usuario_logado_email(usuario_id)

