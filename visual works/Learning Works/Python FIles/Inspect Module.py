import sqlalchemy
import pandas as pd
import inspect
with open("E:\\Creative Works\\Visual Works\\Learning Works\\Python FIles\\Examine Modules.txt","w") as f:
    src=inspect.getsource(pd.DataFrame.to_sql)
    f.writelines(src)
