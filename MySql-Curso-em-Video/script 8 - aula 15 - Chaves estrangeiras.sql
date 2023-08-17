use cadastro;

describe gafanhotos;

alter table gafanhotos
add column cursopreferido int;

alter table gafanhotos
add foreign key (cursopreferido)
references cursos(idcurso); /*Agora a foreing key aparece como mul*/

select * from gafanhotos;
select * from cursos;

update gafanhotos 
set cursopreferido = '6'
where id = '1';

delete from cursos
where idcurso = '6'; /*Dá erro de integridade referecial*/

delete from cursos
where idcurso = '28'; /*Aqui, como o curso não estava referenciado
a ninguém, foi possível apagar, integridade referencial é o nome*/

