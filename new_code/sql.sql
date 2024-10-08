CREATE TABLE construtora (
  id INT NOT NULL PRIMARY KEY,
  nome VARCHAR(100),
  cnpj VARCHAR(14) UNIQUE,
  endereco VARCHAR(255),
  telefone VARCHAR(15)
);
CREATE TABLE pessoa (
  id INT NOT NULL PRIMARY KEY,
  nome VARCHAR(100),
  cpf VARCHAR(11) UNIQUE,
  data_nascimento DATE,
  telefone VARCHAR(15)
);
CREATE TABLE condominio (
  id INT NOT NULL PRIMARY KEY,
  nome VARCHAR(100),
  cidade VARCHAR(100),
  estado VARCHAR(50),
  id_construtora INT,
  FOREIGN KEY (id_construtora) REFERENCES construtora(id)
);
CREATE TABLE casa (
  id INT NOT NULL PRIMARY KEY,
  numero INT,
  area DECIMAL(10, 2),
  id_condominio INT,
  id_pessoa INT,
  FOREIGN KEY (id_condominio) REFERENCES condominio(id),
  FOREIGN KEY (id_pessoa) REFERENCES pessoa(id)
);

-----TABELA CONSTRUTORA--------------------
INSERT INTO construtora (id, nome, cnpj, endereco, telefone) VALUES (1, 'Construtora Alpha', '12345678000101', 'Rua das Flores, 100', '11987654321');
INSERT INTO construtora (id, nome, cnpj, endereco, telefone) VALUES (2, 'Construtora Beta', '23456789000112', 'Avenida Central, 200', '11987654322');
INSERT INTO construtora (id, nome, cnpj, endereco, telefone) VALUES (3, 'Construtora Gama', '34567890000123', 'Rua dos Limoeiros, 300', '11987654323');
INSERT INTO construtora (id, nome, cnpj, endereco, telefone) VALUES (4, 'Construtora Delta', '45678901000134', 'Alameda dos Anjos, 400', '11987654324');
INSERT INTO construtora (id, nome, cnpj, endereco, telefone) VALUES (5, 'Construtora Epsilon', '56789012000145', 'Praça do Sol, 500', '11987654325');
INSERT INTO construtora (id, nome, cnpj, endereco, telefone) VALUES (6, 'Construtora Zeta', '67890123000156', 'Avenida das Palmeiras, 600', '11987654326');
INSERT INTO construtora (id, nome, cnpj, endereco, telefone) VALUES (7, 'Construtora Eta', '78901234000167', 'Rua das Acácias, 700', '11987654327');
INSERT INTO construtora (id, nome, cnpj, endereco, telefone) VALUES (8, 'Construtora Theta', '89012345000178', 'Avenida Atlântica, 800', '11987654328');
INSERT INTO construtora (id, nome, cnpj, endereco, telefone) VALUES (9, 'Construtora Iota', '90123456000189', 'Rua das Palmeiras, 900', '11987654329');
INSERT INTO construtora (id, nome, cnpj, endereco, telefone) VALUES (10, 'Construtora Kappa', '01234567000190', 'Alameda das Rosas, 1000', '11987654330');
INSERT INTO construtora (id, nome, cnpj, endereco, telefone) VALUES (11, 'Construtora Lambda', '12345678000201', 'Avenida da Liberdade, 1100', '11987654331');
INSERT INTO construtora (id, nome, cnpj, endereco, telefone) VALUES (12, 'Construtora Mu', '23456789000212', 'Rua dos Girassóis, 1200', '11987654332');
INSERT INTO construtora (id, nome, cnpj, endereco, telefone) VALUES (13, 'Construtora Nu', '34567890000223', 'Avenida Rio Branco, 1300', '11987654333');
INSERT INTO construtora (id, nome, cnpj, endereco, telefone) VALUES (14, 'Construtora Xi', '45678901000234', 'Rua São João, 1400', '11987654334');
INSERT INTO construtora (id, nome, cnpj, endereco, telefone) VALUES (15, 'Construtora Omicron', '56789012000245', 'Praça das Américas, 1500', '11987654335');
-----TABELA PESSOA--------------------
INSERT INTO pessoa (id, nome, cpf, data_nascimento, telefone) VALUES (1, 'Ana Silva', '12345678901', '1985-05-10', '11987654321');
INSERT INTO pessoa (id, nome, cpf, data_nascimento, telefone) VALUES (2, 'Bruno Souza', '23456789012', '1990-06-15', '11987654322');
INSERT INTO pessoa (id, nome, cpf, data_nascimento, telefone) VALUES (3, 'Carla Mendes', '34567890123', '1987-07-20', '11987654323');
INSERT INTO pessoa (id, nome, cpf, data_nascimento, telefone) VALUES (4, 'Daniel Oliveira', '45678901234', '1983-08-25', '11987654324');
INSERT INTO pessoa (id, nome, cpf, data_nascimento, telefone) VALUES (5, 'Elaine Pereira', '56789012345', '1992-09-30', '11987654325');
INSERT INTO pessoa (id, nome, cpf, data_nascimento, telefone) VALUES (6, 'Fabio Lima', '67890123456', '1988-10-05', '11987654326');
INSERT INTO pessoa (id, nome, cpf, data_nascimento, telefone) VALUES (7, 'Gustavo Santos', '78901234567', '1991-11-10', '11987654327');
INSERT INTO pessoa (id, nome, cpf, data_nascimento, telefone) VALUES (8, 'Heloisa Alves', '89012345678', '1984-12-15', '11987654328');
INSERT INTO pessoa (id, nome, cpf, data_nascimento, telefone) VALUES (9, 'Igor Martins', '90123456789', '1986-01-20', '11987654329');
INSERT INTO pessoa (id, nome, cpf, data_nascimento, telefone) VALUES (10, 'Juliana Ramos', '01234567890', '1989-02-25', '11987654330');
INSERT INTO pessoa (id, nome, cpf, data_nascimento, telefone) VALUES (11, 'Kleber Araújo', '12345678912', '1982-03-30', '11987654331');
INSERT INTO pessoa (id, nome, cpf, data_nascimento, telefone) VALUES (12, 'Luciana Barbosa', '23456789023', '1993-04-05', '11987654332');
INSERT INTO pessoa (id, nome, cpf, data_nascimento, telefone) VALUES (13, 'Marcelo Nunes', '34567890134', '1985-05-10', '11987654333');
INSERT INTO pessoa (id, nome, cpf, data_nascimento, telefone) VALUES (14, 'Natália Costa', '45678901245', '1994-06-15', '11987654334');
INSERT INTO pessoa (id, nome, cpf, data_nascimento, telefone) VALUES (15, 'Otávio Correia', '56789012356', '1987-07-20', '11987654335');
-----TABELA CONDOMINIO--------------------
INSERT INTO condominio (id, nome, cidade, estado, id_construtora) VALUES (1, 'Condomínio Bela Vista', 'São Paulo', 'SP', 1);
INSERT INTO condominio (id, nome, cidade, estado, id_construtora) VALUES (2, 'Condomínio Jardim das Flores', 'Rio de Janeiro', 'RJ', 2);
INSERT INTO condominio (id, nome, cidade, estado, id_construtora) VALUES (3, 'Condomínio Residencial Sol', 'Belo Horizonte', 'MG', 3);
INSERT INTO condominio (id, nome, cidade, estado, id_construtora) VALUES (4, 'Condomínio Parque das Águas', 'Curitiba', 'PR', 4);
INSERT INTO condominio (id, nome, cidade, estado, id_construtora) VALUES (5, 'Condomínio Vista Alegre', 'Porto Alegre', 'RS', 5);
INSERT INTO condominio (id, nome, cidade, estado, id_construtora) VALUES (6, 'Condomínio Recanto Verde', 'Salvador', 'BA', 6);
INSERT INTO condominio (id, nome, cidade, estado, id_construtora) VALUES (7, 'Condomínio Morada dos Pássaros', 'Fortaleza', 'CE', 7);
INSERT INTO condominio (id, nome, cidade, estado, id_construtora) VALUES (8, 'Condomínio Vale do Sol', 'Florianópolis', 'SC', 8);
INSERT INTO condominio (id, nome, cidade, estado, id_construtora) VALUES (9, 'Condomínio Jardim América', 'Brasília', 'DF', 9);
INSERT INTO condominio (id, nome, cidade, estado, id_construtora) VALUES (10, 'Condomínio Costa do Atlântico', 'Recife', 'PE', 10);
INSERT INTO condominio (id, nome, cidade, estado, id_construtora) VALUES (11, 'Condomínio Vila Nova', 'Goiânia', 'GO', 11);
INSERT INTO condominio (id, nome, cidade, estado, id_construtora) VALUES (12, 'Condomínio Bosque das Palmeiras', 'Manaus', 'AM', 12);
INSERT INTO condominio (id, nome, cidade, estado, id_construtora) VALUES (13, 'Condomínio Águas Claras', 'Belém', 'PA', 13);
INSERT INTO condominio (id, nome, cidade, estado, id_construtora) VALUES (14, 'Condomínio Campo Belo', 'Natal', 'RN', 14);
INSERT INTO condominio (id, nome, cidade, estado, id_construtora) VALUES (15, 'Condomínio Porto Seguro', 'Vitória', 'ES', 15);
-----TABELA CASA--------------------
INSERT INTO casa (id, numero, area, id_condominio, id_pessoa) VALUES (1, 101, 120.5, 1, 1);
INSERT INTO casa (id, numero, area, id_condominio, id_pessoa) VALUES (2, 102, 130.0, 2, 2);
INSERT INTO casa (id, numero, area, id_condominio, id_pessoa) VALUES (3, 103, 140.5, 3, 2);
INSERT INTO casa (id, numero, area, id_condominio, id_pessoa) VALUES (4, 104, 150.0, 4, 2);
INSERT INTO casa (id, numero, area, id_condominio, id_pessoa) VALUES (5, 105, 160.5, 5, 2);
INSERT INTO casa (id, numero, area, id_condominio, id_pessoa) VALUES (6, 106, 170.0, 6, 2);
INSERT INTO casa (id, numero, area, id_condominio, id_pessoa) VALUES (7, 107, 180.5, 7, 7);
INSERT INTO casa (id, numero, area, id_condominio, id_pessoa) VALUES (8, 108, 190.0, 8, 8);
INSERT INTO casa (id, numero, area, id_condominio, id_pessoa) VALUES (9, 109, 200.5, 9, 9);
INSERT INTO casa (id, numero, area, id_condominio, id_pessoa) VALUES (10, 110, 210.0, 10, 10);
INSERT INTO casa (id, numero, area, id_condominio, id_pessoa) VALUES (11, 111, 220.5, 11, 11);
INSERT INTO casa (id, numero, area, id_condominio, id_pessoa) VALUES (12, 112, 230.0, 12, 12);
INSERT INTO casa (id, numero, area, id_condominio, id_pessoa) VALUES (13, 113, 240.5, 13, 13);
INSERT INTO casa (id, numero, area, id_condominio, id_pessoa) VALUES (14, 114, 250.0, 14, 14);
INSERT INTO casa (id, numero, area, id_condominio, id_pessoa) VALUES (15, 115, 260.5, 15, 15);



---01

SELECT nome,
	(SELECT co.nome FROM condominio co, casa ca WHERE p.id = ca.id_pessoa AND ca.id_condominio = co.id) AS nome_cond
FROM
	pessoa p
WHERE 
	p.nome = 'Ana Silva'

--02
SELECT p.nome,
    (SELECT c.numero
        FROM casa c, condominio co
        WHERE p.id = c.id_pessoa
        AND c.id_condominio = co.id
        AND co.nome = 'Condomínio Bela Vista')
FROM 
    pessoa p, casa c, condominio co
WHERE 
    p.id = c.id_pessoa
    AND c.id_condominio = co.id
    AND co.nome = 'Condomínio Bela Vista'
    AND c.numero > (SELECT AVG(numero) FROM casa)


-03

SELECT
	nome,
	(SELECT cons.nome FROM construtora cons, casa c, condominio con, pessoa p WHERE p.id = c.id_pessoa AND c.id_condominio = con.id AND con.id_construtora = cons.id)
FROM
	pessoa
WHERE
	nome = 'Bruno Souza'
