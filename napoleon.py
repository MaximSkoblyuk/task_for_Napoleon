class Solution:
    def __init__(self):
        self.result = 0

    def romanToInt(self, s: str):
        dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        j = s[-1]
        self.result = dict[j]
        for x in s[-2::-1]:
            if dict[x] >= dict[j]:
                self.result += dict[x]
            else:
                self.result -= dict[x]
            j = x
        return self.result
