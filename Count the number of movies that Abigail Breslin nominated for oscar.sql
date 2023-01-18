/*
Title: Count the number of movies that Abigail Breslin nominated for oscar
Description: Count the number of movies that Abigail Breslin was nominated for an oscar.
*/
select COUNT(*)
from oscar_nominees 
where nominee = 'Abigail Breslin';
