# arrays/next-permutation.py

class Solution:
    def nextPermutation(self, nums):
        """
        Rearranges nums into the next lexicographical permutation.
        If not possible, rearranges into the lowest possible order.
        Modifies nums in-place using constant extra memory.
        """
        # Step 1: Find first decreasing element from the right
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # Step 2: If such element found, find element just larger than nums[i] from right
        if i >= 0:
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]  # Swap

        # Step 3: Reverse the elements after index i
        left, right = i + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
