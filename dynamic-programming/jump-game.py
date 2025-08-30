class Solution:
    def canJump(self, nums):
        # 'goal' represents the last index we need to reach
        goal = len(nums) - 1

        # Traverse backwards from the end
        for i in range(len(nums) - 1, -1, -1):
            # If from position i, we can reach or cross 'goal'
            if i + nums[i] >= goal:
                goal = i  # Move the goalpost closer to the start

        # If we can bring goal to index 0, we can reach the end
        return goal == 0
