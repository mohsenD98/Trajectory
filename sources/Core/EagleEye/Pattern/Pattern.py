class Pattern:
    def __init__(self, m, l, g, k) -> None:
        self.m = m
        self.l = l
        self.k = k
        self.g = g

    def validatePatternTime(self, timeSerie):
        # gap bigger than g is removed in the process so i will not check it here!
        # last segment len > L
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
        
        # min length of beeing togheter > k
        if flag and len(timeSerie) >= self.k: return [True]
        else: return [False]
