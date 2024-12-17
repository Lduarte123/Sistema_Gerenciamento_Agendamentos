import customtkinter as ctk
from tkinter import ttk, messagebox
from datetime import timedelta
from repository.agendamento_repository import AgendamentoRepository
from model.models import AgendamentoModel as Agendamento
from view.editar_agendamento_view import Editar
from datetime import datetime

class VisualizarFrame(ctk.CTkFrame):
    def __init__(self, master, agendamento_repository, usuario_id, filtro):
        super().__init__(master)
        self.agendamento_repository = agendamento_repository
        self.usuario_id = usuario_id

        self.pagina_atual = 0
        self.itens_por_pagina = 40
        self.total_agendamentos = 0

        
        self.pesquisa_frame = ctk.CTkFrame(self)
        self.pesquisa_frame.pack(pady=(20, 10))


        self.entry_pesquisa = ctk.CTkEntry(self.pesquisa_frame, placeholder_text="Digite sua pesquisa aqui", width=300)
        self.entry_pesquisa.pack(side="left", padx=(20, 10))

        self.btn_filtro = ctk.CTkButton(self.pesquisa_frame, text="Pesquisa", command=self.filtro_de_pesquisa)
        self.btn_filtro.pack(side="left", padx=(10, 20))
        
        self.tree = ttk.Treeview(self, columns=("id", "nome", "data", "horario", "local", "descricao", "status"), show='headings', height=42)

        # Definindo as colunas e cabeçalhos
        self.tree.heading("id", text="ID", command=lambda: self.ordenar("id"))
        self.tree.heading("nome", text="Nome", command=lambda: self.ordenar("nome"))
        self.tree.heading("data", text="Data", command=lambda: self.ordenar("data"))
        self.tree.heading("horario", text="Horário", command=lambda: self.ordenar("horario"))
        self.tree.heading("local", text="Local", command=lambda: self.ordenar("local"))
        self.tree.heading("descricao", text="Descrição", command=lambda: self.ordenar("descricao"))
        self.tree.heading("status", text="Status", command=lambda: self.ordenar("status"))


        self.tree.column("id", width=50)
        self.tree.column("nome", width=200)
        self.tree.column("data", width=100)
        self.tree.column("horario", width=100)
        self.tree.column("local", width=150)
        self.tree.column("descricao", width=200)
        self.tree.column("status", width=200)

        self.tree.pack(pady=20, fill="both", expand=False)

        self.botao_frame = ctk.CTkFrame(self)
        self.botao_frame.pack(pady=10)

        self.btn_anterior = ctk.CTkButton(self.botao_frame, text="Anterior", command=self.pagina_anterior)
        self.btn_anterior.pack(side="left", padx=(0, 10))

        self.btn_proximo = ctk.CTkButton(self.botao_frame, text="Próximo", command=self.pagina_proximo)
        self.btn_proximo.pack(side="left", padx=(0, 40))

        self.btn_voltar = ctk.CTkButton(self.botao_frame, text="Editar", command=self.editar_agendamento)
        self.btn_voltar.pack(side="left", padx=(0, 10))

        self.btn_fechar = ctk.CTkButton(self.botao_frame, text="Voltar", command=self.voltar)
        self.btn_fechar.pack(side="left", padx=(0, 10))

        self.btn_excluir = ctk.CTkButton(self.botao_frame, text="Excluir", command=self.excluir_agendamento)
        self.btn_excluir.pack(side="left")

        self.btn_cancelar = ctk.CTkButton(self.botao_frame, text="Cancelar Agendamento", command=self.cancelar_agendamento)
        self.btn_cancelar.pack(side="left", padx=(10, 20))

        self.atualizar_tabela()


        self.ordenacao_direcao = {coluna: True for coluna in ["id", "nome", "data", "horario", "local", "descricao", "status"]}

    def atualizar_tabela(self, agendamentos=None):
        for row in self.tree.get_children():
            self.tree.delete(row)
        if agendamentos is None:
            agendamentos = self.agendamento_repository.listar_agendamentos_por_usuario(self.usuario_id)
            
        self.total_agendamentos = len(agendamentos)

        inicio = self.pagina_atual * self.itens_por_pagina
        fim = inicio + self.itens_por_pagina
        agendamentos_pagina = agendamentos[inicio:fim]

        for agendamento in agendamentos_pagina:
            if isinstance(agendamento.data, str):
                try:
                    data_agendamento = datetime.strptime(agendamento.data, "%Y-%m-%d").date() 
                except ValueError:
                    data_agendamento = datetime.strptime(agendamento.data, "%d-%m-%Y").date() 
            elif isinstance(agendamento.data, datetime):
               data_agendamento = agendamento.data.date()
            else:
                data_agendamento = agendamento.data 

            data_formatada = data_agendamento.strftime("%d-%m-%Y")
            horario_formatado = agendamento.horario if isinstance(agendamento.horario, str) else agendamento.horario.strftime("%H:%M")

            data_atual = datetime.now().date()
            tags = ("Evento proximo",) if data_atual <= data_agendamento <= (data_atual + timedelta(days=2)) else ()
            
            self.tree.tag_configure("Evento proximo", foreground="red", font=("arial", 10, "bold"))
            if isinstance(agendamento.horario, str):
                horario_formatado = agendamento.horario
            else:
                horario_formatado = agendamento.horario.strftime("%H:%M")

            self.tree.insert('', 'end', values=(agendamento.id, agendamento.nome, data_formatada, horario_formatado, agendamento.local, agendamento.descricao, agendamento.status or "N/A"), tags=tags)

        self.btn_anterior.configure(state="normal" if self.pagina_atual > 0 else "disabled")
        self.btn_proximo.configure(state="normal" if fim < self.total_agendamentos else "disabled")

    def ordenar(self, coluna):
        self.ordenacao_direcao[coluna] = not self.ordenacao_direcao[coluna]
        
        agendamentos = self.agendamento_repository.listar_agendamentos_por_usuario(self.usuario_id)
        if coluna == "data":
            agendamentos.sort(key=lambda x: x.data if isinstance(x.data, datetime) else datetime.strptime(x.data, "%d-%m-%Y"), reverse=self.ordenacao_direcao[coluna])
        elif coluna == "horario":
            agendamentos.sort(key=lambda x: datetime.strptime(x.horario, "%H:%M"), reverse=self.ordenacao_direcao[coluna])
        else:
            agendamentos.sort(key=lambda x: getattr(x, coluna), reverse=self.ordenacao_direcao[coluna])
        self.total_agendamentos = len(agendamentos)
        self.pagina_atual = 0
        self.atualizar_tabela(agendamentos)

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

    def atualizar_agendamento_dados(self, novo_nome, nova_data, novo_horario, novo_local, nova_descricao="", novo_status=""):
        agendamento_atualizado = Agendamento(
            id=self.tree.item(self.tree.selection(), "values")[0],
            nome=novo_nome,
            data=nova_data,
            horario=novo_horario,
            local=novo_local,
            descricao=nova_descricao,
            status=novo_status
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

    def cancelar_agendamento(self):
        selected_item = self.tree.selection()
        if selected_item:
            confirmation = messagebox.askyesno("Confirmar Cancelamento", "Tem certeza que deseja cancelar este agendamento?")
            if confirmation:
                agendamento_id = self.get_agendamento_id()
                # Realiza o cancelamento no banco de dados
                self.agendamento_repository.cancelar_agendamento(agendamento_id)
                messagebox.showinfo("Sucesso", "Agendamento cancelado com sucesso!")
                # Atualiza a tabela para que o agendamento cancelado não apareça mais
                self.atualizar_tabela()
                return
        else:
            messagebox.showerror("Erro", "Selecione um agendamento para cancelar.")

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
    
    def filtro_de_pesquisa(self):
        termo_pesquisa = self.entry_pesquisa.get()
        if termo_pesquisa:
            resultados = self.agendamento_repository.obter_agendamentos_por_termo(termo_pesquisa)
            for item in self.tree.get_children():
                self.tree.delete(item)
            for agendamento in resultados:
                self.tree.insert("", "end", values=(agendamento.id, agendamento.nome, agendamento.data, 
                                                    agendamento.horario, agendamento.local, 
                                                    agendamento.descricao, agendamento.status))
        else:
            messagebox.showinfo("Informação", "Digite um termo para pesquisar.")
