import pandas as pd
keys=[]
comp=[]
mon_views=[]
avg_cost=[]

pd.options.display.max_rows = 50000
df = pd.read_csv("data.csv")
# df.loc[x][5]=="Compteteion String"
# df.loc[x][2]=="Avg. Monthly views"

def data():
    global database
    database={
        "Keywords":keys,
        "Competetion":comp,
        "Monthly Views":mon_views,
        "Average Cost":avg_cost

    }    

for x in range(len(df)):
    if df.loc[x][5] == "Low":
        if df.loc[x][2] >= 500:
            avg = round((df.loc[x][7]+df.loc[x][8])/2, 2)
            keys.append(df.loc[x][0])
            comp.append(df.loc[x][5])
            mon_views.append(df.loc[x][2])
            avg_cost.append(avg)

data()

file=pd.DataFrame(database)
file.to_csv('final.csv',index=False)
