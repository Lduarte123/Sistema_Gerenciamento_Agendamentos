import customtkinter as ctk
from tkinter import ttk, messagebox
from repository.agendamento_repository import AgendamentoRepository
from model.agendamento import AgendamentoModel as Agendamento
from view.editar_agendamento_view import Editar
from datetime import datetime

class VisualizarFrame(ctk.CTkFrame):
    def __init__(self, master, agendamento_repository):
        super().__init__(master)
        self.agendamento_repository = agendamento_repository

        self.tree = ttk.Treeview(self, columns=("id", "nome", "data", "horario", "local", "descricao"), show='headings')
        self.tree.heading("id", text="ID")
        self.tree.heading("nome", text="Nome")
        self.tree.heading("data", text="Data")
        self.tree.heading("horario", text="Horário")
        self.tree.heading("local", text="Local")
        self.tree.heading("descricao", text="Descrição")

        self.tree.column("id", width=50)
        self.tree.column("nome", width=200)
        self.tree.column("data", width=100)
        self.tree.column("horario", width=100)
        self.tree.column("local", width=150)
        self.tree.column("descricao", width=200)


        self.tree.pack(pady=20, fill="both", expand=True)

        self.atualizar_tabela()

        # Frame para os botões
        self.botao_frame = ctk.CTkFrame(self)
        self.botao_frame.pack(pady=10)

        self.btn_voltar = ctk.CTkButton(self.botao_frame, text="Editar", command=self.editar_agendamento)
        self.btn_voltar.pack(side="left", padx=(0, 10))  # Margem à direita

        self.btn_fechar = ctk.CTkButton(self.botao_frame, text="Voltar", command=self.voltar)
        self.btn_fechar.pack(side="left", padx=(0, 10))  # Margem à direita

        self.btn_excluir = ctk.CTkButton(self.botao_frame, text="Excluir", command=self.excluir_agendamento)
        self.btn_excluir.pack(side="left")


    def atualizar_tabela(self):
        # Limpa a tabela antes de adicionar novos dados
        for row in self.tree.get_children():
            self.tree.delete(row)

        agendamentos = self.agendamento_repository.listar_agendamentos()

        for agendamento in agendamentos:
            # Verifica se agendamento.data é uma string e converte
            if isinstance(agendamento.data, str):
                try:
                    # Primeiro tenta converter se estiver no formato YYYY-MM-DD
                    data_agendamento = datetime.strptime(agendamento.data, "%Y-%m-%d")
                except ValueError:
                    # Se falhar, assume que está no formato DD-MM-YYYY
                    data_agendamento = datetime.strptime(agendamento.data, "%d-%m-%Y")
            else:
                data_agendamento = agendamento.data  # Presume que já é um objeto datetime

            # Formata a data corretamente como string
            data_formatada = data_agendamento.strftime("%d-%m-%Y")  # Formato dd-mm-aaaa

            # Para o horário, você deve verificar da mesma forma
            if isinstance(agendamento.horario, str):
                horario_formatado = agendamento.horario  # Presume que já é uma string no formato correto
            else:
                horario_formatado = agendamento.horario.strftime("%H:%M")  # Formata o horário

            # Exibe os dados para debug
            print(f"ID: {agendamento.id}, Nome: {agendamento.nome}, Data: {data_formatada}, Horário: {horario_formatado}, Local: {agendamento.local}, Descrição: {agendamento.descricao}")

            # Insere os dados formatados na tabela, incluindo a descrição
            self.tree.insert('', 'end', values=(agendamento.id, agendamento.nome, data_formatada, horario_formatado, agendamento.local, agendamento.descricao if agendamento.descricao else "N/A"))  # Exibe "N/A" se descrição for vazia



    def editar_agendamento(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Erro", "Selecione um agendamento para editar.")
            return

        item_values = self.tree.item(selected_item, "values")
        id_agendamento = item_values[0]

        # Cria um objeto agendamento a partir dos dados selecionados
        agendamento_selecionado = Agendamento(
            id=id_agendamento,
            nome=item_values[1],
            data=item_values[2],
            horario=item_values[3],
            local=item_values[4],
            descricao=item_values[5] if len(item_values) > 5 else ""  # Adiciona a descrição
        )

        editar = Editar(self, agendamento_selecionado, self.atualizar_agendamento_dados)


    def voltar(self):
        self.master.controller.exibir_tela_inicial()

    def atualizar_agendamento_dados(self, novo_nome, nova_data, novo_horario, novo_local, nova_descricao=""):
        agendamento_atualizado = Agendamento(
            id=self.tree.item(self.tree.selection(), "values")[0],
            nome=novo_nome,
            data=nova_data,
            horario=novo_horario,
            local=novo_local,
            descricao=nova_descricao
        )

        # Atualiza o agendamento no repositório
        self.agendamento_repository.atualizar_agendamento(agendamento_atualizado)
        self.atualizar_tabela()

    def excluir_agendamento(self):
        item_selecionado = self.tree.selection()
        if item_selecionado:
            confirmation = messagebox.askyesno("Confirmar Exclusão", "Tem certeza que deseja excluir este agendamento?")
            if confirmation:
                agendamento_id = self.get_agendamento_id()
                self.agendamento_repository.excluir_agendamento(agendamento_id)
                messagebox.showinfo("Sucesso", "Agendamento excluído com sucesso!")
                self.atualizar_tabela() 
                return
        messagebox.showerror("Erro", "Selecione um agendamento para excluir.")


    def get_agendamento_id(self):
        selected_item = self.tree.selection()
        if selected_item:
            return self.tree.item(selected_item, "values")[0]
        return None