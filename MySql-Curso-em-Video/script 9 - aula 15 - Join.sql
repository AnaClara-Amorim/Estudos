/*Comando Join*/

select nome, cursopreferido from gafanhotos; /*Aparece só o número*/
 
 select nome, ano from cursos; 
 
 select gafanhotos.nome, cursos.nome, cursos.ano
 from gafanhotos inner join cursos
 on cursos.idcurso = gafanhotos.cursopreferido
 order by gafanhotos.nome; 
 
 /*Outra forma de escrever
 
 select g.nome, c.nome, c.ano
 from gafanhotos as g inner join cursos as c
 on c.idcurso = g.cursopreferido
 order by g.nome; */