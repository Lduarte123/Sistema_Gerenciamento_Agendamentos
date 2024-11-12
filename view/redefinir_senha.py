import customtkinter as ctk
from services.emails import VerificacaoEmail
from tkinter import messagebox
from repository.usuario_repository import UsuarioRepository

class RedefinirSenhaWindow(ctk.CTkToplevel):
    def __init__(self, master, title):
        super().__init__(master)
        self.title(title)
        self.geometry("350x200")  # Tamanho maior para as telas posteriores
        self.resizable(False, False)

        # Centralizar a janela
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width // 2) - (350 // 2)
        y = (screen_height // 2) - (200 // 2)
        self.geometry(f"350x200+{x}+{y}")  # Centraliza a nova janela

        # Inicializar variáveis
        self.email_usuario = None
        self.verificacao_email = None

        # Primeira tela: Solicitar E-mail
        self.label = ctk.CTkLabel(self, text="Digite seu e-mail:", font=("Arial", 16, "bold"))
        self.label.pack(pady=(20, 9))

        self.email_entry = ctk.CTkEntry(self, placeholder_text="E-mail", width=200)
        self.email_entry.pack(pady=(5, 15))

        # Frame de botões para a primeira tela
        self.button_frame = ctk.CTkFrame(self)
        self.button_frame.pack(pady=(10, 10))

        self.ok_button = ctk.CTkButton(self.button_frame, text="OK", command=self.enviar_codigo, width=95)
        self.ok_button.pack(side="left", padx=5)

        self.cancel_button = ctk.CTkButton(self.button_frame, text="Cancelar", command=self.on_cancel, width=95)
        self.cancel_button.pack(side="left", padx=5)

    def enviar_codigo(self):
        email = self.email_entry.get()
        if email:
            # Armazenando o e-mail fornecido
            self.email_usuario = email

            # Cria o objeto de Verificação e envia o código
            self.verificacao_email = VerificacaoEmail(self.email_usuario)
            codigo = self.verificacao_email.gerar_codigo()
            self.verificacao_email.enviar_email()

            # Atualiza a interface para a tela de código
            self.atualizar_tela_validacao_codigo()

        else:
            messagebox.showerror("Erro", "Por favor, insira um e-mail válido.")

    def atualizar_tela_validacao_codigo(self):
        # Atualiza a interface para permitir a inserção do código de verificação
        self.label.configure(text="Digite o código enviado para o e-mail:")
        self.email_entry.destroy()  # Remove o campo de e-mail

        # Cria o campo para inserir o código
        self.codigo_entry = ctk.CTkEntry(self, placeholder_text="Digite o código", width=200)
        self.codigo_entry.pack(pady=(5, 10))

        # Remove o Frame de botões da tela anterior
        self.button_frame.destroy()

        # Cria um novo Frame para os botões da tela de código, com fundo transparente
        self.button_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.button_frame.pack(pady=(10, 10))

        # Botões da tela de código (de forma horizontal)
        self.ok_button = ctk.CTkButton(self.button_frame, text="Validar Código", command=self.validar_codigo, width=95)
        self.ok_button.pack(side="left", padx=5)

        self.cancel_button = ctk.CTkButton(self.button_frame, text="Cancelar", command=self.on_cancel, width=95)
        self.cancel_button.pack(side="left", padx=5)

    def validar_codigo(self):
        codigo_inserido = self.codigo_entry.get()
        if codigo_inserido:
            # Verifica se o código inserido é válido
            if self.verificacao_email.validar_codigo(codigo_inserido):
                self.redefinir_senha()  # Código válido, permite redefinir a senha
            else:
                messagebox.showerror("Erro", "Código inválido. Tente novamente.")
        else:
            messagebox.showwarning("Atenção", "Por favor, insira o código de verificação.")

    def redefinir_senha(self):
        # Atualiza a interface para permitir a redefinição da senha
        self.label.configure(text="Digite a nova senha:")
        self.codigo_entry.destroy()  # Remove o campo de código
        self.ok_button.configure(text="Redefinir Senha", command=self.salvar_nova_senha)

        # Cria os campos para inserir nova senha
        self.senha_entry = ctk.CTkEntry(self, placeholder_text="Nova senha", show="*", width=200)
        self.senha_entry.pack(pady=(5, 10))

        self.confirm_senha_entry = ctk.CTkEntry(self, placeholder_text="Confirmar senha", show="*", width=200)
        self.confirm_senha_entry.pack(pady=(5, 10))

        # Atualiza os botões
        self.button_frame.destroy()

        # Cria um novo Frame para os botões da tela de redefinição, com fundo transparente
        self.button_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.button_frame.pack(pady=(10, 10))

        # Botões da tela de redefinição de senha (de forma horizontal)
        self.ok_button = ctk.CTkButton(self.button_frame, text="Redefinir Senha", command=self.salvar_nova_senha, width=95)
        self.ok_button.pack(side="left", padx=5)

        self.cancel_button = ctk.CTkButton(self.button_frame, text="Cancelar", command=self.on_cancel, width=95)
        self.cancel_button.pack(side="left", padx=5)

    def salvar_nova_senha(self):
        senha = self.senha_entry.get()
        confirm_senha = self.confirm_senha_entry.get()
        if senha and senha == confirm_senha:
            # Aqui você deve colocar a lógica para salvar a nova senha no banco de dados
            # Supondo que você tenha um repositório de usuários
            if self.atualizar_senha(self.email_usuario, senha):
                messagebox.showinfo("Sucesso", "Senha redefinida com sucesso!")
                self.destroy()  # Fecha a janela de redefinição de senha
            else:
                messagebox.showerror("Erro", "Erro ao redefinir a senha. Tente novamente.")
        else:
            messagebox.showerror("Erro", "As senhas não coincidem ou estão vazias.")

    def atualizar_senha(self, email, nova_senha):
        """
        Atualiza a senha no banco de dados. Aqui você deve implementar a lógica para alterar a senha.
        """
        try:
            # Exemplo de como você pode chamar o método do repositório de usuários para atualizar a senha
            usuario_repo = UsuarioRepository()  # Seu repositório de usuários
            return usuario_repo.atualizar_senha(email, nova_senha)
        except Exception as e:
            print(f"Erro ao atualizar a senha: {e}")
            return False

    def on_cancel(self):
        self.destroy()
