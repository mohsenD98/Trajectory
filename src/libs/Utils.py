import colorama
from colorama import Fore
import enum

class Runtype(enum.Enum):
   DEBUG = 1
   RELEASE = 2

class InputsType(enum.Enum):
   USER_TERMINAL = 1
   DEFAULT_TESTS = 2

runMode = Runtype.RELEASE
inputsType = InputsType.DEFAULT_TESTS

def log(input, important= False):
    if runMode == Runtype.DEBUG: 
      if important:
        print(Fore.RED+input)
      else:
         if type(input) == str:
            print(Fore.WHITE+input)
         else:
            print(input)

# get values from terminal
def get(message, inputLen):
    numList = list(map(float, input(Fore.RED+ message).strip().split()))[:inputLen]
    return numList

def run(command):
   if runMode == Runtype.DEBUG: 
      command()

def cartesianProductDictInList(mDict, mList):
   result = {}
   for key, value in mDict.items():
      for element in mList:
         result[str(key)+"-"+str(element)] = value
   return result
