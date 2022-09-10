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

def log(input):
    if runMode == Runtype.DEBUG: 
        print(input)

# get values from terminal
def get(message, inputLen):
    numList = list(map(float, input(Fore.RED+ message).strip().split()))[:inputLen]
    return numList

def run(command):
   if runMode == Runtype.DEBUG: 
      command()