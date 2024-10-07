import customtkinter as ctk

class LoginView(ctk.CTkFrame):
    def __init__(self, root, controller):
        super().__init__(root)
        self.controller = controller

        # Configurações do frame
        self.pack(expand=True)  # Expande para centralizar o frame


        # Título do Login
        self.title_label = ctk.CTkLabel(self, text="Login", font=("Arial", 24, "bold"))
        self.title_label.pack(pady=(200, 70))

        
        self.entry_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.entry_frame.pack(pady=10)

        self.username_label = ctk.CTkLabel(self.entry_frame, text="Email:", font=("Arial", 14, "bold"))
        self.username_label.grid(row=0, column=0, sticky='w', padx=5)

        self.username_entry = ctk.CTkEntry(self.entry_frame, placeholder_text="Digite seu email", width=300, height=40)
        self.username_entry.grid(row=1, column=0, pady=5) 

        # Label e campo de entrada de senha
        self.password_label = ctk.CTkLabel(self.entry_frame, text="Senha:", font=("Arial", 14, "bold"))
        self.password_label.grid(row=2, column=0, sticky='w', padx=5)

        self.password_entry = ctk.CTkEntry(self.entry_frame, placeholder_text="Digite sua senha", show="*", width=300, height=40)
        self.password_entry.grid(row=3, column=0, pady=5)  # Campo de entrada abaixo da label

        # Botão de login
        self.login_button = ctk.CTkButton(self, text="Entrar", command=self.login, width=300, height=40)
        self.login_button.pack(pady=(20, 5))  # Margem vertical

        # Botão de registro
        self.register_button = ctk.CTkButton(self, text="Registrar Novo Usuário", command=self.open_register, width=300, height=40)
        self.register_button.pack(pady=10)  # Margem vertical

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if self.controller.validar_login(username, password):
            print("Login bem-sucedido")
            self.controller.exibir_tela_inicial()
        else:
            print("Usuário ou senha incorretos")

    def open_register(self):
        self.controller.exibir_tela_registro()
