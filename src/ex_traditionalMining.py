import pandas as pd

from EagleEye import *

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.simplefilter(action='ignore', category=UserWarning)

from ex_makePlot import geoDf

if __name__ == '__main__':
  # set runType [DEBUG(to see logs), RELEASE(to hide logs)]
  Utils.runMode = Runtype.DEBUG

  eye = EagleEye()  
  eye.setGeoDf(gdf= geoDf, idColName= "id", timeColName="Timestamp", timeFormat= '%d/%m/%Y %H:%M:%S')
  eye.setAlgorithm(AlgorithmType.TRADITIONAL)
  eye.findPatterns()
