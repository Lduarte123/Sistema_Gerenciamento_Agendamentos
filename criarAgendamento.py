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
        self.janela_criar = None  # Inicializa a janela como None
        self.abrir_janela_criar()

    def abrir_janela_criar(self):
        self.janela_criar = ctk.CTkToplevel(self.parent)
        self.janela_criar.title("Criar Agendamento")
        self.janela_criar.geometry("600x500")
        
        self.janela_criar.grab_set()

        frameCriarAgendamento = ctk.CTkFrame(self.janela_criar, fg_color='transparent')
        frameCriarAgendamento.pack(pady=30)

        # Nome do Evento
        label_nome = ctk.CTkLabel(frameCriarAgendamento, text="Nome do Evento:")
        label_nome.grid(row=0, column=0, padx=(0, 10), pady=(0, 10), sticky='w')

        self.entrada_nome = ctk.CTkEntry(frameCriarAgendamento, width=200)
        self.entrada_nome.grid(row=0, column=1, pady=(0, 10), sticky='ew')

        # Data do Evento
        label_data = ctk.CTkLabel(self.janela_criar, text="Data do Evento:")
        label_data.pack(pady=(10, 0))

        # Estilizando o calendário
        self.calendario = Calendar(
            self.janela_criar,
            selectmode='day',
            year=2024,
            month=9,
            day=25,
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

        # Botão para salvar o agendamento
        botao_salvar = ctk.CTkButton(self.janela_criar, text="Salvar", command=self.salvar_agendamento)
        botao_salvar.pack(pady=20)

        # Botão para fechar a janela
        botao_fechar = ctk.CTkButton(self.janela_criar, text="Fechar", command=self.janela_criar.destroy)
        botao_fechar.pack(pady=5)

        self.janela_criar.focus_force()

    def salvar_agendamento(self):
        nome = self.entrada_nome.get()
        data = self.calendario.get_date()
        horario = self.entrada_horario.get()
        local = self.entrada_local.get()

        # Validação do horário
        if not re.match(r'^(?:[01]\d|2[0-3]):[0-5]\d$', horario):
            messagebox.showerror("Erro", "Horário deve ser no formato HH:MM.")
            return

        # Formatar a data e hora
        data_hora_str = f"{data} {horario}"
        data_hora_agendamento = datetime.strptime(data_hora_str, "%d/%m/%Y %H:%M")

        # Obter data e hora atuais
        data_hora_atual = datetime.now()

        # Verificar se a data e hora do agendamento são anteriores à data e hora atuais
        if data_hora_agendamento < data_hora_atual:
            messagebox.showerror("Erro", "A data e o horário selecionados já passaram.")
            return

        if nome and data and horario:
            agendamento = Agendamento(nome, data_hora_str, local)  # Armazenando a data e hora
            self.agendamentos.append(agendamento)
            messagebox.showinfo("Sucesso", f"Agendamento criado! Código: {agendamento.codigo}\n{agendamento.nome}\nLocal: {agendamento.local}\nHorário: {agendamento.data}")


            self.janela_criar.destroy()  # Fecha a janela
            return
        
        messagebox.showerror("Erro", "Preencha todos os campos.")
