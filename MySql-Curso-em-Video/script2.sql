create database cadastro
default character set utf8mb4
default collate utf8mb4_general_ci; /*constrains para caracteres especiais*/

/*
DDL - Data definintion language - CREATE DATABASE, CREATE TABLE, ALTER TABLE, DROP TABLE
DML - Data manipulation language - INSERT INTO
*/

create table pessoas (
id int not null auto_increment primary key,  /*Define e gera automaticamente*/
nome varchar(30) not null, /*Torna obrigatório preencher*/
nascimento date, 
sexo enum ('M', 'F'), 
peso decimal (5,2), /*Podem ser cinco casas com dois dígitos após a vírgula*/
altura decimal (3,2),
nacionalidade varchar (20) default 'Brasil' /*Se nada for digitado, o padrão é Brasil */
) default charset = utf8;

insert into pessoas (nome, nascimento, sexo, peso, altura, nacionalidade) /*Não é preciso colocar o auto incromento, mas pode colocar como default*/
values ('Ana', '1999-01-02', 'F', '40.0', '1.57', 'Brasil');

/*Outra forma de inserir, colocando os dados na ordem de sua declaração*/
insert into pessoas values
(DEFAULT, 'Creuza', '2000-01-01', 'F', '60.0', '1.60', 'Brasil');

/*Outra forma de inserir colocando vários dados com um único insert into*/
insert into pessoas 
(id, nome, nascimento, sexo, peso, altura, nacionalidade) 
values
(DEFAULT, 'Pessoa', '2020-01-01', 'M', '20.0', '0.90', 'Brasil'),
(DEFAULT, 'OutraPessoa', '2000-01-01', 'M', '90.0', '1.60', 'Brasil');

select * from pessoas;

/*Alterando a estrutura da tabela*/

describe pessoas; /*ou desc*/

alter table pessoas
add column profissao varchar(10);

select * from pessoas;

/*Removendo colunas*/
alter table pessoas
drop column profissao;

/*Adicionando novamente em outra posição*/

alter table pessoas
add column profissao varchar(10) after nome;

/*Adicionando posição da coluna como primeira*/

alter table pessoas
add column codigo int first; /*aqui, a palavra column é opcional*/

/*Modificando definições, modifica tipos e constrains*/

alter table pessoas
modify column profissao varchar(20);

/*Renomeando coluna*/

alter table pessoas
change column profissao prof varchar(20);

/*Renomeando toda tabela*/

alter table pessoas
rename to gafanhotos;

/*Criando nova tabela*/

create table if not exists gafanhotos (teste int); /*não cria, pois já existe*/

create table if not exists cursos ( /*só cria se ele não existir*/
	nome varchar(30) not null unique, /*unique aqui dizendo que não pode repetir o nome, mas não é pk*/
    descricao text,
    carga int unsigned, /*sem sinal, podendo ser apenas positivo*/
    totaulas int unsigned,
	ano year default '2023'
) default charset = utf8;

describe cursos;

/*Colocando chave primária*/
/*Primeiro, adicionando a coluna*/
alter table cursos
add column idcurso int first;

/*Colocando ele como PK*/

alter table cursos
add primary key (idcurso);

/*Apagando tabelas*/

create table if not exists teste (
id int,
nome varchar(10),
idade int);

insert into teste value
('1', 'Ana', '26'),
('2', 'Sky', '3');

drop table if exists alunos;
drop table if exists teste;







