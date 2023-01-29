# %%
# from sklearn.cluster import KMeans
# from matplotlib import pyplot as plt
# import seaborn as sns
# from inspect import getsource as gst
# import pandas as pd
# Input for 10 numbers and show even and odd

# lame=[]
# even=[]
# odd=[]

# for num in range(10):
#     inp=int(input("Enter your number: "))
#     lame.append(inp)
# for x in lame:
#     if x%2==0:
#         even.append(x)
#     else:
#         odd.append(x)
# print("Even number list is",even)
# print("Odd number list is",odd)


# rows=int(input("Enter your Rows: "))
# columns=int(input("Enter your columns: "))
# for tim in range(rows):
#     for l in range(columns):
#         print("*",end="")
#     print("\n")
    

# def data():
#     pd.options.display.max_rows = 50000
#     df = pd.read_csv("E:\Creative Works\Visual Works\Learning Works\Python FIles\Server_Information.csv")
#     mac_list.extend(df['Mac_Address'].tolist())
#     ip_list.extend(df["IP_Address"].tolist())
#     user_list.extend(df["SSH_Users"].tolist())
# data()
# print(mac_list)
# print(ip_list)
# print(user_list)

# df=pd.read_csv("Colo.csv")
# df=df.dropna()
# cluster=KMeans(n_clusters=15,init="k-means++")
# cluster=cluster.fit(df)

# print(gst(KMeans))
# sns.scatterplot(x=df['x'], y=df['y'], hue=cluster.labels_).set_title('After figuring 15 as clusters')
# plt.scatter(cluster.cluster_centers_[:,0],cluster.cluster_centers_[:,1],color="aqua",marker="x",label='Centroids')

# x=1
# try:
#     1/0
# except Exception as e:
#     print("division by zero" in str(e))

# class employee:
#     def __init__(self,salary,work):
#         self.salary=salary
#         self.work=work
#     def addsalary(self):
#         if self.salary<500:
#             self.salary+=50
#     def addworks(self):
#         if self.work>6:
#             self.salary+=5
#     def finalsalary(self):
#         return self.salary     


# Johanson=employee(50,7)
# Johanson.addsalary()
# Johanson.addworks()
# print(Johanson.finalsalary())

#Protected stuff
# class employee:
#     def __init__(self,salary,work):
#         self.salary=salary
#         self.work=work
#     def addsalary(self):
#         self.salary+=1
#         self.work+=1
#         return [self.salary,self.work]


# Johanson=employee(1,2)
# print(Johanson.addsalary())

#This is a test for copying fiels overs
# a="Hello"
# print(a[::-1])
# Reading fro python file
# from sklearn.linear_model import LinearRegression
# import pandas as pd
# import numpy as np
# import seaborn as sns
# from matplotlib import pyplot as plt
# df=pd.read_csv("Salary_Data.csv")
# x=df["YearsExperience"]
# y=df["Salary"]
# model=LinearRegression()
# model.fit(np.array(x).reshape(len(x),1),np.array(y).reshape(len(y),1))
# y_pred=model.predict(np.array(x).reshape(len(x),1))
# sns.scatterplot(x=x,y=y)
# sns.scatterplot(x=x,y=y_pred.ravel())
# plt.show()
# %%