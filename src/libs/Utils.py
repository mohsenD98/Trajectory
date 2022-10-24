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
    if important:
       print(Fore.RED+input)

    if runMode == Runtype.DEBUG: 
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

# pretty Log Dict
def plog(d, indent=0):
   if runMode == Runtype.DEBUG: 
      for key, value in d.items():
         print('\t' * indent + str(key))
         if isinstance(value, dict):
            plog(value, indent+1)
         else:
            print('\t' * (indent+1) + str(value))

# pretty Log Dict
def ploglist(mlist, indent=0):
   if runMode == Runtype.DEBUG: 
      for d in mlist:
         plog(d)

# test
if __name__ == "__main__":
   # c = {}
   # c["1,2"] = ([1], 1)
   # c["3,4,5"] = ([1], 1)
   st = ["1,2", "3,4", "1", "234", "2,3", "3,4"]
   st=[x for x in st if len(x)>=2]
   print(st, st)
   # print(cartesianProductDictInList(c, st))

