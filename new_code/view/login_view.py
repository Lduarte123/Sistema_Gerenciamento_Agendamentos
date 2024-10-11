import customtkinter as ctk


class LoginView(ctk.CTkFrame):
    def __init__(self, root, controller):
        super().__init__(root)
        self.controller = controller

        # Configurações do frame principal
        self.pack(expand=True)

        # Título do Login
        self.title_label = ctk.CTkLabel(self, text="Login", font=("Arial", 24, "bold"))
        self.title_label.pack(pady=(200, 70))

        # Frame para os campos de entrada (com borda e cantos arredondados)
        self.entry_frame = ctk.CTkFrame(self, border_width=2, border_color="gray", fg_color="#1C1C1C", corner_radius=10, width=340, height=200)
        self.entry_frame.pack(pady=10)

        self.entry_frame.grid_propagate(False)

        # Label e campo de entrada de email
        self.username_label = ctk.CTkLabel(self.entry_frame, text="Email:", font=("Arial", 14, "bold"))
        self.username_label.grid(row=0, column=0, sticky='w', padx=22, pady=(10,5))

        self.username_entry = ctk.CTkEntry(self.entry_frame, placeholder_text="Digite seu email", width=300, height=40)
        self.username_entry.grid(row=1, column=0, padx=17, pady=5)

        # Label e campo de entrada de senha
        self.password_label = ctk.CTkLabel(self.entry_frame, text="Senha:", font=("Arial", 14, "bold"))
        self.password_label.grid(row=2, column=0, sticky='w', padx=22, pady=5)

        self.password_entry = ctk.CTkEntry(self.entry_frame, placeholder_text="Digite sua senha", show="*", width=300, height=40)
        self.password_entry.grid(row=3, column=0, padx=17, pady=5)

        # Botão de login
        self.login_button = ctk.CTkButton(self, text="Entrar", command=self.login, width=300, height=40)
        self.login_button.pack(pady=(20, 5))  # Margem vertical

        # Botão de registro
        self.register_button = ctk.CTkButton(self, text="Registrar Novo Usuário", command=self.open_register, width=300, height=40)
        self.register_button.pack(pady=10)

    def login(self):
        email = self.username_entry.get()  # Alterado de username para email
        password = self.password_entry.get()

        usuario = self.controller.validar_login(email, password)  # Modificado para retornar o objeto do usuário

        if usuario:
            print("Login bem-sucedido")
            self.controller.exibir_tela_inicial(usuario)  # Passa o objeto do usuário para a tela inicial
        else:
            print("Usuário ou senha incorretos")
    def open_register(self):
        self.controller.exibir_tela_registro()
