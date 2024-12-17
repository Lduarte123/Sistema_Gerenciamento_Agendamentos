import customtkinter as ctk
import tkinter as tk


class Editar(ctk.CTkToplevel):
    def __init__(self, master, agendamento, callback):
        super().__init__(master)
        self.agendamento = agendamento
        self.callback = callback

        self.title("Editar Agendamento")
        self.geometry("300x400")

        self.label_nome = ctk.CTkLabel(self, text="Nome:")
        self.label_nome.pack(pady=5)
        self.entry_nome = ctk.CTkEntry(self)
        self.entry_nome.insert(0, self.agendamento.nome)
        self.entry_nome.pack(pady=5)

        self.label_data = ctk.CTkLabel(self, text="Data:")
        self.label_data.pack(pady=5)
        self.entry_data = ctk.CTkEntry(self)
        self.entry_data.insert(0, self.agendamento.data)
        self.entry_data.pack(pady=5)

        self.label_horario = ctk.CTkLabel(self, text="Horário:")
        self.label_horario.pack(pady=5)
        self.entry_horario = ctk.CTkEntry(self)
        self.entry_horario.insert(0, self.agendamento.horario)
        self.entry_horario.pack(pady=5)

        self.label_local = ctk.CTkLabel(self, text="Local:")
        self.label_local.pack(pady=5)
        self.entry_local = ctk.CTkEntry(self)
        self.entry_local.insert(0, self.agendamento.local)
        self.entry_local.pack(pady=5)

        self.botao_salvar = ctk.CTkButton(self, text="Salvar", command=self.salvar_agendamento)
        self.botao_salvar.pack(pady=10)

        self.botao_fechar = ctk.CTkButton(self, text="Fechar", command=self.fechar)
        self.botao_fechar.pack(pady=10)

    def salvar_agendamento(self):
        novo_nome = self.entry_nome.get()
        nova_data = self.entry_data.get()
        novo_horario = self.entry_horario.get()
        novo_local = self.entry_local.get()

        self.callback(novo_nome, nova_data, novo_horario, novo_local)
        self.fechar()

    def fechar(self):
        self.destroy()
