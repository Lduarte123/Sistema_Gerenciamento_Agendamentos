CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    usuario VARCHAR(50) UNIQUE NOT NULL,
    senha VARCHAR(50) NOT NULL
-- ); so nao executa esse       MV

CREATE TABLE agendamentos (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    data DATE NOT NULL,
    horario TIME NOT NULL,
    local VARCHAR(100) NOT NULL,
    descricao TEXT
);


CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    senha VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    data_nasc DATE NOT NULL,
    cidade VARCHAR(255) NOT NULL,
    sexo VARCHAR(10) CHECK (sexo IN ('Masculino', 'Feminino')) NOT NULL
);

select * from usuarios
drop table agendamentos
select * from agendamentos