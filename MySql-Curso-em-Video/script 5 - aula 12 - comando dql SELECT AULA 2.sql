/*COMANDO SELECT - SELECIONANDO COLUNAS*/
/*Data Qwert Language - SELECT*/

/*Seleção por nome*/

select * from cursos
where nome = 'php';

/*Operador like*/

select * from cursos
where nome like 'p%'; /*Onde nome é PARECIDO com p seguido de qualquer coisa. Com o operador like % caractere coringa*/

/*Wildcards*/

select * from cursos
where nome like '%a'; /*Nomes que terminam com a letra a*/

select * from cursos
where nome like '%a%'; /*Qualquer curso com a letra a em qualquer posição*/

select * from cursos
where nome not like '%a%'; /*Descarta qualquer curso com a letra a em qualquer posição*/

update cursos set nome = 'PáOO' where idcurso = '9'; /*Mudando nome do curso de POO
É possível editar diretamente no result grid, onde após clicar em aply, o comando será
mostrado */

select * from cursos
where nome like 'ph%p_';/*O sublinhado exige que tenha algum caractere ali*/

select * from gafanhotos
where nome like '%_silva%';

/*Como distinguir coisas*/

select * from gafanhotos;

select distinct nacionalidade from gafanhotos /*As várias ocorrências viram apenas uma*/
order by nacionalidade;

select distinct carga from cursos
order by carga;

/*Funções de agregação*/

select count(*) from cursos; /*O count dá a quantidade de cursos cadastrados*/

select count(*) from cursos 
where carga > 40; 

select max(carga) from cursos; /*Mostra o valor máximo registrado*/

select max(totaulas) from cursos
where ano = '2016';

select min(totaulas) from cursos; /*Mostra o valor mínimo registrado*/

select sum(totaulas) from cursos
where ano = '2016'; /*Soma*/

select avg(totaulas) from cursos; /*Dá a média*/






