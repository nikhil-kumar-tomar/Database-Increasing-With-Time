import pandas as pd
df = pd.read_csv('data.csv')
ld=df.loc[(df["Competition"]=="High") & (df["Avg. monthly searches"]>=4000),["Keyword","Competition","Avg. monthly searches"]]
ld.to_csv("final.csv")