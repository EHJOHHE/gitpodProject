create database exercicio;
use exercicio;

create table pessoa(
	id int
);

create table telefone(
	id int,
    numero bigint
);

--1º) Adicionar as colunas na tabela pessoa:

ALTER TABLE pessoa ADD nome varchar(255) not null;
ALTER TABLE pessoa ADD sobrenome varchar(255) default 'Farias';

--2º) Remova a coluna id da tabela pessoa
ALTER TABLE pessoa DROP COLUMN id;

--3º) Adicione novamente a coluna id so que dessa vez do tipo int, auto incriment e primary key
ALTER TABLE pessoa ADD id int auto_increment primary key first;

--4º) Adicionar as colunas na tabela telefone
ALTER TABLE telefone DROP COLUMN Numero;
ALTER TABLE telefone ADD Numero bigint not null;

ALTER TABLE telefone ADD fk_id_pessoa int;