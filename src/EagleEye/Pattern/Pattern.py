from EagleEye.Pattern.PatternType import PatternType

class Pattern:
    def __init__(self, m, l, g, k) -> None:
        self.m = m
        self.l = l
        self.k = k
        self.g = g

    def validatePattern(self, timeSerie):
        counter = 1
        flag = False
        if self.l == 1:
            flag = True
        lastElement = timeSerie[-1]
        for element in timeSerie[-2::-1]:
            if lastElement - element == 1:
                counter += 1
                if counter >= self.l:
                    flag = True
                    break
            else:
                if counter >= self.l:
                    flag = True
                    break

        if flag and len(timeSerie) >= self.k: return [True]
        else: return [False]