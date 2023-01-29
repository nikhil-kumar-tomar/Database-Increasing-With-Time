# %%
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier


# df=pd.read_excel("Clusterdata.xlsx")
# knn=KNeighborsClassifier(n_neighbors=7)
# knn.fit(np.array(df["X"]).reshape(len(df["X"]),1),df["Y"])
# y_pred=knn.predict([[0.1]])
# print(y_pred)
# sns.scatterplot(x="X",y="Y",data=df)
# sns.scatterplot(x=0.8,y=y_pred)



df=pd.read_csv("IRIS.csv")
del df["species"]
model=PCA(n_components=len(df.columns))
data=model.fit_transform(df)
rf=pd.DataFrame(data=data,columns=["PC1","PC2","PC3","PC4"])
explained_variance = model.explained_variance_ # eigenvalues we have found
explained_variance_ratio=model.explained_variance_ratio_ # ratio of most data variance
# sns.scatterplot(x=rf["PC1"],y=rf["PC2"])

wcss=[]
X=np.array(rf["PC1"]).reshape(len(rf["PC1"]),1)
Y=np.array(rf["PC2"]).reshape(len(rf["PC2"]),1)
lis=[]
# for x in range(1,10):
#     lis.append(x)
#     model=KMeans(n_clusters=x,init="k-means++")
#     model.fit(rf)
#     wcss.append(model.inertia_)
# sns.lineplot(y=wcss,x=lis)
cluster=KMeans(n_clusters=2,n_init=10)
cluster.fit(X,Y)
sns.scatterplot(x=rf["PC1"],y=rf["PC2"],hue=cluster.labels_,palette=sns.color_palette("husl", len(set(cluster.labels_))))
print(cluster.cluster_centers_)
# %%