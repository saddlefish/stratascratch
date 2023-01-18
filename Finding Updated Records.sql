/*
title: Finding Updated Records
description: We have a table with employees and their 
salaries, however, some of the records are old and 
contain outdated salary information. Find the current 
salary of each employee assuming that salaries increase 
each year. Output their id, first name, last name, department 
ID, and current salary. Order your list by employee ID in ascending order.
*/

#select * from ms_employee_salary;
#Delete 
#from ms_employee_salary
#where 'id' not in (select max('id') 
#                   from ms_employee_salary
#                   group by 'first_name', 'last_name', 'salary', 'department_id')
select id, first_name, last_name, department_id, salary
from ms_employee_salary a
where salary = (select max(b.salary)
                from ms_employee_salary b
                where a.id = b.id)
#group by id
order by id ASC
#where salary in (select max(salary) from ms_employee_salary)
