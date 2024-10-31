class Constante:
    def __init__(self):
        # EMAIL SERVICE
        self._CODIGO_NAO_GERADO = "Código não gerado."
        self._MENSAGEM_EMAIL = "Seu código de verificação é:"
        self._ASSUNTO_EMAIL = "Código de Verificação"
        self._EMAIL_REMETENTE = "projetodeagendamentos@gmail.com"
        self._EMAIL_SENHA = "xaqh roat ndyq ajol"
        self._SMTP_SERVIDOR = "smtp.gmail.com"
        self._SMTP_PORTA = 587
        self._TITULO_JANELA = "Código de Verificação"
        self._MENSAGEM_JANELA = "Digite o código enviado para seu e-mail:"

        # TRATAMENTO DE ERRO
        self.ERRO_USUARIO_ID_NAO_DEFINIDO = "Erro: usuario_id não está definido."
        self.ERRO_USUARIO_NAO_ENCONTRADO = "Erro: usuário não encontrado."
        self.MENSAGEM_ERRO_CAMPO_OBRIGATORIO = "Preencha todos os campos obrigatórios."
        self.MENSAGEM_ERRO_REGISTRO = "Erro ao registrar usuário"
        self.MENSAGEM_USUARIO_NAO_ENCONTRADO = "Usuário não encontrado."
        self.MENSAGEM_ERRO_FORMATO_HORARIO = "Horário deve ser no formato HH:MM."
        self.MENSAGEM_ERRO_FORMATO_DATA = "Formato de data inválido."
        self.MENSAGEM_ERRO_DATA_PASSADA = "A data selecionada já passou."
        self.MENSAGEM_ERRO_CODIGO_INVALIDO = "Código de verificação inválido."

        self.MENSAGEM_SUCESSO_REGISTRO = "Usuário registrado com sucesso."
        self.MENSAGEM_SUCESSO = "Agendamento criado!"

        # TEXTO
        self.TITULO_JANELA_CRIAR = "Criar Agendamento"
        self.TEXTO_NOME_EVENTO = "Nome do Evento*:"
        self.TEXTO_HORARIO = "Horário (HH:MM)*:"
        self.TEXTO_DATA = "Data*:"
        self.TEXTO_LOCALIZACAO = "Localização*:"
        self.TEXTO_DESCRICAO = "Descrição:"

        # DATA BASE
        self.TABELA_USUARIOS = "usuarios"
        self.TABELA_AGENDAMENTOS = "agendamentos"
        self.STATUS_CANCELADO = "Cancelado"
        
        # GLOBAL STRINGS
        self.ERRO =  "Erro"
        self.SUCESSO = "Sucesso"
        self.TEXTO_BOTAO_SALVAR = "Salvar"
        self.TEXTO_BOTAO_VOLTAR = "Voltar"
        self.TITULO_GERENCIAMENTO = "Gerenciamento de Agendamentos"

        # BOTÕES
        self.BOTAO_AGENDAR = "Agendar"
        self.BOTAO_VISUALIZAR = "Visualizar"
        self.BOTAO_PERFIL = "Perfil"

        # FONTES
        self.FONT_TITULO = ("Arial", 20, "bold")
        self.FONT_RELOGIO = ("Arial", 24, "bold")
        self.FONT_DATA = ("Arial", 16, "bold")

    def get_codigo_nao_gerado(self):
        return self._CODIGO_NAO_GERADO
    
    def get_mensagem_email(self):
        return self._MENSAGEM_EMAIL

    def get_assunto_email(self):
        return self._ASSUNTO_EMAIL

    def get_email_remetente(self):
        return self._EMAIL_REMETENTE

    def get_email_senha(self):
        return self._EMAIL_SENHA

    def get_smtp_servidor(self):
        return self._SMTP_SERVIDOR

    def get_smtp_porta(self):
        return self._SMTP_PORTA

    def get_titulo_janela(self):
        return self._TITULO_JANELA

    def get_mensagem_janela(self):
        return self._MENSAGEM_JANELA
    
    def get_erro_usuario_nao_encontrado(self):
        return self.ERRO_USUARIO_NAO_ENCONTRADO

    def get_erro_usuario_id_nao_definido(self):
        return self.ERRO_USUARIO_ID_NAO_DEFINIDO
    
    def get_tabela_usuarios(self):
        return self.TABELA_USUARIOS

    def get_tabela_agendamentos(self):
        return self.TABELA_AGENDAMENTOS
    
    def get_status_cancelado(self):
        return self.STATUS_CANCELADO
    
    def get_mensagem_erro_registro(self):
        return self.MENSAGEM_ERRO_REGISTRO

    def get_mensagem_sucesso_registro(self):
        return self.MENSAGEM_SUCESSO_REGISTRO

    def get_mensagem_usuario_nao_encontrado(self):
        return self.MENSAGEM_USUARIO_NAO_ENCONTRADO
    
    def get_titulo_janela_criar(self):
        return self.TITULO_JANELA_CRIAR

    def get_texto_nome_evento(self):
        return self.TEXTO_NOME_EVENTO

    def get_texto_horario(self):
        return self.TEXTO_HORARIO

    def get_texto_data(self):
        return self.TEXTO_DATA

    def get_texto_localizacao(self):
        return self.TEXTO_LOCALIZACAO

    def get_texto_descricao(self):
        return self.TEXTO_DESCRICAO

    def get_texto_botao_salvar(self):
        return self.TEXTO_BOTAO_SALVAR

    def get_texto_botao_voltar(self):
        return self.TEXTO_BOTAO_VOLTAR

    def get_mensagem_erro_campo_obrigatorio(self):
        return self.MENSAGEM_ERRO_CAMPO_OBRIGATORIO

    def get_mensagem_sucesso(self):
        return self.MENSAGEM_SUCESSO

    def get_mensagem_erro_formato_horario(self):
        return self.MENSAGEM_ERRO_FORMATO_HORARIO

    def get_mensagem_erro_data_passada(self):
        return self.MENSAGEM_ERRO_DATA_PASSADA

    def get_mensagem_erro_codigo_invalido(self):
        return self.MENSAGEM_ERRO_CODIGO_INVALIDO
    
    def get_sucesso(self):
        return self.SUCESSO
    
    def get_erro(self):
        return self.ERRO
    
    def get_mensagem_erro_formato_data(self):
        return self.MENSAGEM_ERRO_FORMATO_DATA
    
    def get_titulo_gerenciamento(self):
        return self.TITULO_GERENCIAMENTO

    def get_botao_agendar(self):
        return self.BOTAO_AGENDAR

    def get_botao_visualizar(self):
        return self.BOTAO_VISUALIZAR

    def get_botao_perfil(self):
        return self.BOTAO_PERFIL

    def get_fonte(self):
        return self.FONT_TITULO

    def get_fonte_relogio(self):
        return self.FONT_RELOGIO

    def get_fonte_data(self):
        return self.FONT_DATA

