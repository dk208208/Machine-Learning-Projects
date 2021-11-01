# -*- coding: utf-8 -*-
"""Predicting Price of House using KNearestNeighbour Regressor.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xraV7Dg-bUgt0aS8jSXRqjc_1brI_TUG
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
import seaborn as sns
from sklearn import preprocessing
from sklearn import metrics
import matplotlib.pyplot as plt
# %matplotlib inline

url = "https://raw.githubusercontent.com/edyoda/data-science-complete-tutorial/master/Data/house_rental_data.csv.txt"
dataset = pd.read_csv(url, index_col=[0])

dataset.head(10)

dataset.shape

dataset.describe()

dataset.dtypes

dataset.isna().sum()

dataset = dataset.rename(columns={"Living.Room":"Living Room"})

dataset.columns

dataset["Sqft"].value_counts()

dataset["Price"].value_counts()

dataset.corr()

sns.heatmap(dataset.corr())

sns.set()
plt.figure(figsize=(17,12))
sns.heatmap(dataset.corr(), annot=False, cmap=plt.cm.CMRmap_r)
plt.show()

figs = plt.figure(figsize=(15,7))
ax1 = figs.add_subplot(121)
ax2 = figs.add_subplot(122)
x = data["Price"]
ax1.hist(x)
ax2.boxplot(x);

figs = plt.figure(figsize=(15,7))
ax1 = figs.add_subplot(121)
ax2 = figs.add_subplot(122)
x = data["Sqft"]
ax1.hist(x)
ax2.boxplot(x);

plt.figure(figsize = (15,10))
sns.scatterplot(data = data, x = data['Sqft'], y = data['Price'], hue = 'Floor')

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)

pd.DataFrame(scaled_data).describe()

from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters = 4, init = 'k-means++')
kmeans.fit(scaled_data)

kmeans.inertia_

sse = []
for k in range(1,20):
    
    kmeans = KMeans(n_jobs = -1,n_clusters = k,init = 'k-means++')
    kmeans.fit(scaled_data)
    sse.append(kmeans.inertia_)

frame = pd.DataFrame({'Cluster':range(1,20), 'SSE':sse})
plt.figure(figsize=(12,6))
plt.plot(frame['Cluster'], frame['SSE'], marker='o')
plt.xlabel('Number of clusters')
plt.ylabel('Inertia')

kmeans = KMeans(n_jobs = -1, n_clusters = 6, init = 'k-means++')
kmeans.fit(scaled_data)
pred = kmeans.predict(scaled_data)

frame = pd.DataFrame(scaled_data)
frame['cluster'] = pred
frame['cluster'].value_counts()

kmeans = KMeans(n_jobs = -1, n_clusters = 8, init = 'k-means++')
kmeans.fit(scaled_data)
pred = kmeans.predict(scaled_data)

frame = pd.DataFrame(scaled_data)
frame['cluster'] = pred
frame['cluster'].value_counts()

