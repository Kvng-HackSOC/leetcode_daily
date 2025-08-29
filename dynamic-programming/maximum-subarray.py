class Solution:
    def maxSubArray(self, nums):
        max_sum = nums[0]
        curr_sum = nums[0]

        for num in nums[1:]:
            # Either extend the current subarray or start new at num
            curr_sum = max(num, curr_sum + num)
            max_sum = max(max_sum, curr_sum)

        return max_sum
