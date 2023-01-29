#%%
# imported libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.cluster import KMeans
from sklearn import linear_model 
# Converting dictionary it to data frame
# dict = {'English': [85, 73, 98], 'Math': [60, 80, 58],
#         'Science': [90, 60, 74], 'French': [95, 87, 92]}
# df = pd.DataFrame(dict, index=[2018, 2019, 2020])
# French 92 to 29
# print(df)
# print('Modify a single value:')
# print('\n')
# df.loc[2020,"French"]=29
# print(df)
# print('\n')
# # Means of english and science
# print("Mean of English is \n")
# print(df["English"].mean())
# print("Mean of Science is \n")
# print(df['Science'].mean())

# Adding economics section
# economics_value=[99,99,99]
# df["Economics"]=economics_value
# print(df)

# changing values of economics
# df.loc[2019,"Economics"]=54
# df.loc[2020,"Economics"]=45
# print(df)

# Q2 C
# Deleting economics columns
# del df["Economics"]
#changing data types
# df = df.astype({"English":float,"Math":float,"Science":float,"French":float})
# df.loc[2022] = [89, 21, 87,59]
# print(df)
# Q2 C-----------------------

# Delete 2018 row
# df.drop(2018,inplace=True)
# print(df)

# count of actors with movies above then 460
# some missing values
# NaN = np.nan
# df = pd.DataFrame({'Name': ['Amitabh', 'Rekha',
#                             'SHARUKH', 'SALMAN',
#                             'PRIYANKA', 'HEMA'],
#                    'MOVIES': [500, 470, 450, 467, NaN, 340],
#                    'SERIAL': [45, 3, NaN, 2, 1, 1],
#                    'ADDS': [13, 10, 15, NaN, NaN, 13]})
# df.fillna(0,inplace=True)
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
# mean_rad=ld["radius (cm)"].mean()
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

# data = pd.read_csv("Salary_Data.csv")
# X = data['YearsExperience']
# Y = data['Salary']

# X = np.array(X).reshape((len(X),1))
# Y = np.array(Y).reshape((len(Y),1))
# model = linear_model.LinearRegression()
# model.fit(X,Y)
# Y_pred = model.predict(X)

# sns.scatterplot(x=X.ravel(),y=Y.ravel())
# sns.lineplot(x=X.ravel(),y=Y_pred.ravel())
# plt.show()

# K mean Cluster code
# df=pd.read_excel("Clusterdata.xlsx")
# df=df.dropna()
# wcss=[]
# x_axis=[]
# for x in range(1,30,1):
#     x_axis.append(x)
#     cluster=KMeans(n_clusters=x,init="k-means++",n_init=10,algorithm="lloyd")
#     cluster=cluster.fit(df)
#     wcss.append(cluster.inertia_)
# # uncomment below line one to see the Elbow Graph.
# sns.lineplot(x=x_axis,y=wcss)
# # Value got from elbow graph is 15
# cluster=KMeans(n_clusters=15,init="k-means++",n_init=10,algorithm="lloyd")
# cluster=cluster.fit(df)
# sns.scatterplot(x='X', y='Y',data=df, hue=cluster.labels_,palette=sns.color_palette("husl", len(set(cluster.labels_)))).set_title('After figuring 15 as clusters')

# plt.scatter(cluster.cluster_centers_[:,0],cluster.cluster_centers_[:,1],color="black",marker="x",label='Centroids')
# plt.show()

# Kmean clustering 2, finding accuracy
# df=pd.read_csv("IRIS.csv")
# df=df.dropna()
# test=df.loc[:,["sepal_length","sepal_width","petal_length","petal_width"]] # just slicing this list
# cluster=KMeans(n_clusters=3,init="k-means++",n_init=10)
# cluster=cluster.fit(test)
# # making dataframe to find numerical ground truth of all the flowers

# new_df=pd.DataFrame({
#     "Cluster":cluster.labels_,
#     "species":df["species"],
# })
# i_s=new_df.loc[(new_df['species']=="Iris-setosa")]
# i_versi=new_df.loc[(new_df["species"]=="Iris-versicolor")]
# i_vergi=new_df.loc[(new_df["species"]=="Iris-virginica")]
# # Had to use mode to get the cluster for the name
# i_s_value=(i_s["Cluster"].mode())
# i_versi_value=(i_versi["Cluster"].mode())
# i_vergi_value=(i_vergi["Cluster"].mode())

# #lets replace species dataframe real values with what we have received
# species=df["species"]
# species.replace(["Iris-setosa","Iris-versicolor","Iris-virginica"],[i_s_value,i_versi_value,i_vergi_value],inplace=True)
# species=species.tolist()

# # Trying to find accuracy by running a for loop.
# l=0
# for x in range(len(species)):
#     if species[x]==cluster.labels_[x]:
#         l+=1
# accuracy=(l/len(species))*100
# # l is the amount of times our predicted value was equal to ground truth, and accuracy is just l/number of entries of species
# print(f"accuracy of the model is {accuracy}%")
# print("Initial running ended")

# # asking the user for more 
# choic=str(input("Do you want to Run the algorithim 5 times with different seed points(Y/N): "))

# # Re-running the above code atleast 5 times with different seed points and commenting
# if choic.upper()=="YES" or choic.upper()=="Y":
#     for time in range(5):
#         cluster=KMeans(n_clusters=3,init='k-means++',n_init=10)
#         cluster=cluster.fit(test)
#         # making dataframe to find numerical ground truth of all the flowers

#         new_df=pd.DataFrame({
#             "Cluster":cluster.labels_,
#             "species":df["species"],
#         })
#         i_s=new_df.loc[(new_df['species']=="Iris-setosa")]
#         i_versi=new_df.loc[(new_df["species"]=="Iris-versicolor")]
#         i_vergi=new_df.loc[(new_df["species"]=="Iris-virginica")]
#         # Had to use mode to get the cluster for the name
#         i_s_value=(i_s["Cluster"].mode())
#         i_versi_value=(i_versi["Cluster"].mode())
#         i_vergi_value=(i_vergi["Cluster"].mode())

#         #lets replace species dataframe real values with what we have received
#         species=df["species"]
#         species.replace(["Iris-setosa","Iris-versicolor","Iris-virginica"],[i_s_value,i_versi_value,i_vergi_value],inplace=True)
#         species=species.tolist()

#         # Trying to find accuracy by running a for loop.
#         l=0
#         for x in range(len(species)):
#             if species[x]==cluster.labels_[x]:
#                 l+=1
#         accuracy=(l/len(species))*100
#         # l is the amount of times our predicted value was equal to ground truth, and accuracy is just l/number of entries of species
#         print(f"accuracy of the model for the {time+1} time is {accuracy}%")
#     print("Accuracy of the model is changing with random seed points")
    
# %%