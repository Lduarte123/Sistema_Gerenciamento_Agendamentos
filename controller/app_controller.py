import customtkinter as ctk
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
from view.visualizar_user import VisualizarUsuariosFrame
from view.admin_view import AdminFrame
from view.admin_agendamentos import VisualizarAdminFrame
from services.emails import VerificacaoEmail
from view.redefinir_senha import RedefinirSenhaWindow  # Certifique-se de que a janela de redefinir senha está importada

constante = Constante()

class AppController:
    def __init__(self, root):
        self.root = root
        self.agendamento_model = AgendamentoModel()
        self.agendamento_repository = AgendamentoRepository()
        self.usuario_repo = UsuarioRepository()
        self.main_frame = None
        self.usuario_id = None
        self.usuario_tipo_admin = False
        self.verificacao_email = None  # Instância do serviço de verificação de e-mail
        self.exibir_tela_login()

    # Função de logout
    def logout(self):
        self.usuario_id = None  # Limpa o ID do usuário logado
        self.exibir_tela_login()  # Volta para a tela de login

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

    def registrar_usuario(self, nome, email, senha, data_nasc, cidade, sexo, tipo):
        return self.usuario_repo.registrar_usuario(nome, email, senha, data_nasc, cidade, sexo, tipo="padrão")

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

        if self.usuario_tipo_admin:
            self.main_frame = VisualizarAdminFrame(self.root, self.agendamento_repository, self.usuario_id)
        else:
            self.main_frame = VisualizarFrame(self.root, self.agendamento_repository, self.usuario_id, filtro=None)
            
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

    def abrir_listar_usuarios(self):
        """Abre a tela de visualização de todos os usuários"""
        if self.main_frame:
            self.main_frame.pack_forget()  # Remove o frame anterior

        # Paginação (por exemplo, página 1 e 20 itens por página)
        pagina = 1
        itens_por_pagina = 20

        # Obtém os usuários da primeira página
        usuarios = self.usuario_repo.listar_usuarios(pagina, itens_por_pagina)

        # Cria o frame para visualizar todos os usuários
        self.main_frame = VisualizarUsuariosFrame(self.root, self.usuario_repo, usuarios)
        self.main_frame.pack(fill="both", expand=True)

    def validar_login(self, username, senha):
        usuario = self.usuario_repo.validar_usuario(username, senha)
        if usuario:
            self.usuario_id = usuario.id
            self.usuario_tipo_admin = self.usuario_repo.checar_tipo(usuario.id)
        return usuario

    def exibir_tela_inicial(self):
        if self.main_frame:
            self.main_frame.pack_forget()

        if self.usuario_tipo_admin:
            self.main_frame = AdminFrame(self.root, self)
        else:
            self.main_frame = MainFrame(self.root, self)
        
        self.main_frame.pack(fill="both", expand=True)

    def obter_emails_cadastrados(self):
        return self.usuario_repo.obter_emails_cadastrados()
    
    def usuario_logado_email(self):
        usuario_id = self.usuario_id
        return self.usuario_repo.obter_usuario_logado_email(usuario_id)

    def obter_nome_usuario(self):
        if self.usuario_id is not None:
            usuario = self.usuario_repo.obter_usuario_por_id(self.usuario_id)
            if usuario:
                return usuario.nome
        return "Usuário"

    def iniciar_recuperacao_senha(self):
        """Inicia o processo de recuperação de senha"""
        email = self.obter_emails_cadastrados()  # Pode ser um método que retorna os emails cadastrados
        if email:
            self.verificacao_email = VerificacaoEmail(email)  # Instancia a classe de verificação de e-mail
            self.verificacao_email.solicitar_codigo_verificacao(self.root)  # Exibe a tela para inserir o código
        else:
            print("Email não encontrado")

    def validar_codigo_recuperacao_senha(self, codigo_inserido):
        """Valida o código de verificação enviado por e-mail"""
        if self.verificacao_email.validar_codigo(codigo_inserido):
            # Se o código for válido, abrir a tela de redefinição de senha
            self.abrir_tela_redefinir_senha()
        else:
            print("Código de verificação inválido")

    def abrir_tela_redefinir_senha(self):
        """Exibe a tela para redefinir a senha"""
        if self.main_frame:
            self.main_frame.pack_forget()

        self.main_frame = RedefinirSenhaWindow(self.root, "Recuperação de Senha", self.redefinir_senha)
        self.main_frame.pack(fill="both", expand=True)

    def redefinir_senha(self, nova_senha):
        """Redefine a senha do usuário após a validação do código"""
        if self.usuario_id:
            self.usuario_repo.atualizar_senha(self.usuario_id, nova_senha)
            print("Senha redefinida com sucesso!")
        else:
            print("Erro: ID do usuário não encontrado")
