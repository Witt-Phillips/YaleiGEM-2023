""" 
1. Get four identifiers, and calculate each access statistic across each possible case
    ie. calulate menpause injections for each race listed (how should this data be stored? Matrix?)
2.  Create a search algorithm: given a certain identifier, what access statistic is the most different?
    What is the average difference in all access statistics? ** this could actually be the more
    important statstic**
3. Link papers to each identifier to explain why differneces might exist.
"""
import pandas as pd

df = pd.read_csv(r'/Users/wittphillips/all/igem/iGEM-Shared/SWAN_prelim72.csv')
print(df.head)

#Create matrix

