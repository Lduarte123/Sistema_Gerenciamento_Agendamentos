import customtkinter as ctk
from PIL import Image, ImageTk
from datetime import datetime
from util.constantes import Constante

constante = Constante()

class AdminFrame(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master, fg_color="transparent")
        self.controller = controller
        self.grid(row=0, column=0, sticky="nsew")

        self.imagem_agendar = self.carregar_imagem("assets/image_c.png", (80, 80))
        self.imagem_visualizar = self.carregar_imagem("assets/image_v.png", (80, 80))
        self.imagem_perfil = self.carregar_imagem("assets/human.png", (80, 80))
        self.imagem_listar_todos = self.carregar_imagem("assets/listagem_todos.png", (80, 80))
        self.imagem_listar_user = self.carregar_imagem("assets/listar_user.png", (80, 80))


        self.container = ctk.CTkFrame(self, fg_color="transparent")
        self.container.pack(expand=True, fill="both")

        self.frame_superior = ctk.CTkFrame(
            self.container,
            fg_color="transparent",
            corner_radius=10,
            width=200,
            height=100
        )
        self.frame_superior.place(x=10, y=-20)
        self.label_relogio = ctk.CTkLabel(
            self.frame_superior,
            text="",
            font=(constante.get_fonte_relogio()),
            text_color="white",
            anchor="w"
        )
        self.label_relogio.place(x=10, rely=0.25)
        
        self.label_data = ctk.CTkLabel(
            self.frame_superior,
            text="",
            font=(constante.get_fonte_data()),
            text_color="white",
            anchor="w"
        )
        self.label_data.place(x=10, rely=0.55)

        self.atualizar_relogio()

        self.botao_frame = ctk.CTkFrame(
            self.container, 
            border_width=2,
            border_color="gray",
            fg_color="#1C1C1C", 
            corner_radius=10,
            width=500,
            height=500
        )
        self.botao_frame.pack(expand=True, padx=20, pady=20)

        self.titulo = ctk.CTkLabel(self.botao_frame, text=constante.get_titulo_gerenciamento(), font=(constante.get_fonte()))
        self.titulo.pack(pady=(10, 30))

        self.button_a = ctk.CTkButton(
            self.botao_frame, text="Agendar", image=self.imagem_agendar, compound="top",
            width=100, height=100, corner_radius=15, command=self.controller.abrir_criar_agendamento
        )
        self.button_a.pack(side="left", padx=20, pady=15)

        self.button_b = ctk.CTkButton(
            self.botao_frame, text="Agendamentos", image=self.imagem_listar_todos, compound="top",
            width=100, height=100, corner_radius=15, command=self.controller.abrir_visualizar_agendamento
        )
        self.button_b.pack(side="left", padx=20, pady=15)

        self.button_c = ctk.CTkButton(
            self.botao_frame, text="Perfil", image=self.imagem_perfil, compound="top",
            width=100, height=100, corner_radius=15, command=self.controller.abrir_visualizar_perfil
        )
        self.button_c.pack(side="left", padx=20, pady=15)

        self.button_d = ctk.CTkButton(
            self.botao_frame, text="Listar Usuários", image=self.imagem_listar_user, compound="top",
            width=100, height=100, corner_radius=15, command=self.controller.abrir_listar_usuarios
        )
        self.button_d.pack(side="left", padx=20, pady=15)

        self.botao_frame.pack(expand=True)

    def carregar_imagem(self, caminho, tamanho):
        imagem = Image.open(caminho)
        imagem = imagem.resize(tamanho)
        return ImageTk.PhotoImage(imagem)

    def atualizar_relogio(self):
        agora = datetime.now()
        hora_atual = agora.strftime("%H:%M:%S")
        data_atual = agora.strftime("%d/%m/%Y")
        
        self.label_relogio.configure(text=hora_atual)
        self.label_data.configure(text=data_atual)
        self.after(1000, self.atualizar_relogio)
