class Solution:
    def findMin(self, nums):
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            # If middle element is greater than the rightmost, 
            # the smallest value is to the right
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
                
        return nums[left]
