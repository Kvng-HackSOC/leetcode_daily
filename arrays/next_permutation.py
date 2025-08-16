class Solution:
    def nextPermutation(self, nums):
        # Step 1: Find the first index 'i' from the end where nums[i] < nums[i+1]
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # Step 2: If such index is found, find 'j' to swap with
        if i >= 0:
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        # Step 3: Reverse the part after index i
        left, right = i + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


# Example usage
nums = [1, 2, 3]
Solution().nextPermutation(nums)
print(nums)  # Output: [1, 3, 2]
