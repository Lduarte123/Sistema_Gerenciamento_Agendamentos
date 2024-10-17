import customtkinter as ctk
from tkinter import messagebox
from tkcalendar import Calendar
from agendamentos import Agendamento
import re  # Para validação do horário
from datetime import datetime

class CriarAgendamento:
    def __init__(self, parent, agendamentos):
        self.parent = parent
        self.agendamentos = agendamentos
        self.janela_criar = None 
        self.abrir_janela_criar()

    def abrir_janela_criar(self):
        self.janela_criar = ctk.CTkToplevel(self.parent)
        self.janela_criar.title("Criar Agendamento")
        self.janela_criar.geometry("600x500")
        
        self.janela_criar.attributes("-topmost", True)

        frameCriarAgendamento = ctk.CTkFrame(self.janela_criar, fg_color='transparent')
        frameCriarAgendamento.pack(pady=30)

        # Nome
        label_nome = ctk.CTkLabel(frameCriarAgendamento, text="Nome do Evento:")
        label_nome.grid(row=0, column=0, padx=(0, 10), pady=(0, 10), sticky='w')

        self.entrada_nome = ctk.CTkEntry(frameCriarAgendamento, placeholder_text="Inisira o evento",width=200)
        self.entrada_nome.grid(row=0, column=1, pady=(0, 10), sticky='ew')

        # Data
        label_data = ctk.CTkLabel(self.janela_criar, text="Data do Evento:")
        label_data.pack(pady=(10, 0))

        dia_atual = datetime.now()

        # Calendario
        self.calendario = Calendar(
            self.janela_criar,
            selectmode='day',
            year=dia_atual.year,
            month=dia_atual.month,
            day=dia_atual.day,
            background='#145DA0', 
            locale='pt_BR',
            foreground='white',
            bordercolor='#4682b4', 
            headersbackground='#5f9ea0', 
            headersforeground='white',
            showweeknumbers=False,
            weekendbackground='white', 
            weekendforeground='black',
            font=('Arial', 10)
        )
        self.calendario.pack(pady=(0, 10))

        # Horário
        label_horario = ctk.CTkLabel(frameCriarAgendamento, text="Horário (HH:MM):")
        label_horario.grid(row=1, column=0, padx=(0, 10), pady=(0, 10), sticky='w')

        self.entrada_horario = ctk.CTkEntry(frameCriarAgendamento, placeholder_text="HH:MM", width=200)
        self.entrada_horario.grid(row=1, column=1, pady=(0, 10), sticky='ew')

        # Local
        label_local = ctk.CTkLabel(frameCriarAgendamento, text="Local: ")
        label_local.grid(row=2, column=0, padx=(0, 10), pady=(0, 10), sticky='w')

        self.entrada_local = ctk.CTkEntry(frameCriarAgendamento, placeholder_text="Opcional", width=200)
        self.entrada_local.grid(row=2, column=1, pady=(0, 10), sticky='ew')

        botao_salvar = ctk.CTkButton(self.janela_criar, text="Salvar", command=self.salvar_agendamento)
        botao_salvar.pack(pady=20)

        botao_fechar = ctk.CTkButton(self.janela_criar, text="Fechar", command=self.janela_criar.destroy)
        botao_fechar.pack(pady=5)


    def salvar_agendamento(self):
        nome = self.entrada_nome.get()
        data = self.calendario.get_date()
        horario = self.entrada_horario.get()
        local = self.entrada_local.get()

        # Validação do horário
        if not re.match(r'^(?:[01]\d|2[0-3]):[0-5]\d$', horario):
            messagebox.showerror("Erro", "Horário deve ser no formato HH:MM.", parent=self.janela_criar)
            return

        # Obter data e hora atuais
        data_hora_atual = datetime.now()

        # Separando a validação da data e do horário
        data_agendamento = datetime.strptime(data, "%d/%m/%Y")
        hora_agendamento = datetime.strptime(horario, "%H:%M").time()

        # Verificar se a data do agendamento é anterior à data atual
        if data_agendamento.date() < data_hora_atual.date():
            messagebox.showerror("Erro", "A data selecionada já passou.", parent=self.janela_criar)
            return

        # Verificar se o horário é anterior ao horário atual se for no mesmo dia
        if data_agendamento.date() == data_hora_atual.date() and hora_agendamento < data_hora_atual.time():
            messagebox.showerror("Erro", "O horário selecionado já passou.", parent=self.janela_criar)
            return

        if nome and data and horario:
            # Não precisa mais concatenar a data e o horário, eles são tratados separadamente
            agendamento = Agendamento(nome, data, horario, local)
            self.agendamentos.append(agendamento)
            messagebox.showinfo("Sucesso", f"Agendamento criado! Código: {agendamento.codigo}\n{agendamento.nome}\nLocal: {agendamento.local}\nData: {agendamento.data}\nHorário: {agendamento.horario}", parent=self.janela_criar)
            self.janela_criar.destroy()  # Fecha a janela
            return
        
        messagebox.showerror("Erro", "Preencha todos os campos.", parent=self.janela_criar)
