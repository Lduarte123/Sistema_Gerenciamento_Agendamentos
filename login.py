import customtkinter as ctk

# Definindo o tema
ctk.set_appearance_mode("dark")  # Modo escuro
ctk.set_default_color_theme("blue")  # Tema azul

# Função para lidar com o login
def fazer_login():
    usuario = entry_usuario.get()
    senha = entry_senha.get()
    print(f"Usuário: {usuario}, Senha: {senha}")  # Aqui você pode adicionar a lógica para verificar as credenciais.

# Função para criar conta
def criar_conta():
    print("Criar conta clicado!")  # Aqui você pode adicionar a lógica para criar uma nova conta.

# Criação da janela principal
app = ctk.CTk()
app.title("Tela de Login")
app.geometry("500x450")  # Tamanho ajustado para caber todos os elementos

# Criação dos widgets
label_usuario = ctk.CTkLabel(app, text="Usuário:")
label_usuario.pack(pady=10)

entry_usuario = ctk.CTkEntry(app, placeholder_text="Digite seu usuário")
entry_usuario.pack(pady=5)

label_senha = ctk.CTkLabel(app, text="Senha:")
label_senha.pack(pady=10)

entry_senha = ctk.CTkEntry(app, show='*', placeholder_text="Digite sua senha")
entry_senha.pack(pady=5)

# Botão de Login
botao_login = ctk.CTkButton(app, text="Login", command=fazer_login)
botao_login.pack(pady=(20, 5))  # Espaçamento melhorado

# Botão de Criar Conta
botao_criar_conta = ctk.CTkButton(app, text="Criar Conta", command=criar_conta)
botao_criar_conta.pack(pady=(5, 20))  # Espaçamento melhorado

# Iniciar o loop da interface
app.mainloop()
