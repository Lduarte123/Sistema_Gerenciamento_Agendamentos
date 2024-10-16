import customtkinter as ctk
from datetime import datetime  # Importa datetime corretamente
import datetime as dt  # Para acessar datetime.date

class VisualizarPerfilFrame(ctk.CTkFrame):
    def __init__(self, master, usuario_info):
        super().__init__(master)

        # Frame principal estilizado com largura aumentada
        self.frame_principal = ctk.CTkFrame(self, border_width=2, corner_radius=10, fg_color="#1C1C1C", width=400)  # Ajuste a largura aqui
        self.frame_principal.pack(pady=50, padx=700, fill=None, expand=False)  # Ajuste de preenchimento e expansão

        # Label de nome
        self.nome_value = ctk.CTkLabel(self.frame_principal, text=usuario_info.nome, font=ctk.CTkFont(size=24, weight="bold"))
        self.nome_value.pack(pady=15)

        # Label de e-mail
        self.email_value = ctk.CTkLabel(self.frame_principal, text=usuario_info.email, font=ctk.CTkFont(size=20))
        self.email_value.pack(pady=15)

        # Label de sexo
        self.sexo_value = ctk.CTkLabel(self.frame_principal, text=usuario_info.sexo, font=ctk.CTkFont(size=20))
        self.sexo_value.pack(pady=15)

        # Cálculo da idade
        idade = self.calcular_idade(usuario_info.data_nasc)  # A data de nascimento é esperada como objeto datetime.date
        self.idade_value = ctk.CTkLabel(self.frame_principal, text=f"Idade: {idade}", font=ctk.CTkFont(size=20))
        self.idade_value.pack(pady=15)

        # Frame para os botões
        self.frame_botoes = ctk.CTkFrame(self.frame_principal, fg_color="transparent")  # Cor de fundo para o frame dos botões
        self.frame_botoes.pack(pady=10)

        # Botão de Voltar
        self.botao_voltar = ctk.CTkButton(self.frame_botoes, text="Voltar", command=self.voltar, width=100)
        self.botao_voltar.pack(side="left", padx=(4,4))

        # Botão de Editar
        self.botao_editar = ctk.CTkButton(self.frame_botoes, text="Editar", command=self.editar, width=100)
        self.botao_editar.pack(side="left", padx=(4,4))

    def calcular_idade(self, data_nasc):
        """Calcula a idade a partir da data de nascimento."""
        # Verifique se data_nasc é um objeto datetime.date
        if isinstance(data_nasc, dt.date):  # Corrigido para datetime.date
            nascimento = data_nasc
        else:
            # Se for uma string, converta-a
            nascimento = datetime.strptime(data_nasc, "%d/%m/%Y")

        hoje = datetime.now().date()  # Obtém a data atual
        idade = hoje.year - nascimento.year - ((hoje.month, hoje.day) < (nascimento.month, nascimento.day))
        return idade

    def voltar(self):
        self.master.controller.exibir_tela_inicial()  # Método para voltar à tela anterior

    def editar(self):
        # Defina o que acontece ao clicar no botão de editar
        print("Botão de Editar clicado!")  # Exemplo de ação
