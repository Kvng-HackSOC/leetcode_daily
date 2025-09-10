class Solution:
    def sortColors(self, nums):
        left, curr, right = 0, 0, len(nums) - 1

        while curr <= right:
            if nums[curr] == 0:  # red
                nums[left], nums[curr] = nums[curr], nums[left]
                left += 1
                curr += 1
            elif nums[curr] == 2:  # blue
                nums[right], nums[curr] = nums[curr], nums[right]
                right -= 1
            else:  # white
                curr += 1
