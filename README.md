# Sistema de Agendamento

### Descrição do Projeto

O Sistema de Agendamento é um aplicativo desenvolvido em Python, com uma interface gráfica intuitiva criada utilizando a biblioteca CustomTkinter. Este projeto foi realizado como Trabalho de Conclusão da UC4 do curso de Desenvolvimento de Sistemas no SENAC.

Ele permite que os usuários gerenciem seus compromissos de maneira simples e eficiente. O sistema oferece funcionalidades como:
- Adição de novos compromissos
- Edição de compromissos existentes
- Exclusão de eventos
- Visualização detalhada de compromissos em um calendário.

---

### Tecnologias Utilizadas

- **Linguagem de Programação:** Python
- **Interface Gráfica:** CustomTkinter / Tkinter
- **Banco de Dados:** PostgreSQL

#### Bibliotecas Principais
- **[CustomTkinter](https://github.com/TomSchimansky/CustomTkinter):** Para criar interfaces mais personalizadas e atraentes.
- **[Tkcalendar](https://github.com/j4321/tkcalendar):** Para manipulação de calendários e seleção de datas.
- **[Pillow](https://pillow.readthedocs.io):** Para manipulação de imagens e adição de elementos visuais.
- **[Datetime](https://docs.python.org/3/library/datetime.html):** Para trabalhar com datas e horas.
- **[SQLAlchemy](https://www.sqlalchemy.org):** Para gerenciamento eficiente da conexão e manipulação do banco de dados.

---

### Requisitos

#### 1. Pré-requisitos

Certifique-se de ter as seguintes ferramentas instaladas no seu sistema:
- Python (3.8 ou superior)
- PostgreSQL (para o banco de dados)

#### 2. Instalação das Bibliotecas Necessárias

Instale as bibliotecas utilizando o pip:
```bash
pip install CustomTkinter tkcalendar Pillow psycopg2 SQLAlchemy
```

---

### Instalação do Projeto

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/Lduarte123/ProjetoFInalTkinter.git
   ```

2. **Navegue até o diretório do projeto:**
   ```bash
   cd ProjetoFInalTkinter
   ```

3. **Configure o Banco de Dados:**
   - Configure o PostgreSQL conforme as instruções do seu ambiente.
   - Certifique-se de criar o banco de dados e ajustar as credenciais no arquivo de configuração do projeto.

4. **Execute o script principal:**
   ```bash
   python app.py
   ```

---

### Como Usar

1. **Tela de Login:**
   - Ao abrir o sistema, insira suas credenciais para acessar.
   - Caso ainda não tenha cadastro, crie uma nova conta.

2. **Tela Principal:**
   - Adicione novos compromissos com a opção de escolha de datas e horários.
   - Edite ou exclua compromissos existentes de forma simples.
   - Utilize a visualização do calendário para gerenciar seus compromissos com mais clareza.

---

### Colaboração

Agradecemos as contribuições dos seguintes colaboradores:
- **Marcos Vitor** - [victorlima11](https://github.com/victorlima11)
- **Cauã Enzo** - [cauaenzo](https://github.com/cauaenzo)
- **Lucas Duarte** - [Lduarte123](https://github.com/Lduarte123/)
- **João Lucas** - [Joaolucasos169](https://github.com/Joaolucasos169)

---
