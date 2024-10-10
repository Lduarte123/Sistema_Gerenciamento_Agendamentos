import customtkinter as ctk

class Navbar(ctk.CTkFrame):
    def __init__(self, master, abrir_criar, abrir_visualizar):
        super().__init__(master, fg_color="#000000")
        self.grid(row=0, column=0, sticky="ew", padx=0, pady=0)

        # Título da Navbar
        self.titulo = ctk.CTkLabel(self, text="Gerenciamento de Agendamentos", font=("Arial", 20, "bold"), text_color="white")
        self.titulo.pack(pady=10)

        # Botões da Navbar
        self.button_a = ctk.CTkButton(
            self, text="Agendar", width=100, corner_radius=15,
            command=abrir_criar
        )
        self.button_a.pack(side="left", padx=(20, 5), pady=10)

        self.button_b = ctk.CTkButton(
            self, text="Visualizar", width=100, corner_radius=15,
            command=abrir_visualizar
        )
        self.button_b.pack(side="left", padx=5, pady=10)

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("App de Agendamentos")

        # Cria a barra de navegação
        self.navbar = Navbar(self, self.abrir_criar_agendamento, self.abrir_visualizar_agendamento)

        # Frame abaixo da Navbar
        self.frame_vertical = ctk.CTkFrame(self, fg_color="#f0f0f0")
        self.frame_vertical.grid(row=1, column=0, sticky="ew", padx=10, pady=10)

        # Ajusta a altura do frame para cerca de 25% da altura da tela
        self.geometry(f"{self.winfo_screenwidth()}x{int(self.winfo_screenheight() * 0.75)}")

        # Exemplo de conteúdo no frame vertical
        self.label = ctk.CTkLabel(self.frame_vertical, text="Conteúdo Vertical", font=("Arial", 16))
        self.label.pack(pady=20)

        # Seção "Adicione os Usuários" no canto inferior esquerdo
        self.adicionar_usuarios = ctk.CTkLabel(self.frame_vertical, text="Adicione os Usuários", font=("Arial", 14))
        self.adicionar_usuarios.pack(side="bottom", anchor="sw", padx=10, pady=10)

        # Configura o layout da janela
        self.grid_rowconfigure(0, weight=0)  # Navbar não se expande
        self.grid_rowconfigure(1, weight=1)  # Frame vertical se expande
        self.grid_columnconfigure(0, weight=1)  # Frame se expande

    def abrir_criar_agendamento(self):
        # Implementação do método para abrir a tela de agendamento
        print("Abrir criação de agendamento")
 
    def abrir_visualizar_agendamento(self):
        # Implementação do método para abrir a tela de visualização
        print("Abrir visualização de agendamentos")

# Exemplo de uso da aplicação
if __name__ == "__main__":
    app = App()
    app.mainloop()
