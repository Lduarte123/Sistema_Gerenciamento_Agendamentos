import customtkinter as ctk
from tkinter import messagebox

class AdminFrame(ctk.CTkFrame):
    def __init__(self, root, controller):
        super().__init__(root)
        self.controller = controller

        # Configurações gerais da tela
        self.pack(expand=True, fill="both", padx=20, pady=20)
        self.configure(fg_color="#2E2E2E")  # Fundo mais escuro

        # Título da tela
        self.title_label = ctk.CTkLabel(self, text="Administração", font=("Arial", 24, "bold"), text_color="#FFD700")
        self.title_label.pack(pady=(50, 20))

        # Botão de Gerenciamento de Usuários
        self.user_mgmt_button = ctk.CTkButton(self, text="Gerenciar Usuários", command=self.gerenciar_usuarios, width=250, height=40)
        self.user_mgmt_button.pack(pady=10)

        # Botão para Visualizar Logs
        self.view_logs_button = ctk.CTkButton(self, text="Visualizar Logs", command=self.visualizar_logs, width=250, height=40)
        self.view_logs_button.pack(pady=10)

        # Botão para Gerenciar Configurações do Sistema
        self.system_settings_button = ctk.CTkButton(self, text="Configurações do Sistema", command=self.configurar_sistema, width=250, height=40)
        self.system_settings_button.pack(pady=10)

        # Listagem de Ações Recentes (apenas para visualização)
        self.actions_label = ctk.CTkLabel(self, text="Ações Recentes", font=("Arial", 18, "bold"), text_color="#FFD700")
        self.actions_label.pack(pady=(40, 10))

        # Caixa de Texto para Exibir Logs
        self.logs_textbox = ctk.CTkTextbox(self, width=400, height=200)
        self.logs_textbox.pack(pady=10)
        self.logs_textbox.insert("1.0", "Log 1: Usuário X criou um agendamento.\nLog 2: Usuário Y deletou um agendamento.")
        self.logs_textbox.configure(state="disabled")  # Impede edição dos logs

        # Botão de Voltar
        self.back_button = ctk.CTkButton(self, text="Voltar", command=self.voltar, width=100, height=30, fg_color="#FF4500")
        self.back_button.pack(pady=(30, 10))

    def gerenciar_usuarios(self):
        messagebox.showinfo("Gerenciar Usuários", "Aqui você poderá gerenciar os usuários.")

    def visualizar_logs(self):
        messagebox.showinfo("Visualizar Logs", "Aqui você poderá visualizar logs do sistema.")

    def configurar_sistema(self):
        messagebox.showinfo("Configurações do Sistema", "Aqui você poderá alterar as configurações do sistema.")

    def voltar(self):
        self.controller.exibir_tela_inicial()

