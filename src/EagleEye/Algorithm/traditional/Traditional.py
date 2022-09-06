from typing import overload
from EagleEye.Algorithm.Algorithm import Algorithm
from Elibs.Utils import *


class Traditional(Algorithm):
    def __init__(self) -> None:
        Algorithm.__init__(self)
        log("[+] init Traditional")

    def findPatterns(self):
        log("[+] [Traditional] findPatterns")