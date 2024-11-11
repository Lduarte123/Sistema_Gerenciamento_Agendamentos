import customtkinter as ctk
from tkinter import messagebox
from services.emails import VerificacaoEmail
from util.constantes import Constante
from services.emails import VerificacaoEmail
from view.redefinir_senha import RedefinirSenhaWindow

constante = Constante()

class LoginView(ctk.CTkFrame):
    def __init__(self, root, controller):
        super().__init__(root)
        self.controller = controller

        self.pack(expand=True)

        self.title_label = ctk.CTkLabel(self, text="Login", font=(constante.get_fonte()))
        self.title_label.pack(pady=(200, 70))

        self.entry_frame = ctk.CTkFrame(self, border_width=2, border_color="gray", fg_color="#1C1C1C", corner_radius=10, width=340, height=200)
        self.entry_frame.pack(pady=10)

        self.entry_frame.grid_propagate(False)

        self.username_label = ctk.CTkLabel(self.entry_frame, text="Email:", font=("Arial", 14, "bold"))
        self.username_label.grid(row=0, column=0, sticky='w', padx=22, pady=(10,5))

        self.username_entry = ctk.CTkEntry(self.entry_frame, placeholder_text="Digite seu email", width=300, height=40)
        self.username_entry.grid(row=1, column=0, padx=17, pady=5)

        self.password_label = ctk.CTkLabel(self.entry_frame, text="Senha:", font=("Arial", 14, "bold"))
        self.password_label.grid(row=2, column=0, sticky='w', padx=22, pady=5)

        self.password_entry = ctk.CTkEntry(self.entry_frame, placeholder_text="Digite sua senha", show="*", width=300, height=40)
        self.password_entry.grid(row=3, column=0, padx=17, pady=5)

        self.login_button = ctk.CTkButton(self, text="Entrar", command=self.login, width=300, height=40)
        self.login_button.pack(pady=(20, 5)) 

        self.register_button = ctk.CTkButton(self, text="Registrar Novo Usuário", command=self.open_register, width=300, height=40)
        self.register_button.pack(pady=10)

        self.forgot_password_label = ctk.CTkLabel(self, text="Esqueceu sua senha? Redefina", font=("Arial", 12, "underline"), fg_color="transparent", text_color="blue", cursor="hand2")
        self.forgot_password_label.pack(pady=10)
        self.forgot_password_label.bind("<Button-1>", self.abrir_redefinir_senha)  # Aqui estamos usando o bind para o evento de clique

    def abrir_redefinir_senha(self, event=None):  # Adiciona 'event' para capturar o argumento extra
        # Corrigido: Agora passamos o 'title' para a janela
        janela_redefinir = RedefinirSenhaWindow(self.master, title="Redefinir Senha")  # Passa o título corretamente
        janela_redefinir.grab_set()  # Mantém a janela de redefinir senha na frente da janela principal

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
