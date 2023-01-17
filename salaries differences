"""
Title: Salaries differences
Description: Write a query that calculates the difference between the highest salaries 
             found in the marketing and engineering departments. Output just the absolute 
             difference in salaries.
"""

# Import your libraries
import pandas as pd

# Start writing code
db_employee.head()

new = pd.merge(db_employee, db_dept, left_on = 'department_id', right_on = 'id')
dept = ['engineering', 'marketing']
new = new[new['department'].isin(dept)]
#max2 = new.loc[new.groupby(['department'])['salary'].idxmax()]
mkt_high = new.loc[new['department'] == 'marketing','salary'].max()
eng_high = new.loc[new['department'] == 'engineering','salary'].max()
#max2['salary'].diff(axis=1)
abs(mkt_high - eng_high)
