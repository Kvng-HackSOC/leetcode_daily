class Solution:
    def threeSumClosest(self, nums, target):
        # guard (shouldn't be needed on LeetCode because of constraints)
        if not nums or len(nums) < 3:
            return None

        nums.sort()
        n = len(nums)
        closest_sum = nums[0] + nums[1] + nums[2]

        for i in range(n - 2):
            left, right = i + 1, n - 1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                # update closest if this is better
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum

                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    # exact match
                    return current_sum

        return closest_sum


# --- quick local test ---
if __name__ == "__main__":
    print(Solution().threeSumClosest([-1, 2, 1, -4], 1))  # expected output: 2
