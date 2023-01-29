#%%
# Linear Regression Code

import os
filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Salary_Data.csv')
import pandas as pd
import seaborn as sns
import numpy as np
from sklearn import linear_model 
data = pd.read_csv(filename)
X = data['YearsExperience']
Y = data['Salary']
X=np.array(X).reshape(len(X),1)
Y=np.array(Y).reshape(len(Y),1)
model = linear_model.LinearRegression()
model.fit(X,Y)
Y_pred = model.predict(X)
Y_pred=np.array(Y_pred).reshape(1,len(Y_pred))
prediction=pd.DataFrame({"YearsExperience":X.ravel(),"Salary":Y_pred.ravel()})
# sns.relplot(x='YearsExperience',y='Salary',data=data)
# sns.lineplot(x="YearsExperience",y="Salary",data=prediction)
sns.relplot(x='YearsExperience',y='Salary',data=data,kind='line')
# sns.lineplot(x="YearsExperience",y="Salary",data=prediction)