import psycopg2
from config import create_connection
from model.agendamento import AgendamentoModel 
from datetime import datetime, time  # Certifique-se de importar 'time' também

class AgendamentoRepository:
    def __init__(self):
        self.conn = create_connection()

    def salvar_agendamento(self, agendamento):
        try:
            with self.conn.cursor() as cursor:
                # Debug: Imprimindo todos os campos do agendamento
                print(f"Nome: {agendamento.nome}")  # Nome do agendamento
                print(f"Data original: {agendamento.data}")  # Data do agendamento
                print(f"Horário original: {agendamento.horario}")  # Horário do agendamento
                print(f"Local: {agendamento.local}")  # Local do agendamento
                print(f"Descrição: {agendamento.descricao}")  # Descrição do agendamento

                # Se agendamento.data for um datetime, você pode fazer o seguinte
                if isinstance(agendamento.data, datetime):
                    data = agendamento.data.date()  # Pega apenas a data
                else:
                    data = datetime.strptime(agendamento.data, "%d-%m-%Y").date()  # Se for string, converte

                # Verificando o tipo de agendamento.horario
                if isinstance(agendamento.horario, str):
                    horario = datetime.strptime(agendamento.horario, "%H:%M").time()  # Converte a string de horário para time
                elif isinstance(agendamento.horario, time):  # Verifique se `time` está importado corretamente
                    horario = agendamento.horario  # Se já é um objeto time, usa como está
                else:
                    raise ValueError("Horário deve ser uma string no formato HH:MM ou um objeto time")

                print(f"Data convertida: {data}")  # Debug: mostra a data convertida
                print(f"Horário convertido: {horario}")  # Debug: mostra o horário convertido

                query = """
                INSERT INTO agendamentos (nome, data, horario, local, descricao)
                VALUES (%s, %s, %s, %s, %s)
                """
                cursor.execute(query, (agendamento.nome, data, horario, agendamento.local, agendamento.descricao))
            self.conn.commit()
            print("Agendamento salvo com sucesso!")  # Mensagem de sucesso
        except Exception as e:
            print(f"Erro ao salvar agendamento: {e}")
            self.conn.rollback()

    def listar_agendamentos(self):
        try:
            with self.conn.cursor() as cursor:
                cursor.execute("SELECT id, nome, data, horario, local, descricao FROM agendamentos")
                resultados = cursor.fetchall()

                agendamentos = []
                for row in resultados:
                    # Atribua os valores retornados aos atributos corretos
                    agendamento = AgendamentoModel(id=row[0], nome=row[1], data=row[2], horario=row[3], local=row[4], descricao=row[5])
                    agendamentos.append(agendamento)

                return agendamentos
        except Exception as e:
            print(f"Erro ao listar agendamentos: {e}")
            return []



    def fechar_conexao(self):
        self.conn.close()
    
    def atualizar_agendamento_dados(self, novo_nome, nova_data, novo_horario, novo_local, nova_descricao=""):  # Descrição agora é um parâmetro
        agendamento_atualizado = AgendamentoModel(
            id=self.tree.item(self.tree.selection(), "values")[0],
            nome=novo_nome,
            data=nova_data,
            horario=novo_horario,
            local=novo_local,
            descricao=nova_descricao  # Inclua a nova descrição
        )

        # Atualiza o agendamento no repositório
        self.agendamento_repository.atualizar_agendamento(agendamento_atualizado)
        self.atualizar_tabela()


    
    def excluir_agendamento(self, agendamento_id):
        try:
            with self.conn:
                cursor = self.conn.cursor()
                cursor.execute(
                    "DELETE FROM agendamentos WHERE id = %s",
                    (agendamento_id,)
                )
            self.conn.commit()
        except Exception as e:
            print(f"Erro ao excluir agendamento: {e}")
            self.conn.rollback()
