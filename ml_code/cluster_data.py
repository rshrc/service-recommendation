# -*- coding: utf-8 -*-
"""
Created on Tue Aug 06 10:53:22 2019

@author: hp
"""

from pandas import Series, DataFrame
from sklearn.cluster import KMeans
import sklearn.metrics
import pickle as pk
from sklearn.preprocessing import LabelEncoder
raw_data = pd.read_csv("issues.csv")
raw_data.dtypes
raw_data.head()
#clust_data = raw_data.drop("PROBLEM_TYPE",axis=1)
#clust_data.head()
 

#Finding optimal no. of clusters using knee testx
from scipy.spatial.distance import cdist
clusters=range(1,10)
meanDistortions=[]
 
for k in clusters:
    model=KMeans(n_clusters=k)
    model.fit(clust_data)
    prediction=model.predict(clust_data)
    meanDistortions.append(sum(np.min(cdist(clust_data, model.cluster_centers_, 'euclidean'), axis=1)) / clust_data.shape[0])
 
#plt.cla()
plt.plot(clusters, meanDistortions, 'bx-')
plt.xlabel('k')
plt.ylabel('Average distortion')
plt.title('Selecting k with the Elbow Method')

#can be seen from graph that knee happens at k=3
#Optimal clusters is 3
final_model=KMeans(3)
final_model.fit(clust_data)
prediction=final_model.predict(clust_data)
 
#Join predicted clusters back to raw data
raw_data["GROUP"] = prediction
print("Groups Assigned : \n")
raw_data[["GROUP","PROBLEM_TYPE"]]
raw_data.head()
#We now do a set of boxplots to see how the groups differ for various feature attributes.
#We start off with Count.

#m = raw_data.groupby(['GROUP']).mean()
#m.COUNT

df=raw_data.groupby(["GROUP"])
print(df["PROBLEM_TYPE"])
