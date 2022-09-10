from pandas import DataFrame
import matplotlib.pyplot as plt
import matplotlib
from sklearn.cluster import DBSCAN

x1 = [[10.0, 1.0], [10.0, 2.0], [10.0, 10.0], [10.0, 10.0], [10.0, 23.0], [10.0, 22.0]]
x2 = [[20.0, 2.0], [20.0, 15.0], [20.0, 26.0], [20.0, 13.0], [20.0, 32.0], [20.0, 35.0]]
x3 = [[30.0, 25.0], [30.0, 28.0], [30.0, 17.0], [30.0, 16.0], [30.0, 15.0], [30.0, 38.0]]
x4 = [[40.0, 1.0], [40.0, 2.0], [40.0, 16.0], [40.0, 41.0], [40.0, 40.0], [40.0, 39.0]]
x5 = [[60.0, 1.0], [60.0, 10.0], [60.0, 12.0], [60.0, 32.0], [60.0, 33.0], [60.0, 50.0]]
x6 = [[1,1], [1,2], [2,1] , [2,2], [8,8], [8,9], [9,8], [9,9] , [14,15], [14,14], [15,14] ,[15,15], [20,21], [20,20] , [21,21] , [21,20]]

df1 = DataFrame(data= x1) 
df2 = DataFrame(data= x2)
df3 = DataFrame(data= x3)
df4 = DataFrame(data= x4)
df5 = DataFrame(data= x5)
df6 = DataFrame(data= x6)

data = df2

dbscan_opt=DBSCAN(eps=3.0,min_samples=1).fit(data[[0,1]])

data['DBSCAN_opt_labels']=dbscan_opt.labels_
data['DBSCAN_opt_labels'].value_counts()

print(data)

# Plotting the resulting clusters
colors=['purple','red','blue','green', 'magenta', 'teal', 'black']
plt.figure(figsize=(6,6))
plt.scatter(data[0],data[1],c=data['DBSCAN_opt_labels'],cmap=matplotlib.colors.ListedColormap(colors),s=60)
plt.title('DBSCAN Clustering',fontsize=20)
plt.xlabel('Feature 1',fontsize=14)
plt.ylabel('Feature 2',fontsize=14)
plt.show()


