from pandas import DataFrame
from EagleEye.Clustering.Cluster import Cluster
from EagleEye.Clustering.ClusteringType import ClusteringType

df = DataFrame(data= [(10,1), (10, 1.5), (20,4), (20, 5), (30, 1), (30, 2)]) 

c = Cluster()
c.setClusteringType(ClusteringType.KMEANS)
c.setData(df)
c.setClusteringParams(min_samples=2 ,max_distance=2, k_means_cluster_count= 3) # k_means_cluster_count just used in KMEANS 
c.calculate()
c.plot()