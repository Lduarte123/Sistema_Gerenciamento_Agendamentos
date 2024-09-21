import customtkinter as ctk

class AppController:
    def __init__(self, root):
        self.root = root
        self.janelaPrincipal()

    def janelaPrincipal(self):
        # Define as propriedades da janela principal
        self.root.title("Sistema de Agendamento")
        self.root.geometry("800x600")


# ALTH CAUA
        # Centraliza os botões
        button_frame = ctk.CTkFrame(self.root)
        button_frame.pack(pady=50)

        # Botão A
        button_a = ctk.CTkButton(button_frame, text="A", width=100, height=100, corner_radius=15)
        button_a.grid(row=0, column=0, padx=20)

        # Botão B
        button_b = ctk.CTkButton(button_frame, text="B", width=100, height=100, corner_radius=15)
        button_b.grid(row=0, column=1, padx=20)

        # Botão C
        button_c = ctk.CTkButton(button_frame, text="C", width=100, height=100, corner_radius=15)
        button_c.grid(row=0, column=2, padx=20)
# l