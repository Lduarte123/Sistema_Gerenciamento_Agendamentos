import customtkinter as ctk
from tkinter import messagebox
from tkcalendar import Calendar
from agendamentos import Agendamento

class CriarAgendamento:
    def __init__(self, parent, agendamentos):
        self.parent = parent
        self.agendamentos = agendamentos
        self.janela_criar = None  # Inicializa a janela como None
        self.abrir_janela_criar()

    def abrir_janela_criar(self):
        self.janela_criar = ctk.CTkToplevel(self.parent)
        self.janela_criar.title("Criar Agendamento")
        self.janela_criar.geometry("700x500")
        
        self.janela_criar.grab_set()

        # Dentro do método abrir_janela_criar()
        frame_nome = ctk.CTkFrame(self.janela_criar)
        frame_nome.pack(pady=10)

        label_nome = ctk.CTkLabel(frame_nome, text="Nome do Evento:")
        label_nome.pack(side='left', padx=(0, 10))

        self.entrada_nome = ctk.CTkEntry(frame_nome)
        self.entrada_nome.pack(side='left')


        label_data = ctk.CTkLabel(self.janela_criar, text="Data do Evento:")
        label_data.pack(pady=10)

        # Estilizando o calendário
        self.calendario = Calendar(
            self.janela_criar,
            selectmode='day',
            year=2024,
            month=9,
            day=25,
            background='#145DA0', 
            foreground='white',
            bordercolor='#4682b4', 
            headersbackground='#5f9ea0', 
            headersforeground='white', 
            weekheader='#20b2aa', 
            showweeknumbers=False,
            font=('Arial', 10)
        )

        self.calendario.pack(pady=10)

        botao_salvar = ctk.CTkButton(self.janela_criar, text="Salvar", command=self.salvar_agendamento)
        botao_salvar.pack(pady=20)

        self.janela_criar.focus_force()
        
    def salvar_agendamento(self):
        nome = self.entrada_nome.get()
        data = self.calendario.get_date()

        if nome and data:
            agendamento = Agendamento(nome, data)
            self.agendamentos.append(agendamento)
            messagebox.showinfo("Sucesso", f"Agendamento criado! Código: {agendamento.codigo}")
            self.janela_criar.destroy()  # Fecha a janela
            return
        
        messagebox.showerror("Erro", "Preencha todos os campos.")
