import customtkinter as ctk
from tkcalendar import Calendar
import tkinter as tk
from tkinter import Toplevel, messagebox
from datetime import datetime



class RegisterView(ctk.CTkFrame):
    def __init__(self, root, controller):
        super().__init__(root)
        self.controller = controller
        
        # Título
        self.label = ctk.CTkLabel(self, text="Registrar Novo Usuário", font=ctk.CTkFont(size=20, weight="bold"))
        self.label.pack(pady=(160, 20))

        # Criação de um frame para o formulário, centralizando ele
        form_frame = ctk.CTkFrame(self, fg_color="transparent")
        form_frame.pack(pady=40, padx=20, anchor="center")  # Centraliza o frame no meio da tela

        # Nome
        self.nome_label = ctk.CTkLabel(form_frame, text="Nome:", font=ctk.CTkFont(size=16, weight="bold"))
        self.nome_label.grid(row=0, column=0, padx=(0, 25), pady=5, sticky="e")
        self.nome_entry = ctk.CTkEntry(form_frame, placeholder_text="Digite seu nome", width=300, height=40)
        self.nome_entry.grid(row=0, column=1, pady=5, sticky="w")

        # Senha
        self.senha_label = ctk.CTkLabel(form_frame, text="Senha:", font=ctk.CTkFont(size=16, weight="bold"))
        self.senha_label.grid(row=1, column=0, padx=(0, 25), pady=5, sticky="e")
        self.senha_entry = ctk.CTkEntry(form_frame, placeholder_text="Digite sua senha", show="*", width=300, height=40)
        self.senha_entry.grid(row=1, column=1, pady=5, sticky="w")

        # Email
        self.email_label = ctk.CTkLabel(form_frame, text="Email:", font=ctk.CTkFont(size=16, weight="bold"))
        self.email_label.grid(row=2, column=0, padx=(0, 25), pady=5, sticky="e")
        self.email_entry = ctk.CTkEntry(form_frame, placeholder_text="Digite seu email", width=300, height=40)
        self.email_entry.grid(row=2, column=1, pady=5, sticky="w")

        # Data de Nascimento com botão de calendário
        self.data_nasc_label = ctk.CTkLabel(form_frame, text="Data de Nascimento:", font=ctk.CTkFont(size=16, weight="bold"))
        self.data_nasc_label.grid(row=3, column=0, padx=(0, 25), pady=5, sticky="e")
        self.data_nasc_button = ctk.CTkButton(form_frame, text="Selecionar Data", command=self.open_calendar, width=300, height=40)
        self.data_nasc_button.grid(row=3, column=1, pady=5, sticky="w")
        self.data_nasc_var = tk.StringVar()
        self.data_nasc_display = ctk.CTkLabel(form_frame, textvariable=self.data_nasc_var)
        self.data_nasc_display.grid(row=4, column=1, padx=10, pady=5, sticky="w")

        # Cidade
        self.cidade_label = ctk.CTkLabel(form_frame, text="Cidade:", font=ctk.CTkFont(size=16, weight="bold"))
        self.cidade_label.grid(row=5, column=0, padx=(0, 25), pady=5, sticky="e")
        self.cidade_entry = ctk.CTkEntry(form_frame, placeholder_text="Digite sua cidade", width=300, height=40)
        self.cidade_entry.grid(row=5, column=1, pady=5, sticky="w")

        # Sexo
        self.sexo_label = ctk.CTkLabel(form_frame, text="Sexo:", font=ctk.CTkFont(size=16, weight="bold"))
        self.sexo_label.grid(row=6, column=0, padx=(0, 25), pady=5, sticky="e")
        self.sexo_entry = ctk.CTkComboBox(form_frame, values=["Masculino", "Feminino"], width=300, height=40)
        self.sexo_entry.grid(row=6, column=1, pady=5, sticky="w")

        # Aceitar termos
        self.termos_var = tk.BooleanVar()
        self.termos_check = ctk.CTkCheckBox(form_frame, text="Aceito os termos e condições", variable=self.termos_var)
        self.termos_check.grid(row=7, columnspan=2, pady=10)

        # Botão de registro
        self.register_button = ctk.CTkButton(self, text="Registrar", command=self.register, width=300, height=40)
        self.register_button.pack(pady=20)

        # Botão de voltar
        self.back_button = ctk.CTkButton(self, text="Voltar", command=self.voltar, width=300, height=40)
        self.back_button.pack(pady=10)

    def open_calendar(self):
        self.calendar_window = Toplevel(self)
        self.calendar = Calendar(
            self.calendar_window,
            selectmode='day',
            year=2023,
            month=10,
            day=5,
            date_pattern="dd/mm/yyyy"  # Configuração do formato
        )
        self.calendar.pack(pady=20)

        select_button = ctk.CTkButton(self.calendar_window, text="Selecionar", command=self.select_date)
        select_button.pack(pady=10)

    def select_date(self):
        selected_date = self.calendar.get_date()
        try:
            valid_date = datetime.strptime(selected_date, "%d/%m/%Y")
            # Verifica se a data selecionada é no futuro
            if valid_date.date() > datetime.now().date():
                messagebox.showerror("Erro", "A data de nascimento não pode ser no futuro.")
                return
        except ValueError:
            messagebox.showerror("Erro", "Formato de data inválido. Por favor, selecione uma data válida.")
            return

        self.data_nasc_var.set(selected_date)
        print(f"Data registrada: {selected_date}")
        self.calendar_window.destroy()

    def register(self):
        nome = self.nome_entry.get()
        senha = self.senha_entry.get()
        email = self.email_entry.get()
        data_nasc = self.data_nasc_var.get()
        cidade = self.cidade_entry.get()
        sexo = self.sexo_entry.get()

        # Verifica se todos os campos estão preenchidos
        if not all([nome, senha, email, data_nasc, cidade, sexo]):
            messagebox.showerror("Erro", "Todos os campos são obrigatórios. Por favor, preencha todos os campos.")
            return

        # Verifica se o e-mail já está cadastrado
        emails_cadastrados = self.controller.obter_emails_cadastrados()
        if email in emails_cadastrados:
            messagebox.showerror("Erro", "Erro ao registrar usuário: o e-mail já está em uso.")
            return

        resultado = self.controller.registrar_usuario(nome, email, senha, data_nasc, cidade, sexo)
        if resultado:
            messagebox.showinfo("Sucesso", "Usuário registrado com sucesso!")
            self.voltar()
        else:
            messagebox.showerror("Erro", "Erro ao registrar usuário. Verifique suas informações.")

    def voltar(self):
        self.controller.exibir_tela_login()
