/*COMANDO SELECT - SELECIONANDO COLUNAS*/
/*Data Qwert Language - SELECT*/

select * from cursos
ORDER BY nome; /*Vai ordenar em ordem alfabética*/

select * from cursos
ORDER BY nome desc; /*Vai ordenar em ordem alfabética ao contrário*/

select nome, carga, ano from cursos
order by nome; /*Aqui, não usamos o asterístico, pois ele seleciona todos*/

select nome, nome, ano from cursos
order by ano;

/*COMANDO SELECT - SELECIONANDO LINHAS*/

select * from cursos 
where ano = 2016
order by nome;

select nome, descricao, ano carga from cursos
where ano != 2015 /*Adiciona todos os anos diferentes de 2015*/
order by ano, nome; /*Ordem alfabetica e por ordem de ano*/

select nome, ano from cursos 
where ano between 2014 and 2016 /*Mostra 2014, 2015 e 2016*/
order by ano desc;

select nome, ano from cursos
where ano in (2014, 2016) /*Mostra 2014 e 2016*/
order by ano;

select nome, carga, totaulas from cursos
where carga > 35 and totaulas <30;




