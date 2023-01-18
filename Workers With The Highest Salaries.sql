/* 
Title: Workers With The Highest Salaries
Description: Find the titles of workers that earn 
the highest salary. Output the highest-paid title 
or multiple titles that share the highest salary.
*/
--select * from worker;
select a.worker_title 
from worker b 
join title a on b.worker_id = a.worker_ref_id
where salary in (select max(salary) from worker);
