class Solution:
    def grayCode(self, n):
        res = []
        for i in range(1 << n):      # loop 0..2^n-1
            res.append(i ^ (i >> 1)) # Gray code formula
        return res
