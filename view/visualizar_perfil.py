import customtkinter as ctk
from datetime import datetime
import datetime as dt
from repository.usuario_repository import UsuarioRepository

class VisualizarPerfilFrame(ctk.CTkFrame):
    def __init__(self, master, usuario_info):
        super().__init__(master)
        self.usuario_info = usuario_info

        self.frame_principal = ctk.CTkFrame(self, border_width=2, corner_radius=10, fg_color="#1C1C1C", width=600, height=400)
        self.frame_principal.pack(pady=50, padx=50, anchor="center")
        self.frame_principal.pack_propagate(False)

        self.frame_nome = ctk.CTkFrame(self.frame_principal, fg_color="transparent")
        self.frame_nome.pack(pady=10)
        self.nome_label = ctk.CTkLabel(self.frame_nome, text="Nome:", font=ctk.CTkFont(size=16, weight="bold"))
        self.nome_label.pack(side="left", padx=5, pady=10)
        self.nome_value = ctk.CTkLabel(self.frame_nome, text=usuario_info.nome, font=ctk.CTkFont(size=16))
        self.nome_value.pack(side="left", padx=5)

        self.frame_email = ctk.CTkFrame(self.frame_principal, fg_color="transparent")
        self.frame_email.pack(pady=10)
        self.email_label = ctk.CTkLabel(self.frame_email, text="Email:", font=ctk.CTkFont(size=16, weight="bold"))
        self.email_label.pack(side="left", padx=5)
        self.email_value = ctk.CTkLabel(self.frame_email, text=usuario_info.email, font=ctk.CTkFont(size=16))
        self.email_value.pack(side="left", padx=5)

        self.frame_cidade = ctk.CTkFrame(self.frame_principal, fg_color="transparent")
        self.frame_cidade.pack(pady=10)
        self.cidade_label = ctk.CTkLabel(self.frame_cidade, text="Cidade:", font=ctk.CTkFont(size=16, weight="bold"))
        self.cidade_label.pack(side="left", padx=5)
        self.cidade_value = ctk.CTkLabel(self.frame_cidade, text=usuario_info.cidade, font=ctk.CTkFont(size=16))
        self.cidade_value.pack(side="left", padx=5)

        self.frame_sexo = ctk.CTkFrame(self.frame_principal, fg_color="transparent")
        self.frame_sexo.pack(pady=10)
        self.sexo_label = ctk.CTkLabel(self.frame_sexo, text="Sexo:", font=ctk.CTkFont(size=16, weight="bold"))
        self.sexo_label.pack(side="left", padx=5)
        self.sexo_value = ctk.CTkLabel(self.frame_sexo, text=usuario_info.sexo, font=ctk.CTkFont(size=16))
        self.sexo_value.pack(side="left", padx=5)

        self.frame_idade = ctk.CTkFrame(self.frame_principal, fg_color="transparent")
        self.frame_idade.pack(pady=10)
        self.idade_label = ctk.CTkLabel(self.frame_idade, text="Idade:", font=ctk.CTkFont(size=16, weight="bold"))
        self.idade_label.pack(side="left", padx=5)
        idade = self.calcular_idade(usuario_info.data_nasc)
        self.idade_value = ctk.CTkLabel(self.frame_idade, text=f"{idade}", font=ctk.CTkFont(size=16))
        self.idade_value.pack(side="left", padx=5)

        self.frame_senha = ctk.CTkFrame(self.frame_principal, fg_color="transparent")
        self.frame_senha.pack(pady=10)
        self.senha_label = ctk.CTkLabel(self.frame_senha, text="Senha:", font=ctk.CTkFont(size=16, weight="bold"))
        self.senha_label.pack(side="left", padx=5)
        
        self.senha_value = ctk.CTkEntry(self.frame_senha, show="*", font=ctk.CTkFont(size=16), width=200)
        self.senha_value.insert(0, usuario_info.senha)
        self.senha_value.configure(state="disabled") 
        self.senha_value.pack(side="left", padx=5)

        self.toggle_button = ctk.CTkButton(self.frame_senha, text="Mostrar", command=self.toggle_senha, width=80)
        self.toggle_button.pack(side="left", padx=5)

        self.frame_botoes = ctk.CTkFrame(self.frame_principal, fg_color="transparent")
        self.frame_botoes.pack(pady=30)
        self.botao_voltar = ctk.CTkButton(self.frame_botoes, text="Voltar", command=self.voltar, width=100)
        self.botao_voltar.pack(side="left", padx=(10, 10))
        self.botao_editar = ctk.CTkButton(self.frame_botoes, text="Editar", command=self.abrir_janela_edicao, width=100)
        self.botao_editar.pack(side="left", padx=(10, 10))

        self.senha_visivel = False

    def calcular_idade(self, data_nasc):
        if isinstance(data_nasc, dt.date):
            nascimento = data_nasc
        else:
            nascimento = datetime.strptime(data_nasc, "%d/%m/%Y")

        hoje = datetime.now().date()
        idade = hoje.year - nascimento.year - ((hoje.month, hoje.day) < (nascimento.month, nascimento.day))
        return idade

    def toggle_senha(self):
        if self.senha_visivel:
            self.senha_value.configure(show="*")
            self.toggle_button.configure(text="Mostrar")
        else:
            self.senha_value.configure(show="")
            self.toggle_button.configure(text="Esconder")
        self.senha_visivel = not self.senha_visivel

    def voltar(self):
        self.master.controller.exibir_tela_inicial()

    def abrir_janela_edicao(self):
        janela_edicao = ctk.CTkToplevel(self)
        janela_edicao.title("Editar Perfil")

        nome_label = ctk.CTkLabel(janela_edicao, text="Nome:", font=ctk.CTkFont(size=16, weight="bold"))
        nome_label.pack(pady=(10, 0))
        nome_entry = ctk.CTkEntry(janela_edicao, width=150)
        nome_entry.insert(0, self.usuario_info.nome)
        nome_entry.pack(pady=10)

        email_label = ctk.CTkLabel(janela_edicao, text="E-mail:", font=ctk.CTkFont(size=16, weight="bold"))
        email_label.pack(pady=(10, 0))
        email_entry = ctk.CTkEntry(janela_edicao, width=150)
        email_entry.insert(0, self.usuario_info.email)
        email_entry.pack(pady=10)

        cidade_label = ctk.CTkLabel(janela_edicao, text="Cidade:", font=ctk.CTkFont(size=16, weight="bold"))
        cidade_label.pack(pady=(10, 0))
        cidade_entry = ctk.CTkEntry(janela_edicao, width=150)
        cidade_entry.insert(0, self.usuario_info.cidade)
        cidade_entry.pack(pady=10)

        genero_label = ctk.CTkLabel(janela_edicao, text="Gênero:", font=ctk.CTkFont(size=16, weight="bold"))
        genero_label.pack(pady=(10, 0))
        frame_sexo = ctk.CTkFrame(janela_edicao, fg_color="transparent")
        frame_sexo.pack(pady=10)

        genero_var = ctk.StringVar(value=self.usuario_info.sexo)
        masculino_radio = ctk.CTkRadioButton(frame_sexo, text="Masculino", variable=genero_var, value="Masculino")
        masculino_radio.pack(side="left", padx=10)

        feminino_radio = ctk.CTkRadioButton(frame_sexo, text="Feminino", variable=genero_var, value="Feminino")
        feminino_radio.pack(side="left", padx=10)

        senha_label = ctk.CTkLabel(janela_edicao, text="Senha:", font=ctk.CTkFont(size=16, weight="bold"))
        senha_label.pack(pady=(10, 0))
        senha_entry = ctk.CTkEntry(janela_edicao, show="*", width=150)
        senha_entry.insert(0, self.usuario_info.senha)
        senha_entry.pack(pady=10)

        botao_confirmar = ctk.CTkButton(janela_edicao, text="Salvar", command=lambda: self.salvar_edicao(
            nome_entry, email_entry, cidade_entry, genero_var, senha_entry, janela_edicao
        ))
        botao_confirmar.pack(pady=10)

    def salvar_edicao(self, nome_entry, email_entry, cidade_entry, genero_var, senha_entry, janela_edicao):
        self.usuario_info.nome = nome_entry.get()
        self.usuario_info.email = email_entry.get()
        self.usuario_info.cidade = cidade_entry.get()
        self.usuario_info.sexo = genero_var.get()
        self.usuario_info.senha = senha_entry.get()

        usuario_repository = UsuarioRepository()
        sucesso = usuario_repository.atualizar_usuario(
            usuario_id=self.usuario_info.id,
            nome=self.usuario_info.nome,
            email=self.usuario_info.email,
            cidade=self.usuario_info.cidade,
            sexo=self.usuario_info.sexo,
            senha=self.usuario_info.senha
        )

        if sucesso:
            print("Usuário atualizado com sucesso.")
        else:
            print("Erro ao atualizar usuário.")

        self.nome_value.configure(text=self.usuario_info.nome)
        self.email_value.configure(text=self.usuario_info.email)
        self.cidade_value.configure(text=self.usuario_info.cidade)
        self.sexo_value.configure(text=self.usuario_info.sexo)
        self.senha_value.configure(state="normal")
        self.senha_value.delete(0, 'end')
        self.senha_value.insert(0, self.usuario_info.senha)
        self.senha_value.configure(state="disabled")

        janela_edicao.destroy()



