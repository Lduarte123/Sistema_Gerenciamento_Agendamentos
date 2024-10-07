from config import create_connection

class UsuarioRepository:
    def __init__(self):
        self.connection = create_connection()

    def validar_usuario(self, email, senha):
        try:
            # Reabre a conexão caso ela tenha sido fechada
            if self.connection.closed:
                self.connection = create_connection()

            with self.connection.cursor() as cursor:
                cursor.execute("SELECT * FROM usuarios WHERE email = %s AND senha = %s", (email, senha))
                return cursor.fetchone() is not None
        except Exception as e:
            print(f"Erro ao validar usuário: {e}")
            return False


    def registrar_usuario(self, nome, email, senha, data_nasc, cidade, sexo):
        try:
            cursor = self.connection.cursor()
            # Ajustando os marcadores de posição para o PostgreSQL
            sql = "INSERT INTO usuarios (nome, email, senha, data_nasc, cidade, sexo) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (nome, email, senha, data_nasc, cidade, sexo))
            
            self.connection.commit()
            return True  # Sucesso
            
        except Exception as e:
            print(f"Erro ao registrar usuário: {e}")  # Exibe o erro no console
            self.connection.rollback()  # Reverte a operação se houver um erro
            return False  # Indica falha no registro
        
    def obter_emails_cadastrados(self):
        """Obtém todos os e-mails cadastrados no banco de dados."""
        try:
            query = "SELECT email FROM usuarios"
            cursor = self.connection.cursor()
            cursor.execute(query)
            # Armazena todos os e-mails em uma lista
            emails = [row[0] for row in cursor.fetchall()]
            cursor.close()
            return emails
        except Exception as e:
            print(f"Erro ao obter e-mails: {e}")
            return []  # Retorna uma lista vazia em caso de erro


