import pandas as pd
from tabulate import tabulate as tb

# mydataset = {
#   'cars': ["BMW", "Volvo", "Ford"],
#   'passings': [3, 7, 2]
# }

# myva = pd.DataFrame(mydataset)
# print(myva.loc[[0,1]])
# making dataframe from mydataset in {} brackets with keywords and the values it is supposed to show and shwoing it
#pd.DataFrame for converting mydataset to a dataframe so it can be shown and epxorted to csv or xl
#pd.DataFrame.loc or simply myva.loc[0] returns the row with all columns of for a specific column use myva.loc[0][0] this will return 0th row 0th element example is above try and test
# loc function allows you to apply conditions and loops as well and representing values along the side as well. 

#myva.loc[[0,1]] returns all the row 0 and 1 with all columns

# in pandas you can also get your own indexes but its not worth it, If your making a program you can just allow the user to take his input and find his entry from if conditions using myva.loc[0][1] to find the exact row and columns with name

# you can also read csv direlctly using pd.read_csv() fucntion 

# df = pd.read_csv('E:\\Creative Works\\Visual Works\\Learning Works\\Python FIles\\data.csv')
# dffer=[["Keywords","Currency","Avg.Monthly Views","Competition(Category)","Competition(Values)","Top of page bid (low range)","Top of page bid (high range)"]]
# for x in range(len(df)):
#     if df.loc[x][5]=="Low" and int(df.loc[x][2])>5:
#         dffer.append([df.loc[x][0],df.loc[x][1],df.loc[x][2],df.loc[x][5],df.loc[x][6],df.loc[x][7],df.loc[x][8]])
        

# fancy=tb(dffer,tablefmt="fancy_grid")
# print(fancy)

#in above code we took and read a csv then created a list dffer with header so it can be useful with tabulate, then we found the no of rows of csv dataframe df
#after that we looped the range of df as x and we put conditions on specific columns of all the rows, like 5 columns(0-5 numbering its 6th column actually)
#and we applied condition on 5 column to be Low and 2 column to be bigger than 5 and append all the things to dffer so tabulate can make a data structure for it
# after that we defined fancy and put dffer list in it as well as tablefmt fancy_grid to be displayed beautifully
#and then we just simply print the damn thing also for console printing making list and using tabulate is best option
# But for epxorting everything to csv we have to make a dataframe seperately


#pandas series is one dimensional and of same type basically inferior to python lists


# df = pd.read_csv('E:\\Creative Works\\Visual Works\\Learning Works\\Python FIles\\data.csv')
# ld = df.loc[(df['Competition']=='Low') & (df['Avg. monthly searches']==500), ["Keyword","Competition","Avg. monthly searches"]]
# ld=df.loc[(df["Competition"]=="High") & (df["Avg. monthly searches"]<=4000),["Keyword","Competition","Avg. monthly searches"]]
# print(ld)
# for conditions (df["Competition"]=="High") must be in parenthesis and is & inside pandas and rest is told eariler
# here we are with df.loc finding rows with conditions like competetion and avg. monthly searches and then we are simply telling what columns we want in new csv like competeivin and avg.monthlyu searches
# ld.to_csv('E:\\Creative Works\\Visual Works\\Learning Works\\Python FIles\\final.csv') 
# table=df.loc[df["Competition"]=="Low",["Competition","Keyword"]]

