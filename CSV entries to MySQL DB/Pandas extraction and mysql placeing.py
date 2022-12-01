import pandas as pd
from sqlalchemy import create_engine
engine = create_engine("mysql+mysqldb://root:"+'1234567890'+"@localhost/nick")
df=pd.read_csv("File.csv")
df.to_sql(con=engine, name='information',if_exists='replace', index=False)
