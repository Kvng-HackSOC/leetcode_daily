class Solution:
    def combinationSum(self, candidates, target):
        res = []
        
        def backtrack(start, path, total):
            # If total matches target, save combination
            if total == target:
                res.append(path[:])
                return
            
            # Stop exploring if total exceeds target
            if total > target:
                return
            
            # Explore further candidates
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(i, path, total + candidates[i])  # reuse allowed
                path.pop()
        
        backtrack(0, [], 0)
        return res
