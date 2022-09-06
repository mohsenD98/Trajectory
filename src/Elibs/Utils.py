import enum

class Runtype(enum.Enum):
   DEBUG = 1
   RELEASE = 2

runMode = Runtype.RELEASE

def log(input):
    if runMode == Runtype.DEBUG: 
        print(input)