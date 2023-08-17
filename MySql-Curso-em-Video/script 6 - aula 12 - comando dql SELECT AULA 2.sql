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

/*Selecionar todas as alunAs*/
select * from gafanhotos
where sexo = 'f';

/*Selecionar uma lista com os ddos de todos que nasceram entre 1/jan/2000 e 31/dez/2015*/

select * from gafanhotos 
where nascimento between '2000-01-01' and '2015-12-31';

/*Uma lista de todo os homems que trabalham com programação*/

select * from gafanhotos
where profissao = 'programador' and sexo = 'm';

/*Uma lista com todos os dados de todas as mulheres que nasceram no Brasil e que tem seu nome iniciando com a letra J*/

select * from gafanhotos
where nacionalidade = 'Brasil' and nome like 'J%';

/*Uma lista com o nome e a nascionalidade de todos homens que tem
Silva no nome, não nasceram no brasil e pesam menos de 100kg*/

select nome, nacionalidade, peso from gafanhotos 
where sexo = 'M' and nacionalidade != 'Brasil' 
and peso < '100' and nome like '%Silva%';

/*Qual a maior altura dos homens no Brasil?*/

select max(altura) from gafanhotos
where sexo = 'm' and nacionalidade = 'brasil';

/*Qual a média de peso de todos?*/

select avg(peso) from gafanhotos;

/*Qual é o menor peso entre os gafanhotos Mulheres que nasceram
 fora do Brasil e entre 01/Jan/1990 e 31/Dez/2000?*/
 select min(peso), nome from gafanhotos
 where sexo = 'F' and nacionalidade != 'Brasil' and 
 nascimento between '1990-01-01' and '2000-12-31';
 
/*Quantas gafanhotos Mulheres tem mais de 1.90cm de altura?*/
 select count(altura) from gafanhotos
 where sexo = 'F' and altura > '1.90';






