# arrays/search-in-rotated-sorted-array.py

class Solution:
    def search(self, nums, target):
        """
        Returns the index of target in a rotated sorted array, or -1 if not found.
        Uses binary search with O(log n) runtime.
        """
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            
            # Check which side is properly sorted
            if nums[left] <= nums[mid]:  # Left side sorted
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:  # Right side sorted
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return -1
