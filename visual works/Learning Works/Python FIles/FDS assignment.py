#%%
# imported libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
# # Converting dictionary it to data frame
# dict = {'English': [85, 73, 98], 'Math': [60, 80, 58],
#         'Science': [90, 60, 74], 'French': [95, 87, 92]}
# df = pd.DataFrame(dict, index=[2018, 2019, 2020])
# # French 92 to 29
# print('Modify a single value:')
# print('\n')
# df["French"][2020]=29
# print('\n')
# # Means of english and science
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
# NaN = np.nan
# df = pd.DataFrame({'Name': ['Amitabh', 'Rekha',
#                             'SHARUKH', 'SALMAN',
#                             'PRIYANKA', 'HEMA'],
#                    'MOVIES': [500, 470, 450, 467, NaN, 340],
#                    'SERIAL': [45, 3, NaN, 2, 1, 1],
#                    'ADDS': [13, 10, 15, NaN, NaN, 13]})

# l=df.loc[(df["MOVIES"]>460),['Name']]
# print(len(l))

#assignment 2 starts here

# Selecting rows of Woman 
# df=pd.read_excel("Height.xlsx")
# wd=df.loc[df["Gender"]=='W']
# print(wd)

# mean of weight and height
# df=pd.read_excel("Height.xlsx")
# wd=df.loc[df["Gender"]=="W"]
# mean_ht=sum(wd["Height(cm)"])/len(wd)
# mean_wt=sum(wd["Weight(kg)"])/len(wd)
# print(f"Mean height of woman is {mean_ht}")
# print(f"Mean Weight of woman is {mean_wt}")

#Max and min weight 
# df=pd.read_excel("Height.xlsx")
# wd=df.loc[df["Gender"]=="W"]
# max_wt=max(wd["Weight(kg)"])
# min_wt=min(wd["Weight(kg)"])
# print(f"Max Weight of woman is {max_wt}")
# print(f"Min Weight of woman is {min_wt}")

# Algeria women height mean
# df=pd.read_excel("Height.xlsx")
# wd=df.loc[(df["Gender"]=="W") & (df["Country/Team"]=="Algeria")]
# mean_Alg=sum(wd["Height(cm)"])/len(wd)
# print(f"Mean Height of woman of Algeria is {mean_Alg}")

# create dataframe circle1

# tb={
#     "radius (cm)":[1.0,1.5,2.5,4.0,6.0],
#     "color":["red","blue","orange","green","red"],
#     "area(in cm2)":[3.140,7.065,19.625,50.240,113.040] 
# }

# ld=pd.DataFrame(tb)
# index=pd.Index(["Circle 1","Circle 2","Circle 3","Circle 4","Circle 5"])
# ld = ld.set_index(index)

# print(ld)

# Calculate the average radius of a circle in this data frame.

# tb={
#     "radius (cm)":[1.0,1.5,2.5,4.0,6.0],
#     "color":["red","blue","orange","green","red"],
#     "area(in cm2)":[3.140,7.065,19.625,50.240,113.040] 
# }

# ld=pd.DataFrame(tb)
# index=pd.Index(["Circle 1","Circle 2","Circle 3","Circle 4","Circle 5"])
# ld = ld.set_index(index)
# mean_rad=sum(ld["radius (cm)"])/len(ld)
# print(f"Mean Radius is {mean_rad}")


# Frequently occuring color
# from statistics import mode
# tb={
#     "radius (cm)":[1.0,1.5,2.5,4.0,6.0],
#     "color":["red","blue","orange","green","red"],
#     "area(in cm2)":[3.140,7.065,19.625,50.240,113.040] 
# }

# ld=pd.DataFrame(tb)
# index=pd.Index(["Circle 1","Circle 2","Circle 3","Circle 4","Circle 5"])
# ld = ld.set_index(index)
# color=ld["color"]
# res=mode(color)
# print(f"Color occuring the most is {res}")


# deleting area cm2 
# tb={
#     "radius (cm)":[1.0,1.5,2.5,4.0,6.0],
#     "color":["red","blue","orange","green","red"],
#     "area(in cm2)":[3.140,7.065,19.625,50.240,113.040] 
# }

# ld=pd.DataFrame(tb)
# index=pd.Index(["Circle 1","Circle 2","Circle 3","Circle 4","Circle 5"])
# ld = ld.set_index(index)
# ld.drop("area(in cm2)",axis=1,inplace=True)
# print(ld)

# deleting row with highest area
# tb={
#     "radius (cm)":[1.0,1.5,2.5,4.0,6.0],
#     "color":["red","blue","orange","green","red"],
#     "area(in cm2)":[3.140,7.065,19.625,50.240,113.040] 
# }

# ld=pd.DataFrame(tb)
# index=pd.Index(["Circle 1","Circle 2","Circle 3","Circle 4","Circle 5"])
# ld = ld.set_index(index)
# color=ld["color"]
# ld.drop(ld[(ld["area(in cm2)"] ==max(ld["area(in cm2)"]))].index, inplace=True)
# print(ld)

# creating 2 dataframe 
# tb1={
#     "mark1":[10,40,15,40],
#     "mark2":[15,45,30,70],
# }

# tb2={
#     "mark1":[30,20,20,50],
#     "mark2":[20,25,30,30],
# }

# df1=pd.DataFrame(tb1)
# df2=pd.DataFrame(tb2)
# print(df1)
# print(df2)

# adding 2 dataframes

# tb1={
#     "mark1":[10,40,15,40],
#     "mark2":[15,45,30,70],
# }

# tb2={
#     "mark1":[30,20,20,50],
#     "mark2":[20,25,30,30],
# }

# df1=pd.DataFrame(tb1)
# df2=pd.DataFrame(tb2)
# df3=pd.concat([df1,df2],ignore_index=True)
# print(df3)

# SUbtratcion dataframes df1-df2
# tb1={
#     "mark1":[10,40,15,40],
#     "mark2":[15,45,30,70],
# }

# tb2={
#     "mark1":[30,20,20,50],
#     "mark2":[20,25,30,30],
# }

# df1=pd.DataFrame(tb1)
# df2=pd.DataFrame(tb2)
# df3=df1-df2
# print(df3)

#Renaming columns
# tb1={
#     "mark1":[10,40,15,40],
#     "mark2":[15,45,30,70],
# }

# tb2={
#     "mark1":[30,20,20,50],
#     "mark2":[20,25,30,30],
# }

# df1=pd.DataFrame(tb1)
# df2=pd.DataFrame(tb2)
# df1.rename(columns={"mark1":"marks1"},inplace=True)
# df2.rename(columns={"mark1":"marks1"},inplace=True)
# print(df1)
# print(df2)

# changing index
# tb1={
#     "mark1":[10,40,15,40],
#     "mark2":[15,45,30,70],
# }

# df1=pd.DataFrame(tb1)

# df1.rename(columns={"mark1":"marks1"},inplace=True)
# index=pd.Index(["zero","one","two","three"])
# df1.set_index(index,inplace=True)
# print(df1)

# Assignment 3 Starts here
# most medal won by sydney
# df=pd.read_excel("Summer-Olympic-medals-1976-to-2008student.xlsx")
# sydn_list=df.loc[(df["City"]=="Sydney")]
# medals=sydn_list["Medal"].mode()
# print(f"Most medals won by Sydney are {medals[0]}")


# gold won by sydney
# df=pd.read_excel("Summer-Olympic-medals-1976-to-2008student.xlsx")
# sydn_list=df.loc[(df["City"]=="Sydney") & (df["Medal"]=="Gold")]
# print(f"Number of golds won by Sydney are {len(sydn_list)}")

#number of Woman winning gold
# df=pd.read_excel("Summer-Olympic-medals-1976-to-2008student.xlsx")
# sydn_list=df.loc[(df["City"]=="Sydney") & (df["Medal"]=="Gold") & (df["Gender"]=="Women")]
# print(f"Number of Women from Sydney who Won Gold Medals are {len(sydn_list)}")

# Number of gold won by sydney
# df=pd.read_excel("Summer-Olympic-medals-1976-to-2008student.xlsx")
# sydn_list=df.loc[(df["City"]=="Sydney")]
# print(f"The number of Medals won by Sydney are {len(sydn_list)}")

# Medals in SPorts Aquatics
# df=pd.read_excel("Summer-Olympic-medals-1976-to-2008student.xlsx")
# sydn_list=df.loc[(df["Sport"]=="Aquatics")]
# print(f"The number of Medals won in Aquatics Sport are {len(sydn_list)}")

# Aquatics sport, Gold Medal, Women, From sydney
# df=pd.read_excel("Summer-Olympic-medals-1976-to-2008student.xlsx")
# sydn_list=df.loc[(df["Sport"]=="Aquatics") & (df["Medal"]=="Gold") & (df["Gender"]=="Women") & (df["City"]=="Sydney")]
# print(f"The number of gold medals won in Aquatics Sport by women from sydney are {len(sydn_list)}")

# assignment 4 starts here
# df=pd.read_excel("outlier_example2.xlsx")
# data=df["Salary of Employee in Rs"]

# for visualing box plot before removing outliars, please uncomment below lines for this
# plt.boxplot(data)
# plt.show
# while(True):
#     data=data.astype('float')
#     data=data.sort_values()
#     q1=data.quantile(0.25,interpolation='midpoint')
#     q3=data.quantile(0.75,interpolation='midpoint')
#     iqr=q3-q1

#     lower_range = q1-1.5*iqr
#     upper_range=q3+1.5*iqr
#     print(upper_range)
#     print(lower_range,upper_range)
#     outlier_index=data.loc[data>upper_range].index.to_list()
#     outlier_index.extend(data.loc[data<lower_range].index.to_list())
#     for x in outlier_index:
#         data=data.drop(x)
#     if len(outlier_index)==0:
#         break

    
# for visualising data after removing outliars, please uncomment below lines for this
# plt.boxplot(data)
# plt.show


# Linear Regression Code
# import pandas as pd
# from matplotlib import pyplot as plt
# import numpy as np
# from sklearn import linear_model 

# data = pd.read_csv("Salary_Data.csv")
# X = data['YearsExperience']
# Y = data['Salary']

# X = np.array(X).reshape((len(X),1))
# Y = np.array(Y).reshape((len(Y),1))
# model = linear_model.LinearRegression()
# model.fit(X,Y)
# Y_pred = model.predict(X)


# plt.figure()
# plt.scatter(X, Y, color='black', label="Given Values")
# plt.plot(X, Y_pred, color='green', linewidth=2, label="Prediction")
# plt.xlabel("Experience in Years")
# plt.ylabel("Salary in INR")
# plt.title('Result of Training Data')
# plt.legend()
# plt.show()


# K mean Cluster code
df=pd.read_excel("Clusterdata.xlsx")
df=df.dropna()
wcss=[]
x_axis=[]
for x in range(1,30,1):
    x_axis.append(x)
    cluster=KMeans(n_clusters=x,init="k-means++",n_init=10,algorithm="lloyd")
    cluster=cluster.fit(df)
    wcss.append(cluster.inertia_)
# uncomment below line one to see the Elbow Graph.
# sns.lineplot(x=x_axis,y=wcss)
# Value got from elbow graph is 15
cluster=KMeans(n_clusters=15,init="k-means++",n_init=10,algorithm="lloyd")
cluster=cluster.fit(df)
sns.scatterplot(x='x', y='y',data=df, hue=cluster.labels_,palette=sns.color_palette("husl", len(set(cluster.labels_)))).set_title('After figuring 15 as clusters')
plt.scatter(cluster.cluster_centers_[:,0],cluster.cluster_centers_[:,1],color="black",marker="x",label='Centroids')
# %%