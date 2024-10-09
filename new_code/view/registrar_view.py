import customtkinter as ctk
from tkcalendar import Calendar
import tkinter as tk
from tkinter import Toplevel, messagebox
from datetime import datetime
from model.usuario import UsuarioModel


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
        """Abre uma janela com um calendário para selecionar a data de nascimento."""
        self.calendar_window = Toplevel(self)
        self.calendar = Calendar(self.calendar_window, selectmode='day', year=2023, month=10, day=5)
        self.calendar.pack(pady=20)

        select_button = ctk.CTkButton(self.calendar_window, text="Selecionar", command=self.select_date)
        select_button.pack(pady=10)

    # def select_date(self):
    #     """Obtém a data selecionada e fecha o calendário."""
    #     selected_date = self.calendar.get_date()
    #     self.data_nasc_var.set(selected_date)
    #     self.calendar_window.destroy()



    # def select_date(self):
    #     """Obtém a data selecionada e fecha o calendário."""
    #     selected_date = self.calendar.get_date()  # Exemplo: '10/2/23' ou '10/02/2023'
    #     print(f"Data selecionada: {selected_date}")  # Para depuração

    #     try:
    #         valid_date = datetime.strptime(selected_date, "%d/%m/%Y")  # Para '10/02/2023'
    #     except ValueError:
    #         messagebox.showerror("Erro", "Formato de data inválido. Por favor, use dia/mês/ano.")
    #         return

    #     formatted_date = valid_date.strftime("%d-%m-%Y")  # Formata para DD-MM-AAAA
    #     self.data_nasc_var.set(formatted_date)  # Armazena a data como string
    #     print(f"Data formatada: {formatted_date}")  # Para depuração
    #     self.calendar_window.destroy()


    def select_date(self):
        """Obtém a data selecionada e fecha o calendário."""
        selected_date = self.calendar.get_date()  # Exemplo: '10/3/23'
        print(f"Data selecionada: {selected_date}")  # Para depuração


        valid_date = datetime.strptime(selected_date, "%m/%d/%y")  # Para '10/3/23'
   
        inverted_date = valid_date.strftime("%d/%m/%Y")  # Formata para MM-DD-AAAA
        self.data_nasc_var.set(inverted_date)  # Armazena a data como string
        print(f"Data invertida: {inverted_date}")  # Para depuração
        self.calendar_window.destroy()

    def register(self):
        nome = self.nome_entry.get()
        senha = self.senha_entry.get()
        email = self.email_entry.get()
        data_nasc = self.data_nasc_var.get()  # data no formato MM-DD-AAAA
        cidade = self.cidade_entry.get()
        sexo = self.sexo_entry.get()
        
        
        emails_cadastrados = self.controller.obter_emails_cadastrados()

        

        if not all([nome, senha, email, data_nasc, cidade, sexo]):
            messagebox.showerror("Erro", "Todos os campos são obrigatórios. Por favor, preencha todos os campos.")
            return

        if not self.termos_var.get():
            messagebox.showerror("Erro", "Você deve aceitar os termos e condições para se registrar.")
            return
        
        if email in emails_cadastrados:
            messagebox.showerror("Erro", "Erro ao registrar usuário: o e-mail já está em uso.")
            return

        print(f"Data a ser registrada: {data_nasc}")  # Para depuração

        try:
            # Valida a data no formato MM-DD-AAAA
            valid_date = datetime.strptime(data_nasc, "%d/%m/%Y")
            if valid_date > datetime.now():
                raise ValueError("A data não pode ser no futuro.")
        except ValueError:
            messagebox.showerror("Erro", "Data inválida. Por favor, insira uma data válida no formato mês-dia-ano (MM-DD-AAAA).")
            return
        
        usuario = UsuarioModel(
            nome=nome,
            email=email,
            senha=senha,
            data_nasc=valid_date.date(),  # Usar a data validada
            cidade=cidade,
            sexo=sexo
        )

        # Chama o método registrar_usuario com todos os parâmetros
        if self.controller.registrar_usuario(nome, email, senha, data_nasc, cidade, sexo):
            messagebox.showinfo("Sucesso", "Usuário registrado com sucesso!")
            self.voltar()
        else:
            messagebox.showerror("Erro", "Erro ao registrar usuário. Verifique suas informações.")

    def voltar(self):
        self.controller.exibir_tela_login()
