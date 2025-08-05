class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        # Step 1: Combine both arrays
        combined = nums1 + nums2

        # Step 2: Sort the combined array
        combined.sort()

        # Step 3: Find the length
        n = len(combined)

        # Step 4: If length is odd, return the middle
        if n % 2 == 1:
            return combined[n // 2]
        else:
            # If even, return average of two middles
            mid1 = combined[n // 2]
            mid2 = combined[n // 2 - 1]
            return (mid1 + mid2) / 2.0
