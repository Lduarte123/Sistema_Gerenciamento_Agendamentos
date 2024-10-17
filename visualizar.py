import customtkinter as ctk
from tkinter import messagebox
from tkinter import ttk 

class Visualizar:
    def __init__(self, parent, agendamentos):
        self.parent = parent
        self.agendamentos = agendamentos
        self.janela_visualizar = None
        self.visualizar_informacoes()

    def visualizar_informacoes(self):
        self.janela_visualizar = ctk.CTkToplevel(self.parent)
        self.janela_visualizar.title("Visualizando Agendamentos")
        self.janela_visualizar.geometry("800x500")

        self.janela_visualizar.attributes("-topmost", True)

        # Criação da Treeview para a tabela
        self.tree = ttk.Treeview(self.janela_visualizar, columns=("codigo", "nome", "data", "horario", "local"), show='headings')
        self.tree.heading("codigo", text="Código")
        self.tree.heading("nome", text="Nome")
        self.tree.heading("data", text="Data")
        self.tree.heading("horario", text="Horário")
        self.tree.heading("local", text="Local")

        # Define o tamanho das colunas
        self.tree.column("codigo", width=100)
        self.tree.column("nome", width=150)
        self.tree.column("data", width=150)
        self.tree.column("horario", width=150)
        self.tree.column("local", width=150)

        # Adiciona agendamentos à Treeview
        self.atualizar_tabela()

        self.tree.pack(pady=20, fill="both", expand=True)

        # Botões de Editar e Excluir
        botao_editar = ctk.CTkButton(self.janela_visualizar, text="Editar", command=self.editar_agendamento)
        botao_editar.pack(side="left", padx=(20, 10), pady=20)

        botao_excluir = ctk.CTkButton(self.janela_visualizar, text="Excluir", command=self.confirmar_exclusao)
        botao_excluir.pack(side="right", padx=(10, 20), pady=20)

        # Botão para fechar a janela
        botao_fechar = ctk.CTkButton(self.janela_visualizar, text="Fechar", command=self.janela_visualizar.destroy)
        botao_fechar.pack(pady=20)

    def atualizar_tabela(self):
        # Limpa a Treeview antes de adicionar os agendamentos
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Adiciona os agendamentos à Treeview
        for agendamento in self.agendamentos:
            self.tree.insert("", "end", values=(agendamento.codigo, agendamento.nome, agendamento.data, agendamento.horario, agendamento.local))

    def editar_agendamento(self):
        # Obtém o item selecionado
        selected_item = self.tree.selection()
        if selected_item:
            item_values = self.tree.item(selected_item, 'values')
            codigo = item_values[0]
            nome = item_values[1]
            data = item_values[2]
            horario = item_values[3]
            local = item_values[4]

            # Abre a janela personalizada para edição
            self.janela_editar(codigo, nome, data, horario, local)
            return
        messagebox.showerror("Erro", "Houve um erro ao editar o agendamento", parent=self.parent)
       

    def janela_editar(self, codigo, nome, data, horario, local):
        # Criação da janela de edição
        janela_editar = ctk.CTkToplevel(self.janela_visualizar)
        janela_editar.title("Editar Agendamento")
        janela_editar.geometry("500x500")

        janela_editar.attributes("-topmost", True)


        # Campos de entrada
        ctk.CTkLabel(janela_editar, text="Código:").pack(pady=5)
        label_codigo = ctk.CTkLabel(janela_editar, text=codigo)
        label_codigo.pack(pady=5)

        ctk.CTkLabel(janela_editar, text="Nome:").pack(pady=5)
        entrada_nome = ctk.CTkEntry(janela_editar, width=200)
        entrada_nome.insert(0, nome)
        entrada_nome.pack(pady=5)

        ctk.CTkLabel(janela_editar, text="Data:").pack(pady=5)
        entrada_data = ctk.CTkEntry(janela_editar, width=200)
        entrada_data.insert(0, data)
        entrada_data.pack(pady=5)

        ctk.CTkLabel(janela_editar, text="Horário:").pack(pady=5)
        entrada_horario = ctk.CTkEntry(janela_editar, width=200)
        entrada_horario.insert(0, horario)
        entrada_horario.pack(pady=5)

        ctk.CTkLabel(janela_editar, text="Local:").pack(pady=5)
        entrada_local = ctk.CTkEntry(janela_editar, width=200)
        entrada_local.insert(0, local)
        entrada_local.pack(pady=5)

        # Botão para salvar as edições
        botao_salvar = ctk.CTkButton(janela_editar, text="Salvar", command=lambda: self.salvar_edicao(janela_editar, codigo, entrada_nome.get(), entrada_data.get(), entrada_horario.get(), entrada_local.get()))
        botao_salvar.pack(pady=20)

    def salvar_edicao(self, janela, codigo, novo_nome, novo_data, novo_horario, novo_local):
        if novo_nome and novo_data and novo_horario:
            # Atualiza o agendamento
            for agendamento in self.agendamentos:
                if agendamento.codigo == int(codigo):
                    agendamento.nome = novo_nome
                    agendamento.data = novo_data
                    agendamento.horario = novo_horario
                    agendamento.local = novo_local
                    break
            self.atualizar_tabela()  # Atualiza a tabela
            janela.destroy()  # Fecha a janela de edição
            messagebox.showinfo("Sucesso", f"Agendamento {agendamento.codigo} editado com sucesso!", parent=self.tree.winfo_toplevel())
            return
        messagebox.showerror("Erro" f"Selecione um agendamento para editar!", parent=self.tree.winfo_toplevel())

    def confirmar_exclusao(self):
        # Obtém o item selecionado
        itemSelecionado = self.tree.selection()
        if itemSelecionado:
            # Exibe a mensagem de confirmação
            resposta = messagebox.askyesno("Confirmação", "Você tem certeza que deseja excluir este agendamento?", parent=self.tree.winfo_toplevel())
            if resposta:  # Se o usuário confirmar
                self.excluir_agendamento()
    
    def excluir_agendamento(self):
        # Obtém o item selecionado
        itemSelecionado = self.tree.selection()
        if itemSelecionado:
            valoresItens = self.tree.item(itemSelecionado, 'values')
            codigo = int(valoresItens[0])  # Certifique-se de que o código é um inteiro

            # Tenta encontrar e remover o agendamento correspondente
            agendamento_encontrado = None
            for agendamento in self.agendamentos:
                if agendamento.codigo == codigo:
                    agendamento_encontrado = agendamento
                    break

            if agendamento_encontrado:
                self.agendamentos.remove(agendamento_encontrado)  # Remove da lista
                self.tree.delete(itemSelecionado)  # Remove o item da Treeview
                messagebox.showinfo("Sucesso", "Agendamento excluído com sucesso!", parent=self.tree.winfo_toplevel())
                return
            messagebox.showerror("Erro", "Selecione um agendamento para excluir!")

    

