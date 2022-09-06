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
  {'id':2, 'geometry':Point(20, 25), 'Timestamp':datetime(2022,1,1,12,5,0)},
  {'id':2, 'geometry':Point(30, 28), 'Timestamp':datetime(2022,1,1,12,6,0)},
  {'id':2, 'geometry':Point(40, 2), 'Timestamp':datetime(2022,1,1,12,7,0)},
  {'id':2, 'geometry':Point(50, 1), 'Timestamp':datetime(2022,1,1,12,8,0)},
  {'id':2, 'geometry':Point(60, 20), 'Timestamp':datetime(2022,1,1,12,9,0)},
  
  {'id':3, 'geometry':Point(10, 20), 'Timestamp':datetime(2022,1,1,12,4,0)},
  {'id':3, 'geometry':Point(20, 26), 'Timestamp':datetime(2022,1,1,12,5,0)},
  {'id':3, 'geometry':Point(30, 27), 'Timestamp':datetime(2022,1,1,12,6,0)},
  {'id':3, 'geometry':Point(40, 26), 'Timestamp':datetime(2022,1,1,12,7,0)},
  {'id':3, 'geometry':Point(50, 3), 'Timestamp':datetime(2022,1,1,12,8,0)},
  {'id':3, 'geometry':Point(60, 22), 'Timestamp':datetime(2022,1,1,12,9,0)},
  
  {'id':4, 'geometry':Point(10, 22), 'Timestamp':datetime(2022,1,1,12,4,0)},
  {'id':4, 'geometry':Point(20, 23), 'Timestamp':datetime(2022,1,1,12,5,0)},
  {'id':4, 'geometry':Point(30 ,26), 'Timestamp':datetime(2022,1,1,12,6,0)},
  {'id':4, 'geometry':Point(40, 51), 'Timestamp':datetime(2022,1,1,12,7,0)},
  {'id':4, 'geometry':Point(50, 25), 'Timestamp':datetime(2022,1,1,12,8,0)},
  {'id':4, 'geometry':Point(60, 42), 'Timestamp':datetime(2022,1,1,12,9,0)},

  {'id':5, 'geometry':Point(10, 33), 'Timestamp':datetime(2022,1,1,12,4,0)},
  {'id':5, 'geometry':Point(20, 42), 'Timestamp':datetime(2022,1,1,12,5,0)},
  {'id':5, 'geometry':Point(30, 25), 'Timestamp':datetime(2022,1,1,12,6,0)},
  {'id':5, 'geometry':Point(40, 50), 'Timestamp':datetime(2022,1,1,12,7,0)},
  {'id':5, 'geometry':Point(50, 48), 'Timestamp':datetime(2022,1,1,12,8,0)},
  {'id':5, 'geometry':Point(60, 43), 'Timestamp':datetime(2022,1,1,12,9,0)},

  {'id':6, 'geometry':Point(10, 32), 'Timestamp':datetime(2022,1,1,12,4,0)},
  {'id':6, 'geometry':Point(20, 45), 'Timestamp':datetime(2022,1,1,12,5,0)},
  {'id':6, 'geometry':Point(30, 48), 'Timestamp':datetime(2022,1,1,12,6,0)},
  {'id':6, 'geometry':Point(40, 49), 'Timestamp':datetime(2022,1,1,12,7,0)},
  {'id':6, 'geometry':Point(50, 47), 'Timestamp':datetime(2022,1,1,12,8,0)},
  {'id':6, 'geometry':Point(60, 60), 'Timestamp':datetime(2022,1,1,12,9,0)}
  ])

geoDf = GeoDataFrame(df)

if __name__ == '__main__':
    eye = EagleEye()
    eye.setGeoDf(gdf= geoDf, idColName= "id", timeColName="Timestamp", timeFormat= '%d/%m/%Y %H:%M:%S')
    eye.plotGeoDf()
