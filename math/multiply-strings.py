# math/multiply-strings.py

class Solution:
    def multiply(self, num1, num2):
        if num1 == "0" or num2 == "0":
            return "0"
        
        # result array with maximum possible length
        result = [0] * (len(num1) + len(num2))
        
        # reverse iterate through num1 and num2
        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                mul = int(num1[i]) * int(num2[j])
                # position in result array
                p1, p2 = i + j, i + j + 1
                # add to previous value
                summation = mul + result[p2]
                
                result[p2] = summation % 10
                result[p1] += summation // 10
        
        # build result string
        result_str = ''.join(map(str, result))
        
        # remove leading zeros
        return result_str.lstrip('0')
