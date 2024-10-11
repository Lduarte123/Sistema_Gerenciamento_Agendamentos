import customtkinter as ctk
from PIL import Image, ImageTk
from datetime import date

class ButtonFrame(ctk.CTkFrame):
    def __init__(self, master, controller, usuario):
        super().__init__(master, fg_color="transparent")
        self.controller = controller
        self.usuario = usuario  # Armazena o objeto do usuário
        self.grid(row=0, column=0, sticky="nsew")
        self.exibir_informacoes_usuario()  # Chama para exibir as informações do usuário

        # Carrega as imagens
        self.imagem_agendar = self.carregar_imagem("new_code/assets/image_c.png", (80, 80))
        self.imagem_visualizar = self.carregar_imagem("new_code/assets/image_v.png", (80, 80))

        self.botao_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.botao_frame.grid(row=0, column=0, padx=20, pady=20)

        self.titulo = ctk.CTkLabel(self.botao_frame, text="Gerenciamento de Agendamentos", font=("Arial", 20, "bold"))
        self.titulo.pack(pady=(10, 50))

        self.button_a = ctk.CTkButton(
            self.botao_frame, text="Agendar", image=self.imagem_agendar, compound="top",
            width=100, height=100, corner_radius=15, command=self.controller.abrir_criar_agendamento
        )
        self.button_a.pack(side="left", padx=30, pady=0)
        
        self.button_b = ctk.CTkButton(
            self.botao_frame, text="Visualizar", image=self.imagem_visualizar, compound="top",
            width=100, height=100, corner_radius=15, command=self.controller.abrir_visualizar_agendamento
        )
        self.button_b.pack(side="left", padx=5, pady=0)

        self.botao_frame.pack(expand=True)

    def exibir_informacoes_usuario(self):
        # Título
        titulo_label = ctk.CTkLabel(self, text="Informações do Usuário", font=("Arial", 24, "bold"), text_color="white")
        titulo_label.pack(pady=10)

        # Nome
        nome_label = ctk.CTkLabel(self, text=f"Nome: {self.usuario.nome}", text_color="white")
        nome_label.pack(pady=(5, 0))

        # Idade
        idade_label = ctk.CTkLabel(self, text=f"Idade: {self.calcular_idade(self.usuario.data_nasc)} anos", text_color="white")
        idade_label.pack(pady=(5, 0))

        # E-mail
        email_label = ctk.CTkLabel(self, text=f"E-mail: {self.usuario.email}", text_color="white")
        email_label.pack(pady=(5, 0))

        # Cidade
        cidade_label = ctk.CTkLabel(self, text=f"Cidade: {self.usuario.cidade}", text_color="white")
        cidade_label.pack(pady=(5, 0))

        # Sexo
        sexo_label = ctk.CTkLabel(self, text=f"Sexo: {self.usuario.sexo}", text_color="white")
        sexo_label.pack(pady=(5, 0))

    def carregar_imagem(self, caminho, tamanho):
        imagem = Image.open(caminho)
        imagem = imagem.resize(tamanho)
        return ImageTk.PhotoImage(imagem)
    
    def calcular_idade(self, data_nasc):
        hoje = date.today()  # Obtém a data atual
        idade = hoje.year - data_nasc.year - ((hoje.month, hoje.day) < (data_nasc.month, data_nasc.day))
        return idade
