from EagleEye.Pattern.PatternType import PatternType

class Pattern:
    def __init__(self, m, l, g, k) -> None:
        self.m = m
        self.l = l
        self.k = k
        self.g = g

    def validatePattern(self, timeSerie):
        if self.isPlatoon(serie= timeSerie):
            return [True, PatternType.PLATOON]
        else:
            return [False, PatternType.NONE]

    def isPlatoon(self, serie):
        if len(serie) >= self.k: return True
