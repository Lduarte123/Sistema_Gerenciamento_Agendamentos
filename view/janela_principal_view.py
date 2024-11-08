import customtkinter as ctk
from PIL import Image, ImageTk
from datetime import datetime
from util.constantes import Constante

constante = Constante()

class MainFrame(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master, fg_color="transparent")
        self.controller = controller
        self.grid(row=0, column=0, sticky="nsew")

        self.imagem_agendar = self.carregar_imagem("assets/image_c.png", (80, 80))
        self.imagem_visualizar = self.carregar_imagem("assets/image_v.png", (80, 80))
        self.imagem_perfil = self.carregar_imagem("assets/human.png", (80, 80))

        self.container = ctk.CTkFrame(self, fg_color="transparent")
        self.container.pack(expand=True, fill="both")

        # Frame superior para relógio, data e botão de logout
        self.frame_superior = ctk.CTkFrame(self.container, fg_color="transparent")
        self.frame_superior.pack(fill="x", padx=10, pady=10)

        # Sub-frame para relógio e data
        self.left_frame = ctk.CTkFrame(self.frame_superior, fg_color="transparent")
        self.left_frame.pack(side="left")

        # Relógio
        self.label_relogio = ctk.CTkLabel(
            self.left_frame,
            text="",
            font=(constante.get_fonte_relogio()),
            text_color="white",
            anchor="w"
        )
        self.label_relogio.pack(anchor="w")

        # Data
        self.label_data = ctk.CTkLabel(
            self.left_frame,
            text="",
            font=(constante.get_fonte_data()),
            text_color="white",
            anchor="w"
        )
        self.label_data.pack(anchor="w")

        # Atualiza o relógio e data
        self.atualizar_relogio()

        # Botão de Logout, alinhado à direita
        self.logout_button = ctk.CTkButton(
            self.frame_superior,
            text="Sair",
            command=self.controller.logout,
            width=70,
            height=30
        )
        self.logout_button.pack(side="right")

        # Frame do usuário - pode ser ajustado independentemente
        nome_usuario = self.controller.obter_nome_usuario()
        tamanho_texto = len(nome_usuario) * 10
        
        self.frame_usuario = ctk.CTkFrame(
            self.container,  # Mantém no container principal
            fg_color="#1a75ff",
            corner_radius=20,
            width=tamanho_texto + 40,
            height=40
        )
        # Adiciona o evento de clique ao frame
        self.frame_usuario.bind("<Button-1>", lambda e: self.controller.abrir_visualizar_perfil())
        self.frame_usuario.place(x=10, rely=0.99, anchor="sw")  # Alterado de 0.93 para 0.97

        # Força o frame a manter o tamanho definido
        self.frame_usuario.grid_propagate(False)
        self.frame_usuario.pack_propagate(False)

        self.label_usuario = ctk.CTkLabel(
            self.frame_usuario,
            text=nome_usuario,
            font=(constante.get_fonte_data()),
            text_color="white",
            anchor="center"
        )
        # Também adiciona o evento de clique à label do usuário
        self.label_usuario.bind("<Button-1>", lambda e: self.controller.abrir_visualizar_perfil())
        self.label_usuario.place(relx=0.5, rely=0.5, anchor="center")

        # Frame principal dos botões
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

        # Título do frame de gerenciamento
        self.titulo = ctk.CTkLabel(self.botao_frame, text=constante.get_titulo_gerenciamento(), font=(constante.get_fonte()))
        self.titulo.pack(pady=(10, 30))

        # Botões principais
        self.button_a = ctk.CTkButton(
            self.botao_frame, text="Agendar", image=self.imagem_agendar, compound="top",
            width=100, height=100, corner_radius=15, command=self.controller.abrir_criar_agendamento
        )
        self.button_a.pack(side="left", padx=20, pady=15)

        self.button_b = ctk.CTkButton(
            self.botao_frame, text="Visualizar", image=self.imagem_visualizar, compound="top",
            width=100, height=100, corner_radius=15, command=self.controller.abrir_visualizar_agendamento
        )
        self.button_b.pack(side="left", padx=20, pady=15)

        self.button_c = ctk.CTkButton(
            self.botao_frame, text="Perfil", image=self.imagem_perfil, compound="top",
            width=100, height=100, corner_radius=15, command=self.controller.abrir_visualizar_perfil
        )
        self.button_c.pack(side="left", padx=20, pady=15)

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


# fix