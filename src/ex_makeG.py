import pandas as pd

from datetime import datetime
from EagleEye import *
from geopandas import GeoDataFrame
from shapely.geometry import Point

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.simplefilter(action='ignore', category=UserWarning)

df = pd.DataFrame([
  {'id':1, 'geometry':Point(10, 1), 'Timestamp':datetime(2022,1,1,12,4,0)},
  {'id':1, 'geometry':Point(20, 2), 'Timestamp':datetime(2022,1,1,12,5,0)},
  {'id':1, 'geometry':Point(30, 25), 'Timestamp':datetime(2022,1,1,12,6,0)},
  {'id':1, 'geometry':Point(40, 1), 'Timestamp':datetime(2022,1,1,12,7,0)},
  {'id':1, 'geometry':Point(50, 2), 'Timestamp':datetime(2022,1,1,12,8,0)},
  {'id':1, 'geometry':Point(60, 1), 'Timestamp':datetime(2022,1,1,12,9,0)},
  
  {'id':2, 'geometry':Point(10, 2), 'Timestamp':datetime(2022,1,1,12,4,0)},
  {'id':2, 'geometry':Point(20, 15), 'Timestamp':datetime(2022,1,1,12,5,0)},
  {'id':2, 'geometry':Point(30, 28), 'Timestamp':datetime(2022,1,1,12,6,0)},
  {'id':2, 'geometry':Point(40, 2), 'Timestamp':datetime(2022,1,1,12,7,0)},
  {'id':2, 'geometry':Point(50, 1), 'Timestamp':datetime(2022,1,1,12,8,0)},
  {'id':2, 'geometry':Point(60, 10), 'Timestamp':datetime(2022,1,1,12,9,0)},
  
  {'id':3, 'geometry':Point(10, 10), 'Timestamp':datetime(2022,1,1,12,4,0)},
  {'id':3, 'geometry':Point(20, 26), 'Timestamp':datetime(2022,1,1,12,5,0)},
  {'id':3, 'geometry':Point(30, 17), 'Timestamp':datetime(2022,1,1,12,6,0)},
  {'id':3, 'geometry':Point(40, 16), 'Timestamp':datetime(2022,1,1,12,7,0)},
  {'id':3, 'geometry':Point(50, 3), 'Timestamp':datetime(2022,1,1,12,8,0)},
  {'id':3, 'geometry':Point(60, 12), 'Timestamp':datetime(2022,1,1,12,9,0)},
  
  {'id':4, 'geometry':Point(10, 10), 'Timestamp':datetime(2022,1,1,12,4,0)},
  {'id':4, 'geometry':Point(20, 13), 'Timestamp':datetime(2022,1,1,12,5,0)},
  {'id':4, 'geometry':Point(30 ,16), 'Timestamp':datetime(2022,1,1,12,6,0)},
  {'id':4, 'geometry':Point(40, 41), 'Timestamp':datetime(2022,1,1,12,7,0)},
  {'id':4, 'geometry':Point(50, 15), 'Timestamp':datetime(2022,1,1,12,8,0)},
  {'id':4, 'geometry':Point(60, 32), 'Timestamp':datetime(2022,1,1,12,9,0)},

  {'id':5, 'geometry':Point(10, 23), 'Timestamp':datetime(2022,1,1,12,4,0)},
  {'id':5, 'geometry':Point(20, 32), 'Timestamp':datetime(2022,1,1,12,5,0)},
  {'id':5, 'geometry':Point(30, 15), 'Timestamp':datetime(2022,1,1,12,6,0)},
  {'id':5, 'geometry':Point(40, 40), 'Timestamp':datetime(2022,1,1,12,7,0)},
  {'id':5, 'geometry':Point(50, 38), 'Timestamp':datetime(2022,1,1,12,8,0)},
  {'id':5, 'geometry':Point(60, 33), 'Timestamp':datetime(2022,1,1,12,9,0)},

  {'id':6, 'geometry':Point(10, 22), 'Timestamp':datetime(2022,1,1,12,4,0)},
  {'id':6, 'geometry':Point(20, 35), 'Timestamp':datetime(2022,1,1,12,5,0)},
  {'id':6, 'geometry':Point(30, 38), 'Timestamp':datetime(2022,1,1,12,6,0)},
  {'id':6, 'geometry':Point(40, 39), 'Timestamp':datetime(2022,1,1,12,7,0)},
  {'id':6, 'geometry':Point(50, 37), 'Timestamp':datetime(2022,1,1,12,8,0)},
  {'id':6, 'geometry':Point(60, 50), 'Timestamp':datetime(2022,1,1,12,9,0)}
  ])

geoDf = GeoDataFrame(df)

geoDf.to_file('dataframe.geojson', driver='GeoJSON')  