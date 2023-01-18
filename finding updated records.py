"""
Title: Finding Updated Records
Description: We have a table with employees and their salaries, 
             however, some of the records are old and contain outdated 
             salary information. Find the current salary of each employee 
             assuming that salaries increase each year. Output their id, 
             first name, last name, department ID, and current salary. 
             Order your list by employee ID in ascending order
"""

# Import your libraries
import pandas as pd

# Start writing code
ms_employee_salary.head()
#df = ms_employee_salary.sort_values(by = ['id','salary'], ascending = False)#.sort_values(by='salary')
#df.loc[df['salary']].max()
#( 
#    ms_employee_salary
#    .groupby(level=0)
#    .apply(lambda group : group.loc[group['salary'] == group['salary'].max()]) #(1, columns = 'salary'))
#    .reset_index(level = -1, drop = True)
#)
#(
#    ms_employee_salary.query('salary < salary')
#    .sort_values('salary', ascending = False)
#    .drop_duplicates(['first_name', 'last_name'])#.groupby('id', sort = False)
#)

ms_employee_salary.sort_values('salary', ascending = False).drop_duplicates('id')
