import pandas as pd

from datetime import datetime
from EagleEye import *
from geopandas import GeoDataFrame
from shapely.geometry import Point

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.simplefilter(action='ignore', category=UserWarning)

# example in Fig1 in "A General and Parallel Platform for Mining Co-Movement Patterns over Large-scale Trajectories"
df1 = pd.DataFrame([
  {'id':1, 'geometry':Point(10, 1), 'Timestamp':datetime(2022,1,1,12,4,0)},
  {'id':1, 'geometry':Point(20, 2), 'Timestamp':datetime(2022,1,1,12,5,0)},
  {'id':1, 'geometry':Point(30, 25), 'Timestamp':datetime(2022,1,1,12,6,0)},
  {'id':1, 'geometry':Point(40, 1), 'Timestamp':datetime(2022,1,1,12,7,0)},
  {'id':1, 'geometry':Point(50, 2), 'Timestamp':datetime(2022,1,1,12,8,0)},
  {'id':1, 'geometry':Point(60, 1), 'Timestamp':datetime(2022,1,1,12,9,0)},
  
  {'id':2, 'geometry':Point(10, 2), 'Timestamp':datetime(2022,1,1,12,4,0)},
  {'id':2, 'geometry':Point(20, 15), 'Timestamp':datetime(2022,1,1,12,5,0)},
  {'id':2, 'geometry':Point(30, 26), 'Timestamp':datetime(2022,1,1,12,6,0)},
  {'id':2, 'geometry':Point(40, 2), 'Timestamp':datetime(2022,1,1,12,7,0)},
  {'id':2, 'geometry':Point(50, 1), 'Timestamp':datetime(2022,1,1,12,8,0)},
  {'id':2, 'geometry':Point(60, 10), 'Timestamp':datetime(2022,1,1,12,9,0)},
  
  {'id':3, 'geometry':Point(10, 10), 'Timestamp':datetime(2022,1,1,12,4,0)},
  {'id':3, 'geometry':Point(20, 16), 'Timestamp':datetime(2022,1,1,12,5,0)},
  {'id':3, 'geometry':Point(30, 27), 'Timestamp':datetime(2022,1,1,12,6,0)},
  {'id':3, 'geometry':Point(40, 16), 'Timestamp':datetime(2022,1,1,12,7,0)},
  {'id':3, 'geometry':Point(50, 3), 'Timestamp':datetime(2022,1,1,12,8,0)},
  {'id':3, 'geometry':Point(60, 12), 'Timestamp':datetime(2022,1,1,12,9,0)},
  
  {'id':4, 'geometry':Point(10, 11), 'Timestamp':datetime(2022,1,1,12,4,0)},
  {'id':4, 'geometry':Point(20, 17), 'Timestamp':datetime(2022,1,1,12,5,0)},
  {'id':4, 'geometry':Point(30 ,28), 'Timestamp':datetime(2022,1,1,12,6,0)},
  {'id':4, 'geometry':Point(40, 41), 'Timestamp':datetime(2022,1,1,12,7,0)},
  {'id':4, 'geometry':Point(50, 15), 'Timestamp':datetime(2022,1,1,12,8,0)},
  {'id':4, 'geometry':Point(60, 32), 'Timestamp':datetime(2022,1,1,12,9,0)},

  {'id':5, 'geometry':Point(10, 23), 'Timestamp':datetime(2022,1,1,12,4,0)},
  {'id':5, 'geometry':Point(20, 30), 'Timestamp':datetime(2022,1,1,12,5,0)},
  {'id':5, 'geometry':Point(30, 29), 'Timestamp':datetime(2022,1,1,12,6,0)},
  {'id':5, 'geometry':Point(40, 40), 'Timestamp':datetime(2022,1,1,12,7,0)},
  {'id':5, 'geometry':Point(50, 38), 'Timestamp':datetime(2022,1,1,12,8,0)},
  {'id':5, 'geometry':Point(60, 33), 'Timestamp':datetime(2022,1,1,12,9,0)},

  {'id':6, 'geometry':Point(10, 22), 'Timestamp':datetime(2022,1,1,12,4,0)},
  {'id':6, 'geometry':Point(20, 32), 'Timestamp':datetime(2022,1,1,12,5,0)},
  {'id':6, 'geometry':Point(30, 38), 'Timestamp':datetime(2022,1,1,12,6,0)},
  {'id':6, 'geometry':Point(40, 39), 'Timestamp':datetime(2022,1,1,12,7,0)},
  {'id':6, 'geometry':Point(50, 37), 'Timestamp':datetime(2022,1,1,12,8,0)},
  {'id':6, 'geometry':Point(60, 50), 'Timestamp':datetime(2022,1,1,12,9,0)}
  ])

# example in Fig4 in "A General and Parallel Platform for Mining Co-Movement Patterns over Large-scale Trajectories"
df2 = pd.DataFrame([
  {'id':1, 'geometry':Point(10, 60), 'Timestamp':datetime(2022,1,1,12,4,0)},
  {'id':1, 'geometry':Point(15, 50), 'Timestamp':datetime(2022,1,1,12,5,0)},
  {'id':1, 'geometry':Point(10, 40), 'Timestamp':datetime(2022,1,1,12,6,0)},
  {'id':1, 'geometry':Point(10, 30), 'Timestamp':datetime(2022,1,1,12,7,0)},
  {'id':1, 'geometry':Point(10, 20), 'Timestamp':datetime(2022,1,1,12,8,0)},
  {'id':1, 'geometry':Point(10, 10), 'Timestamp':datetime(2022,1,1,12,9,0)},
  
  {'id':2, 'geometry':Point(11, 60), 'Timestamp':datetime(2022,1,1,12,4,0)},
  {'id':2, 'geometry':Point(16, 50), 'Timestamp':datetime(2022,1,1,12,5,0)},
  {'id':2, 'geometry':Point(20, 40), 'Timestamp':datetime(2022,1,1,12,6,0)},
  {'id':2, 'geometry':Point(11, 30), 'Timestamp':datetime(2022,1,1,12,7,0)},
  {'id':2, 'geometry':Point(20, 20), 'Timestamp':datetime(2022,1,1,12,8,0)},
  {'id':2, 'geometry':Point(20, 10), 'Timestamp':datetime(2022,1,1,12,9,0)},
  
  {'id':3, 'geometry':Point(20, 60), 'Timestamp':datetime(2022,1,1,12,4,0)},
  {'id':3, 'geometry':Point(30, 50), 'Timestamp':datetime(2022,1,1,12,5,0)},
  {'id':3, 'geometry':Point(22, 40), 'Timestamp':datetime(2022,1,1,12,6,0)},
  {'id':3, 'geometry':Point(20, 30), 'Timestamp':datetime(2022,1,1,12,7,0)},
  {'id':3, 'geometry':Point(21, 20), 'Timestamp':datetime(2022,1,1,12,8,0)},
  {'id':3, 'geometry':Point(21, 10), 'Timestamp':datetime(2022,1,1,12,9,0)},
  
  {'id':4, 'geometry':Point(22, 60), 'Timestamp':datetime(2022,1,1,12,4,0)},
  {'id':4, 'geometry':Point(31, 50), 'Timestamp':datetime(2022,1,1,12,5,0)},
  {'id':4, 'geometry':Point(33, 40), 'Timestamp':datetime(2022,1,1,12,6,0)},
  {'id':4, 'geometry':Point(22, 30), 'Timestamp':datetime(2022,1,1,12,7,0)},
  {'id':4, 'geometry':Point(22, 20), 'Timestamp':datetime(2022,1,1,12,8,0)},
  {'id':4, 'geometry':Point(31, 10), 'Timestamp':datetime(2022,1,1,12,9,0)},

  {'id':5, 'geometry':Point(30, 60), 'Timestamp':datetime(2022,1,1,12,4,0)},
  {'id':5, 'geometry':Point(32, 50), 'Timestamp':datetime(2022,1,1,12,5,0)},
  {'id':5, 'geometry':Point(34, 40), 'Timestamp':datetime(2022,1,1,12,6,0)},
  {'id':5, 'geometry':Point(30, 30), 'Timestamp':datetime(2022,1,1,12,7,0)},
  {'id':5, 'geometry':Point(30, 20), 'Timestamp':datetime(2022,1,1,12,8,0)},
  {'id':5, 'geometry':Point(33, 10), 'Timestamp':datetime(2022,1,1,12,9,0)},

  {'id':6, 'geometry':Point(31, 60), 'Timestamp':datetime(2022,1,1,12,4,0)},
  {'id':6, 'geometry':Point(33, 50), 'Timestamp':datetime(2022,1,1,12,5,0)},
  {'id':6, 'geometry':Point(40, 40), 'Timestamp':datetime(2022,1,1,12,6,0)},
  {'id':6, 'geometry':Point(31, 30), 'Timestamp':datetime(2022,1,1,12,7,0)},
  {'id':6, 'geometry':Point(31, 20), 'Timestamp':datetime(2022,1,1,12,8,0)},
  {'id':6, 'geometry':Point(40, 10), 'Timestamp':datetime(2022,1,1,12,9,0)},
  ])
geoDf = GeoDataFrame(df1)
geoDf.plot()
plt.show()

geoDf.to_file('general_dataframe_fig1.geojson', driver='GeoJSON')  