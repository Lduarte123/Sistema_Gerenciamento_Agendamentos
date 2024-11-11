import customtkinter as ctk
from tkinter import ttk, messagebox
from repository.usuario_repository import UsuarioRepository  # Repositório dos usuários
from model.models import UsuarioModel as Usuario
from datetime import datetime

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

        # Botão de Excluir
        self.btn_excluir = ctk.CTkButton(self.botao_frame, text="Excluir", command=self.excluir_usuario)
        self.btn_excluir.pack(side="right", padx=(0, 10))


        
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
        pass

    def voltar(self):
        self.master.controller.exibir_tela_inicial()


    def excluir_usuario(self):
        # Verifica se algum item foi selecionado na Treeview
        item_selecionado = self.tree.selection()
        if item_selecionado:
            # Exibe uma mensagem de confirmação antes de excluir
            confirmation = messagebox.askyesno("Confirmar Exclusão", "Tem certeza que deseja excluir este usuário?")
            if confirmation:
                # Obtém o ID do usuário selecionado
                usuario_id = self.tree.item(item_selecionado[0], "values")[0]
                
                # Chama o método excluir_usuario do repositório
                if self.usuario_repo.excluir_usuario(usuario_id):
                    messagebox.showinfo("Sucesso", "Usuário excluído com sucesso!")
                    self.atualizar_tabela(self.usuario_repo.listar_usuarios())  # Atualiza a tabela
                else:
                    messagebox.showerror("Erro", "Erro ao excluir o usuário. Tente novamente.")
                return
        
        # Caso nenhum item tenha sido selecionado
        messagebox.showerror("Erro", "Selecione um usuário para excluir.")
