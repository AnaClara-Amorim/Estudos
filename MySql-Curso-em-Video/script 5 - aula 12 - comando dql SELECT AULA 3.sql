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

