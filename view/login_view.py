import customtkinter as ctk
from tkinter import messagebox
from services.emails import VerificacaoEmail
from util.constantes import Constante
from PIL import Image  # Importando apenas o PIL.Image

constante = Constante()

class LoginView(ctk.CTkFrame):
    def __init__(self, root, controller):
        super().__init__(root)
        self.controller = controller

        # Criando o frame externo com uma cor de fundo diferente
        self.main_frame = ctk.CTkFrame(self, width=600, height=600, corner_radius=25)
        self.main_frame.pack(expand=True, padx=20, pady=20)  # Definir o tamanho do frame e espaçamento

        # Carregando a logo usando o PIL.Image
        logo_image = Image.open("assets/awj.png")  # Substitua pelo caminho correto da sua imagem
        logo_image = logo_image.resize((150, 150))  # Ajustando o tamanho da imagem

        # Usando o CTkImage diretamente com a imagem PIL
        self.logo_image = ctk.CTkImage(light_image=logo_image, size=(150, 150))
        
        # Exibindo a logo na parte superior do frame
        self.logo_label = ctk.CTkLabel(self.main_frame, image=self.logo_image, text="")
        self.logo_label.pack(pady=(20, 10))  # Logo no topo com espaçamento

        # Criando o título (Este será o título real da tela de login)
        self.title_label = ctk.CTkLabel(self.main_frame, text="Olá, seja bem-vindo de volta!", font=("Helvetica", 22, "bold"))
        self.title_label.pack(pady=(10, 2))

        # Criando o subtítulo (Agora atuando como um botão)
        self.sub_title_label = ctk.CTkLabel(self.main_frame, text="Ainda não possui uma conta? Registre-se agora!", font=("Helvetica", 12, "normal"))
        self.sub_title_label.pack(pady=(1, 10))

        # Adicionando o bind para o clique no subtítulo, redirecionando para o registro
        self.sub_title_label.bind("<Button-1>", self.open_register)

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

        # Adicionando o bind para o campo de email, pressionando Enter para login
        self.username_entry.bind("<Return>", self.handle_enter_key)

        # Adicionando o rótulo e a entrada de senha
        self.password_label = ctk.CTkLabel(self.entry_frame, text="Senha:", font=("Helvetica", 14, "bold"))
        self.password_label.grid(row=2, column=0, sticky='w', padx=22, pady=5)

        self.password_entry = ctk.CTkEntry(self.entry_frame, placeholder_text="Senha", show="•", width=300, height=35)
        self.password_entry.grid(row=3, column=0, padx=17, pady=(5, 0))

        # Adicionando o bind para o campo de senha, pressionando Enter para login
        self.password_entry.bind("<Return>", self.handle_enter_key)

        self.login_button = ctk.CTkButton(
            self.main_frame,
            text="Entrar",
            font=("Helvetica", 14, "bold"),
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
            font=("Helvetica", 14, "bold"),
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

    def open_register(self, event=None):
        """Redireciona para a tela de registro."""
        self.controller.exibir_tela_registro()

    def handle_enter_key(self, event):
        """Aciona o login quando a tecla Enter é pressionada."""
        self.login()
