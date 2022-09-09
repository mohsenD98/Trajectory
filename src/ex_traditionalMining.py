import pandas as pd

from EagleEye import *

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.simplefilter(action='ignore', category=UserWarning)


if __name__ == '__main__':
  # set runType [DEBUG(to see logs), RELEASE(to hide logs)]
  Utils.runMode = Runtype.DEBUG
  # get inputs from terminal or current test values
  Utils.inputsType = InputsType.DEFAULT_TESTS

  eye = EagleEye()  
  eye.setAlgorithm(AlgorithmType.TRADITIONAL)
  eye.loadDataset(dname= "/home/mohsen/code/trajectories/learnings/Trajectory/datasets/dataframe.geojson")
  eye.extractTrajectories(idColName= "id", timeColName="Timestamp", timeFormat= '%d/%m/%Y %H:%M:%S')
  eye.plotTrajectories()
