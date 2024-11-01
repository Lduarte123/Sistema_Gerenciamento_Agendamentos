import tkinter as tk
from tkinter import messagebox

def atualizar_usuario(self, usuario_id, nome, email, cidade, sexo, senha):
    # Verificação se todos os campos foram preenchidos
    if not all([nome, email, cidade, sexo, senha]):
        messagebox.showwarning("Erro", "Todos os campos devem ser preenchidos para atualizar o perfil.")
        return False

    # Pergunta ao usuário se ele tem certeza de que quer alterar os dados
    confirmacao = messagebox.askyesno("Confirmação", "Tem certeza de que deseja alterar os dados?")
    if not confirmacao:
        return False  # Caso o usuário selecione 'Não', a função é interrompida

    try:
        # Busca o usuário pelo ID
        usuario = self.session.query(UsuarioModel).filter_by(id=usuario_id).first()
        if usuario:
            # Atualiza os dados do usuário
            usuario.nome = nome
            usuario.email = email
            usuario.cidade = cidade
            usuario.sexo = sexo
            usuario.senha = senha
            self.session.commit()

            # Exibe uma mensagem de confirmação de edição concluída
            messagebox.showinfo("Sucesso", "Perfil atualizado com sucesso.")
            return True
        else:
            # Caso o usuário não seja encontrado, exibe uma mensagem de erro
            messagebox.showerror("Erro", constante.get_mensagem_usuario_nao_encontrado())
            return False
    except Exception as e:
        self.session.rollback()
        messagebox.showerror("Erro", "Ocorreu um erro ao atualizar o perfil. Tente novamente.")
        return False
