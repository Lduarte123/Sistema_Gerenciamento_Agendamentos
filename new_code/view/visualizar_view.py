import customtkinter as ctk
from tkinter import ttk, messagebox
from repository.agendamento_repository import AgendamentoRepository
from model.agendamento import AgendamentoModel as Agendamento
from view.editar_agendamento_view import Editar
from datetime import datetime

class VisualizarFrame(ctk.CTkFrame):  # visualização em treeview
    def __init__(self, master, agendamento_repository, usuario_id):
        super().__init__(master)
        self.agendamento_repository = agendamento_repository
        self.usuario_id = usuario_id

        self.pagina_atual = 0
        self.itens_por_pagina = 40
        self.total_agendamentos = 0

        # Configuração da Treeview
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

        # Frame para os botões
        self.botao_frame = ctk.CTkFrame(self)
        self.botao_frame.pack(pady=10)

        self.btn_anterior = ctk.CTkButton(self.botao_frame, text="Anterior", command=self.pagina_anterior)
        self.btn_anterior.pack(side="left", padx=(0, 10))

        self.btn_proximo = ctk.CTkButton(self.botao_frame, text="Próximo", command=self.pagina_proximo)
        self.btn_proximo.pack(side="left", padx=(0, 40))

        self.btn_voltar = ctk.CTkButton(self.botao_frame, text="Editar", command=self.editar_agendamento)
        self.btn_voltar.pack(side="left", padx=(0, 10))  # Margem à direita

        self.btn_fechar = ctk.CTkButton(self.botao_frame, text="Voltar", command=self.voltar)
        self.btn_fechar.pack(side="left", padx=(0, 10))  # Margem à direita

        self.btn_excluir = ctk.CTkButton(self.botao_frame, text="Excluir", command=self.excluir_agendamento)
        self.btn_excluir.pack(side="left")

        # Chama a atualização da tabela após os botões terem sido criados
        self.atualizar_tabela()

    def atualizar_tabela(self):
    # Limpa a tabela antes de adicionar novos dados
        for row in self.tree.get_children():
            self.tree.delete(row)

        # Obtém a lista completa de agendamentos
        agendamentos = self.agendamento_repository.listar_agendamentos_por_usuario(self.usuario_id)
        self.total_agendamentos = len(agendamentos)

        # Calcula os índices para a página atual
        inicio = self.pagina_atual * self.itens_por_pagina
        fim = inicio + self.itens_por_pagina
        agendamentos_pagina = agendamentos[inicio:fim]

        for agendamento in agendamentos_pagina:
            if isinstance(agendamento.data, str):
                try:
                    data_agendamento = datetime.strptime(agendamento.data, "%Y-%m-%d")
                except ValueError:
                    data_agendamento = datetime.strptime(agendamento.data, "%d-%m-%Y")
            else:
                data_agendamento = agendamento.data

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

        # Atualiza o estado dos botões de navegação
        self.btn_anterior.configure(state="normal" if self.pagina_atual > 0 else "disabled")
        self.btn_proximo.configure(state="normal" if fim < self.total_agendamentos else "disabled")


    def editar_agendamento(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Erro", "Selecione um agendamento para editar.")
            return

        item_values = self.tree.item(selected_item, "values")
        id_agendamento = item_values[0]

        agendamento_selecionado = Agendamento(
            id=id_agendamento,
            nome=item_values[1],
            data=item_values[2],
            horario=item_values[3],
            local=item_values[4],
            descricao=item_values[5] if len(item_values) > 5 else ""
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

    def pagina_anterior(self):
        if self.pagina_atual > 0:
            self.pagina_atual -= 1
            self.atualizar_tabela()

    def pagina_proximo(self):
        if (self.pagina_atual + 1) * self.itens_por_pagina < self.total_agendamentos:
            self.pagina_atual += 1
            self.atualizar_tabela()
