import customtkinter as ctk
from tkinter import ttk, messagebox
from repository.usuario_repository import UsuarioRepository  # Repositório dos usuários
from model.models import UsuarioModel as Usuario, UsuarioModel
from datetime import datetime
from util.constantes import Constante

constante = Constante


class VisualizarUsuariosFrame(ctk.CTkFrame):
    def __init__(self, master, usuario_repo, usuarios=None):
        super().__init__(master)
        self.usuario_repo = usuario_repo

        # Configuração da Treeview
        self.tree = ttk.Treeview(self, columns=("id", "nome", "email", "data_nasc", "cidade", "sexo", "tipo"), show='headings', height=20)

        # Definindo as colunas e cabeçalhos
        self.tree.heading("id", text="ID")
        self.tree.heading("nome", text="Nome")
        self.tree.heading("email", text="Email")
        self.tree.heading("data_nasc", text="Data Nasc.")
        self.tree.heading("cidade", text="Cidade")
        self.tree.heading("sexo", text="Sexo")
        self.tree.heading("tipo", text="Tipo")

        self.tree.column("id", width=50)
        self.tree.column("nome", width=200)
        self.tree.column("email", width=200)
        self.tree.column("data_nasc", width=100)
        self.tree.column("cidade", width=150)
        self.tree.column("sexo", width=100)
        self.tree.column("tipo", width=100)

        self.tree.pack(pady=20, fill="both", expand=False)

        # Botão para editar
        self.botao_frame = ctk.CTkFrame(self)
        self.botao_frame.pack(pady=10)

        self.btn_fechar = ctk.CTkButton(self.botao_frame, text="Voltar", command=self.voltar)
        self.btn_fechar.pack(side="right", padx=(0, 10))

        self.btn_editar = ctk.CTkButton(self.botao_frame, text="Editar", command=self.editar_usuario)
        self.btn_editar.pack(side="left", padx=(0, 10))

        
        self.atualizar_tabela(usuarios)

    def atualizar_tabela(self, usuarios):
        """Atualiza a tabela com os usuários"""
        # Limpa a tabela antes de adicionar novos dados
        for row in self.tree.get_children():
            self.tree.delete(row)

        # Adiciona os usuários na tabela
        for usuario in usuarios:
            self.tree.insert('', 'end', values=(usuario.id, usuario.nome, usuario.email, usuario.data_nasc.strftime("%d-%m-%Y"), usuario.cidade, usuario.sexo, usuario.tipo))
    def editar_usuario(self):
        # Pega o item selecionado na Treeview
        selected_item = self.tree.selection()

        if not selected_item:
            messagebox.showwarning("Seleção", "Por favor, selecione um usuário para editar.")
            return

        # Obtém os valores do usuário selecionado
        usuario_id = self.tree.item(selected_item, 'values')[0]
        nome = self.tree.item(selected_item, 'values')[1]
        email = self.tree.item(selected_item, 'values')[2]
        data_nasc = self.tree.item(selected_item, 'values')[3]
        cidade = self.tree.item(selected_item, 'values')[4]
        sexo = self.tree.item(selected_item, 'values')[5]
        tipo = self.tree.item(selected_item, 'values')[6]

        # Cria uma nova janela de edição
        self.editar_window = ctk.CTkToplevel(self)
        self.editar_window.title("Editar Usuário")

        # Campos de entrada para edição
        self.entry_nome = ctk.CTkEntry(self.editar_window, placeholder_text="Nome")
        self.entry_nome.insert(0, nome)
        self.entry_nome.pack(padx=20, pady=5)

        self.entry_email = ctk.CTkEntry(self.editar_window, placeholder_text="Email")
        self.entry_email.insert(0, email)
        self.entry_email.pack(padx=20, pady=5)

        self.entry_data_nasc = ctk.CTkEntry(self.editar_window, placeholder_text="Data Nasc.")
        self.entry_data_nasc.insert(0, data_nasc)
        self.entry_data_nasc.pack(padx=20, pady=5)

        self.entry_cidade = ctk.CTkEntry(self.editar_window, placeholder_text="Cidade")
        self.entry_cidade.insert(0, cidade)
        self.entry_cidade.pack(padx=20, pady=5)

        self.entry_sexo = ctk.CTkEntry(self.editar_window, placeholder_text="Sexo")
        self.entry_sexo.insert(0, sexo)
        self.entry_sexo.pack(padx=20, pady=5)

        self.entry_tipo = ctk.CTkEntry(self.editar_window, placeholder_text="Tipo")
        self.entry_tipo.insert(0, tipo)
        self.entry_tipo.pack(padx=20, pady=5)

        self.entry_senha = ctk.CTkEntry(self.editar_window, placeholder_text="Senha", show="*")
        self.entry_senha.pack(padx=20, pady=5)

        # Botões para Salvar ou Cancelar
        self.botao_frame = ctk.CTkFrame(self.editar_window)
        self.botao_frame.pack(pady=20)

        self.btn_salvar = ctk.CTkButton(self.botao_frame, text="Salvar", command=lambda: self.salvar_usuario(usuario_id))
        self.btn_salvar.pack(side="left", padx=10)

        self.btn_cancelar = ctk.CTkButton(self.botao_frame, text="Cancelar", command=self.editar_window.destroy)
        self.btn_cancelar.pack(side="right", padx=10)

    def salvar_usuario(self, usuario_id):
        # Coleta os dados do formulário
        nome = self.entry_nome.get()
        email = self.entry_email.get()
        data_nasc = self.entry_data_nasc.get()
        cidade = self.entry_cidade.get()
        sexo = self.entry_sexo.get()
        tipo = self.entry_tipo.get()
        senha = self.entry_senha.get()  # Se o campo de senha for editável

        # Verifica se os campos obrigatórios estão preenchidos
        if not nome or not email or not data_nasc:
            messagebox.showwarning("Campos obrigatórios", "Por favor, preencha todos os campos obrigatórios.")
            return

        # Tenta converter a data de nascimento para o formato datetime (caso necessário)
        try:
            data_nasc = datetime.strptime(data_nasc, "%d-%m-%Y")
        except ValueError:
            messagebox.showerror("Data inválida", "Por favor, insira a data no formato DD-MM-AAAA.")
            return

        # Agora, chamamos o método atualizar_usuario do repositório, passando os parâmetros
        usuario_atualizado = self.usuario_repo.atualizar_usuario(
            usuario_id, nome, email, cidade, sexo, senha
        )

        # Fechar a janela de edição
        self.editar_window.destroy()

        # Atualizar a tabela de usuários (você já tem esse método)
        self.atualizar_tabela(self.usuario_repo.listar_usuarios())

        # Exibir uma mensagem de sucesso
        messagebox.showinfo("Sucesso", "Usuário atualizado com sucesso!")

    def atualizar_usuario(self, usuario_id, nome, email, cidade, sexo, senha):
        try:
            # Busca o usuário no banco de dados usando o ID
            usuario = self.session.query(UsuarioModel).filter_by(id=usuario_id).first()

            if usuario:
                # Atualiza os campos do usuário
                usuario.nome = nome
                usuario.email = email
                usuario.cidade = cidade
                usuario.sexo = sexo
                usuario.senha = senha  # Atualiza a senha se necessário

                # Commit na sessão para salvar as mudanças no banco
                self.session.commit()

                # Mensagem de sucesso
                messagebox.showinfo("Sucesso", "Perfil atualizado com sucesso.")
                return True
            else:
                # Caso o usuário não seja encontrado, exibe uma mensagem de erro
                print(constante.get_mensagem_usuario_nao_encontrado())
                messagebox.showerror("Erro", constante.get_mensagem_usuario_nao_encontrado())

                return False
        except Exception as e:
            # Se ocorrer qualquer erro, exibe uma mensagem de erro
            messagebox.showerror("Erro", f"Ocorreu um erro ao atualizar o usuário: {str(e)}")
            return False
    def voltar(self):
        self.master.controller.exibir_tela_inicial()

    
