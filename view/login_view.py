import customtkinter as ctk
from tkinter import messagebox
from services.emails import VerificacaoEmail
from util.constantes import Constante


constante = Constante()

class LoginView(ctk.CTkFrame):
    def __init__(self, root, controller):
        super().__init__(root)
        self.controller = controller

        # Criando o frame externo com uma cor de fundo diferente
        self.main_frame = ctk.CTkFrame(self, width=600, height=600, corner_radius=25)
        self.main_frame.pack(expand=True, padx=20, pady=20)  # Definir o tamanho do frame e espaçamento

        # Criando o título
        self.title_label = ctk.CTkLabel(self.main_frame, text="Olá, seja bem-vindo de volta!", font=(constante.get_fonte()))
        self.title_label.pack(pady=(20, 2))

        self.title_label = ctk.CTkLabel(self.main_frame, text="Ainda não possui uma conta? Registre-se agora!", font=("Helvetica", 10, "normal"))
        self.title_label.pack(pady=(1, 10))


        # Criando o frame para as entradas
        self.entry_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent", width=340, height=200)
        self.entry_frame.pack(pady=10)

        # Desabilitar redimensionamento do frame de entradas
        self.entry_frame.grid_propagate(False)

        # Adicionando o rótulo e a entrada de email
        self.username_label = ctk.CTkLabel(self.entry_frame, text="Email:", font=("Helvetica", 14, "bold"))
        self.username_label.grid(row=0, column=0, sticky='w', padx=22, pady=(10,5))

        self.username_entry = ctk.CTkEntry(self.entry_frame, placeholder_text="Seu Email", width=300, height=35)
        self.username_entry.grid(row=1, column=0, padx=17, pady=5)

        # Adicionando o rótulo e a entrada de senha
        self.password_label = ctk.CTkLabel(self.entry_frame, text="Senha:", font=("Helvetica", 14, "bold"))
        self.password_label.grid(row=2, column=0, sticky='w', padx=22, pady=5)

        self.password_entry = ctk.CTkEntry(self.entry_frame, placeholder_text="Senha", show="•", width=300, height=35)
        self.password_entry.grid(row=3, column=0, padx=17, pady=(5, 0))

        self.login_button = ctk.CTkButton(
            self.main_frame,
            text="Entrar",
            command=self.login,
            width=300,
            height=35,
            corner_radius=30,
            fg_color="white",        # Cor de fundo branca
            text_color="black",        # Cor do texto preto
            hover_color="#d3d3d3"
        )
        self.login_button.pack(pady=(0, 0))

        # Botão para registro de novo usuário
        self.register_button = ctk.CTkButton(
            self.main_frame,
            text="Registre-se",
            command=self.open_register,
            width=300,
            height=35,
            corner_radius=30,
            fg_color="white",        # Cor de fundo branca
            text_color="black",        # Cor do texto preto
            hover_color="#d3d3d3"
        )
        self.register_button.pack(pady=(10, 20))

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if self.controller.validar_login(username, password):
            self.verificacao_email = VerificacaoEmail(self.controller.usuario_logado_email())
            codigo_inserido = self.verificacao_email.solicitar_codigo_verificacao(self.master)
            if codigo_inserido is None or not self.verificacao_email.validar_codigo(codigo_inserido):
                messagebox.showerror(constante.get_erro(), "Código de verificação inválido.")
                return
            self.controller.exibir_tela_inicial()
            return
        messagebox.showerror(constante.get_erro(), "Credenciais Inválidas")

    def open_register(self):
        self.controller.exibir_tela_registro()
