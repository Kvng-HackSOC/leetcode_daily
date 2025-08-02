# Problem: https://leetcode.com/problems/two-sum/
# Difficulty: Easy
# Tags: Array, Hash Table
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def twoSum(self, nums, target):
        # Create a dictionary to store value-to-index mappings
        num_map = {}
        
        # Iterate over the array
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                # Found the two indices
                return [num_map[complement], i]
            # Store the index of the current number
            num_map[num] = i

