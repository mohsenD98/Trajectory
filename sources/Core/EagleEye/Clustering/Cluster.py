# doc's: https://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html
# help: https://www.analyticsvidhya.com/blog/2020/09/how-dbscan-clustering-works/

from .ClusteringType import ClusteringType

import matplotlib.pyplot as plt  
import matplotlib
from pandas import DataFrame


class Cluster:
    def __init__(self) -> None:
        self.clusteringType = ClusteringType.DBSCAN
        # The number of samples (or total weight) in a neighborhood for a point to be considered as a core point.
        self.minSamples = 2
        # The maximum distance between two samples for one to be considered as in the neighborhood of the other
        self.maxDistance = 2

        self.numberOfClustersForKMeans = 3
        self.colorList=['purple','red','blue','green', 'magenta', 'teal', 'black']
        self.data = DataFrame(data=[])
    def __str__(self) -> str:
         return f"min sample = {self.minSamples} max distance = {self.maxDistance} "

    def setClusteringType(self, type):
        self.clusteringType = type

    def setData(self, df):
        self.data = df

    def setClusteringParams(self, min_samples, max_distance, k_means_cluster_count=3):
        self.minSamples = min_samples
        self.maxDistance = max_distance
        self.numberOfClustersForKMeans = k_means_cluster_count

    def calculate(self):
        if ClusteringType.DBSCAN == self.clusteringType:
            return self._calcDBSCAN()

        if ClusteringType.KMEANS == self.clusteringType:
            return self._calcKMeans()

    def _calcKMeans(self):
            from sklearn.cluster import KMeans
            k_means=KMeans(n_clusters=self.numberOfClustersForKMeans,random_state=42)
            k_means.fit(self.data[[0,1]])
            self.data['KMeans_labels']=k_means.labels_

            result = {}
            for index, row in self.data.iterrows():
                if row["KMeans_labels"] in result:
                    result[row["KMeans_labels"]].append(row[2]) # row[2] is id of trajectory
                else:
                    result[row["KMeans_labels"]] = [row[2]]
            
            return result
    def _calcDBSCAN(self):  
            from sklearn.cluster import DBSCAN
            dbscan_opt=DBSCAN(eps=self.maxDistance ,min_samples=self.minSamples,)
            dbscan_opt.fit(self.data[[0,1]])
            self.data['DBSCAN_labels']=dbscan_opt.labels_
            self.data['DBSCAN_labels'].value_counts()

            result = {}
            for index, row in self.data.iterrows():
                if row["DBSCAN_labels"] in result:
                    result[row["DBSCAN_labels"]].append(row[2]) # row[2] is id of trajectory
                else:
                    result[row["DBSCAN_labels"]] = [row[2]]
            
            return result
            
    def plot(self):
        plotTitle = ""
        if self.clusteringType == ClusteringType.DBSCAN:
            plotTitle = 'DBSCAN'

        if self.clusteringType == ClusteringType.KMEANS:
            plotTitle = 'KMeans'

        plt.figure(figsize=(4,4))
        plt.scatter(self.data[0],self.data[1],c=self.data[plotTitle+'_labels'],cmap=matplotlib.colors.ListedColormap(self.colorList),s=80)
        plt.title(plotTitle+" Clustering",fontsize=20)
        plt.xlabel('Feature 1',fontsize=14)
        plt.ylabel('Feature 2',fontsize=14)
        plt.show()
