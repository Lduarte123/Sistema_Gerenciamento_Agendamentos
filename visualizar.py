import customtkinter as ctk
from tkinter import messagebox
from tkinter import ttk  # Importa o ttk para usar Treeview

import customtkinter as ctk
from tkinter import messagebox
from tkinter import ttk  # Importa o ttk para usar Treeview

class Visualizar:
    def __init__(self, parent, agendamentos):
        self.parent = parent
        self.agendamentos = agendamentos
        self.janela_visualizar = None
        self.visualizar_informacoes()

    def visualizar_informacoes(self):
        self.janela_visualizar = ctk.CTkToplevel(self.parent)
        self.janela_visualizar.title("Visualizando Agendamentos")
        self.janela_visualizar.geometry("600x500")

        self.janela_visualizar.grab_set()

        self.tree = ttk.Treeview(self.janela_visualizar, columns=("codigo", "nome", "data", "local"), show='headings')
        self.tree.heading("codigo", text="Código")
        self.tree.heading("nome", text="Nome")
        self.tree.heading("data", text="Data")
        self.tree.heading("local", text="Local")

        # Define o tamanho das colunas
        self.tree.column("codigo", width=100)
        self.tree.column("nome", width=150)
        self.tree.column("data", width=150)
        self.tree.column("local", width=150)

        self.atualizar_tabela()

        self.tree.pack(pady=20, fill="both", expand=True)

        botao_editar = ctk.CTkButton(self.janela_visualizar, text="Editar", command=self.editar_agendamento)
        botao_editar.pack(side="left", padx=(20, 10), pady=20)

        botao_excluir = ctk.CTkButton(self.janela_visualizar, text="Excluir", command=self.excluir_agendamento)
        botao_excluir.pack(side="right", padx=(10, 20), pady=20)

        botao_fechar = ctk.CTkButton(self.janela_visualizar, text="Fechar", command=self.janela_visualizar.destroy)
        botao_fechar.pack(pady=20)

    def atualizar_tabela(self):
        # Limpa a Treeview antes de adicionar os agendamentos
        for item in self.tree.get_children():
            self.tree.delete(item)

        for agendamento in self.agendamentos:
            self.tree.insert("", "end", values=(agendamento.codigo, agendamento.nome, agendamento.data, agendamento.local))

    def editar_agendamento(self):
        # Obtém o item selecionado
        selected_item = self.tree.selection()
        if selected_item:
            item_values = self.tree.item(selected_item, 'values')
            codigo = item_values[0]
            nome = item_values[1]
            data = item_values[2]
            local = item_values[3]

            self.janela_editar(codigo, nome, data, local)
        else:
            messagebox.showwarning("Seleção Inválida", "Selecione um agendamento para editar.")

    def janela_editar(self, codigo, nome, data, local):
        # Criação da janela de edição
        janela_editar = ctk.CTkToplevel(self.janela_visualizar)
        janela_editar.title("Editar Agendamento")
        janela_editar.geometry("500x500")

        # Campos de entrada
        ctk.CTkLabel(janela_editar, text="Código:").pack(pady=10)
        label_codigo = ctk.CTkLabel(janela_editar, text=codigo)
        label_codigo.pack(pady=10)

        ctk.CTkLabel(janela_editar, text="Nome:").pack(pady=10)
        entrada_nome = ctk.CTkEntry(janela_editar, width=200)
        entrada_nome.insert(0, nome)
        entrada_nome.pack(pady=10)

        ctk.CTkLabel(janela_editar, text="Data:").pack(pady=10)
        entrada_data = ctk.CTkEntry(janela_editar, width=200)
        entrada_data.insert(0, data)
        entrada_data.pack(pady=10)

        ctk.CTkLabel(janela_editar, text="Local:").pack(pady=10)
        entrada_local = ctk.CTkEntry(janela_editar, width=200)
        entrada_local.insert(0, local)
        entrada_local.pack(pady=10)

        # Botão para salvar as edições
        botao_salvar = ctk.CTkButton(janela_editar, text="Salvar", command=lambda: self.salvar_edicao(janela_editar, codigo, entrada_nome.get(), entrada_data.get(), entrada_local.get()))
        botao_salvar.pack(pady=20)

    def salvar_edicao(self, janela, codigo, novo_nome, novo_data, novo_local):
        if novo_nome and novo_data:
            # Atualiza o agendamento
            for agendamento in self.agendamentos:
                if agendamento.codigo == int(codigo):
                    agendamento.nome = novo_nome
                    agendamento.data = novo_data
                    agendamento.local = novo_local
                    break
            self.atualizar_tabela()  # Atualiza a tabela
            messagebox.showinfo("Sucesso", "Agendamento editado com sucesso!")
            janela.destroy() 
        else:
            messagebox.showwarning("Erro", "Nome e data não podem estar vazios.")

    def excluir_agendamento(self):
        itemSelecionado = self.tree.selection()
        # Pega o item selecionado
        if itemSelecionado:
            valoresItens = self.tree.item(itemSelecionado, 'values')
            codigo = int(valoresItens[0])  # Certifique-se de que o código é um inteiro

            agendamento_encontrado = None
            for agendamento in self.agendamentos:
                if agendamento.codigo == codigo:
                    agendamento_encontrado = agendamento
                    break

            if agendamento_encontrado:
                self.agendamentos.remove(agendamento_encontrado)  # Remove da lista
                self.tree.delete(itemSelecionado)  
                messagebox.showinfo("Excluir Agendamento", "Agendamento excluído com sucesso!")
            else:
                messagebox.showwarning("Erro", "Agendamento não encontrado.")
        else:
            messagebox.showwarning("Seleção Inválida", "Selecione um agendamento para excluir.")

