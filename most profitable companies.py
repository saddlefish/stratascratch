"""
Title: Most profitable companies
Description: Find the 3 most profitable companies in the entire world.
             Output the result along with the corresponding company name.
             Sort the result based on profits in descending order.
"""

import pandas as pd
#start writing code
forbes_global_2010_2014 = forbes_global_2010_2014.sort_values(['profits'], ascending = False)
answer = forbes_global_2010_2014[:3]
answer
