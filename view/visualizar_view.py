import customtkinter as ctk
from tkinter import ttk, messagebox
from repository.agendamento_repository import AgendamentoRepository
from model.models import AgendamentoModel as Agendamento
from view.editar_agendamento_view import Editar
from datetime import datetime, timedelta
from services.emails import VerificacaoEmail
import schedule
import time
import threading

class VisualizarFrame(ctk.CTkFrame):  # visualização em treeview
    def __init__(self, master, agendamento_repository, usuario_id, filtro):
        super().__init__(master)
        self.agendamento_repository = agendamento_repository
        self.usuario_id = usuario_id

        self.pagina_atual = 0
        self.itens_por_pagina = 40
        self.total_agendamentos = 0

        
        self.pesquisa_frame = ctk.CTkFrame(self)
        self.pesquisa_frame.pack(pady=(20, 10))  # Adiciona algum espaço ao redor


        self.entry_pesquisa = ctk.CTkEntry(self.pesquisa_frame, placeholder_text="Digite sua pesquisa aqui", width=300)
        self.entry_pesquisa.pack(side="left", padx=(20, 10))  # Ajusta o espaçamento do entry
                # Configuração da Treeview
        self.btn_filtro = ctk.CTkButton(self.pesquisa_frame, text="Pesquisa", command=self.filtro_de_pesquisa)
        self.btn_filtro.pack(side="left", padx=(10, 20))  # Ajusta o espaçamento do botão

        # Campo de entrada para pesquisa
        
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
        self.tree.column("status", width=200) #Adicionei coluna status

        self.tree.pack(pady=20, fill="both", expand=False)

        # Frame para os botões
        # Frame para os botões
        self.botao_frame = ctk.CTkFrame(self)
        self.botao_frame.pack(pady=10)

        # Botão de pesquisa (movido para a parte superior)
        # self.btn_filtro = ctk.CTkButton(self, text="Pesquisa", command=self.filtro_de_pesquisa)
        # self.btn_filtro.pack(side="top", padx=(20, 30), pady=(20, 10))  # Adicionei margens para espaçamento

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

        # Substituindo o botão de envio de código por e-mail
        self.btn_enviar_lembrete_email = ctk.CTkButton(self.botao_frame, text="Enviar Lembrete por E-mail", command=self.enviar_lembrete_email)
        self.btn_enviar_lembrete_email.pack(side="left", padx=(10, 20))
        
        # Iniciar o agendador em uma thread separada
        threading.Thread(target=self.iniciar_agendador, daemon=True).start()

                # Chama a atualização da tabela após os botões terem sido criados
        self.atualizar_tabela()

        # Inicializa a direção de ordenação
        self.ordenacao_direcao = {coluna: True for coluna in ["id", "nome", "data", "horario", "local", "descricao", "status"]}

    def atualizar_tabela(self, agendamentos=None):
        """Atualiza a tabela de agendamentos com os dados mais recentes."""
        # Limpa a tabela antes de adicionar novos dados
        for row in self.tree.get_children():
            self.tree.delete(row)

        # Obtém a lista completa de agendamentos, se não for fornecida
        if agendamentos is None:
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

            # Insere os dados formatados na tabela, incluindo a descrição
            self.tree.insert('', 'end', values=(agendamento.id, agendamento.nome, data_formatada, horario_formatado, agendamento.local, agendamento.descricao, agendamento.status))

        # Atualiza o estado dos botões de navegação
        self.btn_anterior.configure(state="normal" if self.pagina_atual > 0 else "disabled")
        self.btn_proximo.configure(state="normal" if fim < self.total_agendamentos else "disabled")

    def ordenar(self, coluna):
        """Ordena a Treeview com base na coluna selecionada."""
        # Alterna a direção de ordenação
        self.ordenacao_direcao[coluna] = not self.ordenacao_direcao[coluna]

        # Obtém a lista completa de agendamentos
        agendamentos = self.agendamento_repository.listar_agendamentos_por_usuario(self.usuario_id)

        # Verifica o tipo de coluna e define a chave de ordenação
        if coluna == "data":
            # Para data, verifica se já é um objeto datetime.date
            agendamentos.sort(key=lambda x: x.data if isinstance(x.data, datetime) else datetime.strptime(x.data, "%d-%m-%Y"), reverse=self.ordenacao_direcao[coluna])
        elif coluna == "horario":
            # Para horário, converte para um objeto de hora
            agendamentos.sort(key=lambda x: datetime.strptime(x.horario, "%H:%M"), reverse=self.ordenacao_direcao[coluna])
        else:
            # Para outras colunas, utiliza o atributo diretamente
            agendamentos.sort(key=lambda x: getattr(x, coluna), reverse=self.ordenacao_direcao[coluna])

        # Atualiza a tabela com a lista ordenada
        self.total_agendamentos = len(agendamentos)
        self.pagina_atual = 0  # Reseta para a primeira página após a ordenação
        self.atualizar_tabela(agendamentos)  # Atualiza a tabela com os agendamentos ordenados

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
            # Aqui você deve chamar o repositório para obter os resultados filtrados.
            resultados = self.agendamento_repository.obter_agendamentos_por_termo(termo_pesquisa)
            
            # Limpe a treeview antes de inserir novos resultados
            for item in self.tree.get_children():
                self.tree.delete(item)
            
            # Popule a treeview com os resultados filtrados
            for agendamento in resultados:
                self.tree.insert("", "end", values=(agendamento.id, agendamento.nome, agendamento.data, 
                                                    agendamento.horario, agendamento.local, 
                                                    agendamento.descricao, agendamento.status))
        else:
            messagebox.showinfo("Informação", "Digite um termo para pesquisar.")

    def iniciar_agendador(self):
        # Agendar a verificação para ser executada a cada dia
        schedule.every().day.at("09:00").do(self.verificar_agendamentos_proximos)

        while True:
            schedule.run_pending()
            time.sleep(1)

    def verificar_agendamentos_proximos(self):
        """Verifica se há agendamentos que começam em 5 dias e envia o código."""
        agendamentos_proximos = self.obter_agendamentos_proximos()

        for agendamento in agendamentos_proximos:
            if hasattr(agendamento, 'email'):
                # Cria uma instância da classe VerificacaoEmail e envia o código
                verificacao_email = VerificacaoEmail(agendamento.email)
                verificacao_email.solicitar_codigo_verificacao(self)

                print(f"Código de verificação enviado para {agendamento.email}.")
            else:
                print(f"O agendamento com ID {agendamento.id} não possui um e-mail associado.")

    def enviar_lembrete_email(self):
        """Envia lembretes de e-mail para os agendamentos que começam em 5 dias."""
        agendamentos_proximos = self.obter_agendamentos_proximos()

        if not agendamentos_proximos:
            messagebox.showinfo("Sem agendamentos próximos", "Não há agendamentos dentro dos próximos 5 dias.")
            return

        for agendamento in agendamentos_proximos:
            if hasattr(agendamento, 'email'):
                # Instancia a classe VerificacaoEmail e envia o lembrete
                verificacao_email = VerificacaoEmail(agendamento.email)
                try:
                    verificacao_email.solicitar_codigo_verificacao(self)  # Isso enviará o e-mail
                    messagebox.showinfo("Lembrete Enviado", f"Lembrete enviado para {agendamento.email}.")
                except Exception as e:
                    messagebox.showerror("Erro ao Enviar", f"Não foi possível enviar o lembrete para {agendamento.email}. Erro: {str(e)}")
            else:
                messagebox.showerror("Erro", f"O agendamento com ID {agendamento.id} não possui um e-mail associado.")

    def obter_agendamentos_proximos(self):
        """Retorna os agendamentos que ocorrem nos próximos 5 dias."""
        agendamentos = self.agendamento_repository.listar_agendamentos_por_usuario(self.usuario_id)
        agendamentos_proximos = []

        hoje = datetime.today()
        for agendamento in agendamentos:
            if isinstance(agendamento.data, str):
                data_agendamento = datetime.strptime(agendamento.data, "%Y-%m-%d")  # Ajuste o formato conforme necessário
            else:
                data_agendamento = agendamento.data

            # Verifica se o agendamento ocorre exatamente em 5 dias
            if hoje + timedelta(days=5) == data_agendamento:
                agendamentos_proximos.append(agendamento)

        return agendamentos_proximos
