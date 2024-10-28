import customtkinter as ctk
from tkcalendar import Calendar
from tkinter import messagebox
from datetime import datetime
import re
from repository.agendamento_repository import AgendamentoRepository
from model.agendamento import AgendamentoModel as Agendamento
from model.emails import VerificacaoEmail

class CriarAgendamentoFrame(ctk.CTkFrame):
    def __init__(self, master, agendamento_model, controller, usuario_id):
        super().__init__(master)
        self.agendamento_model = agendamento_model
        self.controller = controller
        self.usuario_id = usuario_id

        self.agendamento_repository = AgendamentoRepository()
        self.configure(width=300, height=400)

        self.verificacao_email = VerificacaoEmail("projetodeagendamentos@gmail.com")

        # Cria um frame interno para centralização
        self.frame_interno = ctk.CTkFrame(self)
        self.frame_interno.pack(expand=True)  # Usar pack com expand para centralizar o frame

        self.label_titulo = ctk.CTkLabel(self.frame_interno, text="Criar Agendamento", font=("Arial", 20, "bold"))
        self.label_titulo.grid(row=0, column=0, pady=(10, 10))

        self.label_nome = ctk.CTkLabel(self.frame_interno, text="Nome do Evento*:") 
        self.label_nome.grid(row=1, column=0, padx=10, pady=(10, 5), sticky="w")
        self.entrada_nome = ctk.CTkEntry(self.frame_interno, placeholder_text="Nome do Evento", width=250)
        self.entrada_nome.grid(row=2, column=0, padx=10, pady=5)

        self.label_horario = ctk.CTkLabel(self.frame_interno, text="Horário (HH:MM)*:")
        self.label_horario.grid(row=3, column=0, padx=10, pady=(10, 5), sticky="w")
        self.entrada_horario = ctk.CTkEntry(self.frame_interno, placeholder_text="HH:MM", width=250)
        self.entrada_horario.grid(row=4, column=0, padx=10, pady=5)

        self.label_data = ctk.CTkLabel(self.frame_interno, text="Data*:") 
        self.label_data.grid(row=5, column=0, padx=10, pady=(10, 5), sticky="w")
        self.calendario = Calendar(self.frame_interno, selectmode='day', width=250)
        self.calendario.grid(row=6, column=0, padx=10, pady=5)

        self.label_descricao = ctk.CTkLabel(self.frame_interno, text="Descrição:") 
        self.label_descricao.grid(row=9, column=0, padx=10, pady=(10, 5), sticky="w")
        self.entrada_descricao = ctk.CTkEntry(self.frame_interno, placeholder_text="Descrição do Evento", width=250)
        self.entrada_descricao.grid(row=10, column=0, padx=10, pady=5)

        self.label_localizacao = ctk.CTkLabel(self.frame_interno, text="Localização*:") 
        self.label_localizacao.grid(row=7, column=0, padx=10, pady=(10, 5), sticky="w")
        self.entrada_localizacao = ctk.CTkEntry(self.frame_interno, placeholder_text="Localização", width=250)
        self.entrada_localizacao.grid(row=8, column=0, padx=10, pady=5)

        self.frame_botoes = ctk.CTkFrame(self.frame_interno, fg_color='transparent')
        self.frame_botoes.grid(row=11, column=0, pady=10)

        self.botao_salvar = ctk.CTkButton(self.frame_botoes, text="Salvar", command=self.salvar, width=60)
        self.botao_salvar.grid(row=0, column=0, padx=(0, 5))

        self.botao_voltar = ctk.CTkButton(self.frame_botoes, text="Voltar", command=self.voltar, width=60)
        self.botao_voltar.grid(row=0, column=1)

        # Configura o frame interno para ocupar espaço
        self.frame_interno.grid_rowconfigure(0, weight=1) 
        self.frame_interno.grid_columnconfigure(0, weight=1) 

        self.pack_propagate(False)
        self.pack(expand=True)

    def voltar(self):
        self.master.controller.exibir_tela_inicial()

    def salvar(self):
        nome = self.entrada_nome.get().strip()  # Nome em string
        data = self.calendario.get_date().strip()  # Data em string (MM/DD/AA ou MM/DD/YYYY)
        horario = self.entrada_horario.get().strip()  # Horário em string (HH:MM)
        local = self.entrada_localizacao.get().strip()  # Local em string
        descricao = self.entrada_descricao.get()  # Descrição em string

        # Validação do horário
        if not re.match(r'^(?:[01]\d|2[0-3]):[0-5]\d$', horario):
            messagebox.showerror("Erro", "Horário deve ser no formato HH:MM.", parent=self)
            return

        # Verificação da data e conversão
        try:
            print(f"Data recebida: {data}")  # Depuração

            # Conversão da data para o formato correto
            if len(data.split('/')[-1]) == 2:  # Se o ano tem 2 dígitos
                data_agendamento = datetime.strptime(data, "%m/%d/%y")  # MM/DD/AA
            else:
                data_agendamento = datetime.strptime(data, "%m/%d/%Y")  # MM/DD/YYYY

            # Verificando se a data não está no passado
            data_hora_atual = datetime.now()
            if data_agendamento.date() < data_hora_atual.date():
                messagebox.showerror("Erro", "A data selecionada já passou.")
                return

            # Verificando se o horário não passou no mesmo dia
            if data_agendamento.date() == data_hora_atual.date() and data_agendamento.time() < data_hora_atual.time():
                messagebox.showerror("Erro", "O horário selecionado já passou.")
                return

        except ValueError:
            messagebox.showerror("Erro", "Formato de data inválido. Use MM/DD/AAAA ou MM/DD/AA.")
            return

        # Validação para garantir que os campos obrigatórios estejam preenchidos
        if not all([nome, data, horario, local]):
            messagebox.showerror("Erro", "Preencha todos os campos obrigatórios.")
            return

        # Convertendo a data para o formato desejado (DD-MM-AAAA)
        data_formatada = data_agendamento.strftime("%d-%m-%Y")  # Formato como string para o banco de dados

        codigo_inserido = self.verificacao_email.solicitar_codigo_verificacao()
        if codigo_inserido is None or not self.verificacao_email.validar_codigo(codigo_inserido):
            messagebox.showerror("Erro", "Código de verificação inválido.")
            return

        # Criar o objeto agendamento com o usuário associado
        agendamento = Agendamento(
            nome=nome,
            data=data_formatada,
            horario=horario,
            local=local,
            descricao=descricao or "",
            usuario_id=self.usuario_id  # Adiciona o ID do usuário
        )

        try:
            # Salvar o agendamento no banco de dados, passando o usuario_id
            self.agendamento_repository.salvar_agendamento(agendamento)

            # Mostrar mensagem de sucesso
            messagebox.showinfo("Sucesso", f"Agendamento criado!\nNome: {agendamento.nome}\nLocal: {agendamento.local}\nData: {data_formatada}\nHorário: {horario}")

            # Retornar para a tela inicial
            self.master.controller.exibir_tela_inicial()

        except Exception as e:
            # Imprimir o erro no console para depuração
            print(f"Ocorreu um erro ao salvar o agendamento: {e}")
            
            # Exibir mensagem de erro na interface
            messagebox.showerror("Erro", f"Ocorreu um erro ao salvar o agendamento: {str(e)}")

