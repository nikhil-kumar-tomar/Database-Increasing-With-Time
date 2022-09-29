import numpy as np
import pandas as pd
# Converting dictionary it to data frame
dict = {'English': [85, 73, 98], 'Math': [60, 80, 58],
        'Science': [90, 60, 74], 'French': [95, 87, 92]}
df = pd.DataFrame(dict, index=[2018, 2019, 2020])

# French 92 to 29
# print('Modify a single value:')
# print('\n')
# df["French"][2020]=29
# print(df)
# print('\n')

# Means of english and science
# print("Mean of English is \n")
# print((df["English"][2018]+df['English'][2019]+df['English'][2020])/3)
# print("Mean of Science is \n")
# print((df['Science'][2018]+df['Science'][2019]+df['Science'][2020])/3)

# Adding economics section
# economics_value=[99,99,99]
# df["Economics"]=economics_value
# print(df)

# changing values of economics
# df["Economics"][2019]=54
# df["Economics"][2020]=45
# print(df)

# Q2 C
# Deleting economics columns
# del df["Economics"]
#changing data types
# convert_dict = {'English': float,
#                 'Math': float,
#                 'Science': float,
#                 'French':float
#                 }

# df = df.astype(convert_dict)
# df.loc[2022] = [89, 21, 87,59]
# print(df)
# Q2 C-----------------------

# Delete 2018 row
# update=df.drop(2018)
# print(update)

# count of actors with movies above then 460
# some missing values
NaN = np.nan
df = pd.DataFrame({'Name': ['Amitabh', 'Rekha',
                            'SHARUKH', 'SALMAN',
                            'PRIYANKA', 'HEMA'],
                   'MOVIES': [500, 470, 450, 467, NaN, 340],
                   'SERIAL': [45, 3, NaN, 2, 1, 1],
                   'ADDS': [13, 10, 15, NaN, NaN, 13]})

l=df.loc[(df["MOVIES"]>460),['Name']]
print(len(l))
