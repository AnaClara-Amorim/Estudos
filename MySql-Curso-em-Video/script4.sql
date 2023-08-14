use cadastro;

/*Alterando o nome de uma linha específica*/

update cursos 
set nome = 'HTML5' 
where idcurso = '1';

update cursos
set nome = 'PHP', ano = '2015'
where idcurso = '4';

update cursos
set nome = "Java", carga = '40', ano = '2015'
where idcurso = '5';

update cursos
set ano = '2050', carga = '800'
where ano = '2018';

select * from cursos;
/*Para ativar ou desativar o safe update, preferences, sql editor*/

delete from cursos 
where idcurso = '8';

delete from cursos
where ano = '2050'
limit 2;

truncate cursos; /*deleta toda tabela*/

/*DDL create database, create table, alter table, drop table*/

/*DML insert into, update, delete, truncate*/