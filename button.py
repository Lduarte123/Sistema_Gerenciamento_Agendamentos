import customtkinter as ctk
from PIL import Image, ImageTk 

class ButtonFrame:
    def __init__(self, master):
        self.master = master
        self.frame = ctk.CTkFrame(self.master, fg_color="transparent")
        self.frame.pack(pady=50)
        self.frame.pack_propagate(False)  # Impede que o frame ajuste seu tamanho automaticamente

        # Carrega as imagens
        self.imagem_agendar = self.carregar_imagem("assets/image_c.png", (80, 80))
        self.imagem_visualizar = self.carregar_imagem("assets/image_v.png", (80, 80))
        self.imagem_cancelar = self.carregar_imagem("assets/image_x.png", (80, 80))

        # Botão Agendar com imagem
        self.button_a = ctk.CTkButton(
            self.frame, 
            text="Agendar", 
            image=self.imagem_agendar, 
            compound="top",  
            width=120, 
            height=120, 
            corner_radius=15, 
            command=self.action_a
        )
        self.button_a.grid(row=0, column=0, padx=20)

        # Botão Visualizar com imagem
        self.button_b = ctk.CTkButton(
            self.frame, 
            text="Visualizar", 
            image=self.imagem_visualizar, 
            compound="top", 
            width=120, 
            height=120, 
            corner_radius=15, 
            command=self.action_b
        )
        self.button_b.grid(row=0, column=1, padx=20)


    def carregar_imagem(self, caminho, tamanho):
        """Carrega e redimensiona a imagem."""
        imagem = Image.open(caminho)  # Carrega a imagem
        imagem = imagem.resize(tamanho)  # Redimensiona a imagem
        return ImageTk.PhotoImage(imagem)  # Retorna a imagem no formato correto
    
    def action_a():
        print("Botão Agendar pressionado")
    
    def action_b():
        print("Botão Visualizar pressionado")


        



