/*SELECT parte 3, agrupamento & agregamento */

select carga, count(nome) from cursos
group by carga;

select * from cursos;

select totaulas, count(*) from cursos
group by totaulas
order by totaulas;

select carga, totaulas from cursos
where totaulas = 30
group by carga;

select ano, count(*) from cursos /*Seleciona todos os anos e conta eles*/
where totaula > 30
group by ano 
having count(ano) >= 5 /*Só agrupa quem tem o count ano maior que 5*/
order by count(*) desc; /*Ordena por número de contagem do maior por menor*/


select avg (carga) from cursos;

select carga, count(*) from cursos
where ano > 2015
group by carga
having carga > (select avg (carga) from cursos); /*Mostrando quem está acima da carga média*/

/* Exercícíos */

/*Uma lista com as profissões dos gafanhotos e seus quantitativos*/

select profissao, count(*) from gafanhotos
group by profissao;

/*Quantos gafanhotos homens e mulheres nasceram após 01-jan-2005? */

select sexo, count(*) from gafanhotos
 where nascimento > '2005-01-01' 
 group by sexo;

/*Uma lista com os gafanhotos que nasceram fora do Brasil, mostrando
o  país de origiem e o total de pessoas lá. Só nos interessam os países
que tiveram mais de 3 gafanhotos com essa nacionalidade*/

select nacionalidade, count(*) from gafanhotos 
where nacionalidade != 'Brasil' 
group by nacionalidade 
having count(*) > 3 order by count(*) desc;

/*Uma lista agrupada pela altura dos gafanhotos, mostrando quantas 
pessoas pesam mais de 100kg e que estão acima da média de altura de todos*/

select altura, count(*) from gafanhotos 
where peso > 100 and altura > (select avg(altura) from gafanhotos) 
group by altura order by altura;

