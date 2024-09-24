# agendamento.py
import customtkinter as ctk
from tkinter import messagebox
from tkcalendar import Calendar
import random

class Agendamento:
    def __init__(self, nome, data):
        self.nome = nome
        self.data = data
        self.codigo = random.randint(1000, 9999)

class CriarAgendamento:
    def __init__(self, parent, agendamentos):
        self.parent = parent
        self.agendamentos = agendamentos
        self.abrir_janela_criar()

    def abrir_janela_criar(self):
        janela_criar = ctk.CTkToplevel(self.parent)
        janela_criar.title("Criar Agendamento")
        janela_criar.geometry("700x500")
        
        janela_criar.grab_set()

        label_nome = ctk.CTkLabel(janela_criar, text="Nome do Evento:")
        label_nome.pack(pady=10)

        entrada_nome = ctk.CTkEntry(janela_criar)
        entrada_nome.pack(pady=10)

        label_data = ctk.CTkLabel(janela_criar, text="Data do Evento:")
        label_data.pack(pady=10)

        self.calendario = Calendar(janela_criar)
        self.calendario.pack(pady=10)

        botao_salvar = ctk.CTkButton(janela_criar, text="Salvar", command=lambda: self.salvar_agendamento(entrada_nome))
        botao_salvar.pack(pady=20)

        janela_criar.focus_force()
        

    def salvar_agendamento(self, entrada_nome):
        nome = entrada_nome.get()
        data = self.calendario.get_date()

        if nome and data:
            agendamento = Agendamento(nome, data)
            self.agendamentos.append(agendamento)
            messagebox.showinfo("Sucesso", f"Agendamento criado! Código: {agendamento.codigo}")
            entrada_nome.delete(0, ctk.END)  # Limpa o campo de entrada
            self.calendario.selection_clear()  # Limpa a seleção do calendário
        else:
            messagebox.showerror("Erro", "Preencha todos os campos.")
