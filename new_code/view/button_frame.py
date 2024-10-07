import customtkinter as ctk
from PIL import Image, ImageTk

class ButtonFrame(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master, fg_color="transparent")
        self.controller = controller
        self.grid(row=0, column=0, sticky="nsew")

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

    def carregar_imagem(self, caminho, tamanho):
        imagem = Image.open(caminho)
        imagem = imagem.resize(tamanho)
        return ImageTk.PhotoImage(imagem)
