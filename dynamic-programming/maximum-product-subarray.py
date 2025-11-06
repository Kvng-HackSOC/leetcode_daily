class Solution:
    def maxProduct(self, nums):
        curr_max = curr_min = result = nums[0]

        for num in nums[1:]:
            temp = curr_max
            curr_max = max(num, num * curr_max, num * curr_min)
            curr_min = min(num, num * temp, num * curr_min)
            result = max(result, curr_max)

        return result
