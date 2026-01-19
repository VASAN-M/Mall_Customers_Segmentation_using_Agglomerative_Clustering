

import numpy as np
import pandas as pd

df=pd.read_csv(r'/content/Mall_Customers.csv')

df.info()

df.describe()

df.shape

for col in df.columns:
  print(df[col].name,df[col].value_counts().nunique())

df['Genre']=df['Genre'].map({'Male':0,'Female':1})

from sklearn.cluster import AgglomerativeClustering
model=AgglomerativeClustering(linkage='complete',n_clusters=5,metric='euclidean')
x=df[['Annual_Income_(k$)','Spending_Score']]
y=model.fit_predict(x)

import scipy.cluster.hierarchy as sch
dendrogram=sch.dendrogram(sch.linkage(x,method='complete'))

import matplotlib.pyplot as plt
plt.scatter(x['Annual_Income_(k$)'],x['Spending_Score'],c=y,s=15)
plt.title('agglomerative')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.show()