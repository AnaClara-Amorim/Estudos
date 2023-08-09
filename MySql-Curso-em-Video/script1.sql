create database cadastro
default character set utf8mb4
default collate utf8mb4_general_ci; /*constrains para caracteres especiais*/

/*
DDL - Data definintion language - CREATE DATABASE, CREATE TABLE
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



