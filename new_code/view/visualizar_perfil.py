import customtkinter as ctk
from datetime import datetime
import datetime as dt

class VisualizarPerfilFrame(ctk.CTkFrame):
    def __init__(self, master, usuario_info):
        super().__init__(master)

        # Frame principal estilizado com largura e altura aumentadas
        self.frame_principal = ctk.CTkFrame(self, border_width=2, corner_radius=10, fg_color="#1C1C1C", width=600, height=400)
        self.frame_principal.pack(pady=50, padx=50, anchor="center")  # Centraliza o frame
        self.frame_principal.pack_propagate(False)  # Desativa o ajuste automático de tamanho

        # Centralizando cada frame dentro do frame principal
        self.frame_nome = ctk.CTkFrame(self.frame_principal, fg_color="transparent")
        self.frame_nome.pack(pady=10)
        self.nome_label = ctk.CTkLabel(self.frame_nome, text="Nome:", font=ctk.CTkFont(size=16, weight="bold"))
        self.nome_label.pack(side="left", padx=5, pady=10)
        self.nome_value = ctk.CTkLabel(self.frame_nome, text=usuario_info.nome, font=ctk.CTkFont(size=16))
        self.nome_value.pack(side="left", padx=5)

        # Centralizando o frame de e-mail
        self.frame_email = ctk.CTkFrame(self.frame_principal, fg_color="transparent")
        self.frame_email.pack(pady=10)
        self.email_label = ctk.CTkLabel(self.frame_email, text="Email:", font=ctk.CTkFont(size=16, weight="bold"))
        self.email_label.pack(side="left", padx=5)
        self.email_value = ctk.CTkLabel(self.frame_email, text=usuario_info.email, font=ctk.CTkFont(size=16))
        self.email_value.pack(side="left", padx=5)

        # Centralizando o frame de cidade
        self.frame_cidade = ctk.CTkFrame(self.frame_principal, fg_color="transparent")
        self.frame_cidade.pack(pady=10)
        self.cidade_label = ctk.CTkLabel(self.frame_cidade, text="Cidade:", font=ctk.CTkFont(size=16, weight="bold"))
        self.cidade_label.pack(side="left", padx=5)
        self.cidade_value = ctk.CTkLabel(self.frame_cidade, text=usuario_info.cidade, font=ctk.CTkFont(size=16))
        self.cidade_value.pack(side="left", padx=5)

        # Centralizando o frame de sexo
        self.frame_sexo = ctk.CTkFrame(self.frame_principal, fg_color="transparent")
        self.frame_sexo.pack(pady=10)
        self.sexo_label = ctk.CTkLabel(self.frame_sexo, text="Sexo:", font=ctk.CTkFont(size=16, weight="bold"))
        self.sexo_label.pack(side="left", padx=5)
        self.sexo_value = ctk.CTkLabel(self.frame_sexo, text=usuario_info.sexo, font=ctk.CTkFont(size=16))
        self.sexo_value.pack(side="left", padx=5)

        # Centralizando o frame de idade
        self.frame_idade = ctk.CTkFrame(self.frame_principal, fg_color="transparent")
        self.frame_idade.pack(pady=10)
        self.idade_label = ctk.CTkLabel(self.frame_idade, text="Idade:", font=ctk.CTkFont(size=16, weight="bold"))
        self.idade_label.pack(side="left", padx=5)
        idade = self.calcular_idade(usuario_info.data_nasc)
        self.idade_value = ctk.CTkLabel(self.frame_idade, text=f"{idade}", font=ctk.CTkFont(size=16))
        self.idade_value.pack(side="left", padx=5)

        # Centralizando o frame de senha
        self.frame_senha = ctk.CTkFrame(self.frame_principal, fg_color="transparent")
        self.frame_senha.pack(pady=10)
        self.senha_label = ctk.CTkLabel(self.frame_senha, text="Senha:", font=ctk.CTkFont(size=16, weight="bold"))
        self.senha_label.pack(side="left", padx=5)
        
        self.senha_value = ctk.CTkEntry(self.frame_senha, show="*", font=ctk.CTkFont(size=16), width=200)
        self.senha_value.insert(0, usuario_info.senha)  # Insere a senha
        self.senha_value.configure(state="disabled")  # Desabilita edição
        self.senha_value.pack(side="left", padx=5)

        self.toggle_button = ctk.CTkButton(self.frame_senha, text="Mostrar", command=self.toggle_senha, width=80)
        self.toggle_button.pack(side="left", padx=5)

        # Centralizando o frame de botões
        self.frame_botoes = ctk.CTkFrame(self.frame_principal, fg_color="transparent")
        self.frame_botoes.pack(pady=30)
        self.botao_voltar = ctk.CTkButton(self.frame_botoes, text="Voltar", command=self.voltar, width=100)
        self.botao_voltar.pack(side="left", padx=(10, 10))
        self.botao_editar = ctk.CTkButton(self.frame_botoes, text="Editar", command=self.editar, width=100)
        self.botao_editar.pack(side="left", padx=(10, 10))

        # Variável para controlar o estado da senha (mostrar/esconder)
        self.senha_visivel = False

    def calcular_idade(self, data_nasc):
        """Calcula a idade a partir da data de nascimento."""
        if isinstance(data_nasc, dt.date):
            nascimento = data_nasc
        else:
            nascimento = datetime.strptime(data_nasc, "%d/%m/%Y")

        hoje = datetime.now().date()
        idade = hoje.year - nascimento.year - ((hoje.month, hoje.day) < (nascimento.month, nascimento.day))
        return idade

    def toggle_senha(self):
        """Alterna entre mostrar e esconder a senha."""
        if self.senha_visivel:
            self.senha_value.configure(show="*")
            self.toggle_button.configure(text="Mostrar")
        else:
            self.senha_value.configure(show="")
            self.toggle_button.configure(text="Esconder")
        self.senha_visivel = not self.senha_visivel

    def voltar(self):
        self.master.controller.exibir_tela_inicial()

    def editar(self):
        print("Botão de Editar clicado!")
