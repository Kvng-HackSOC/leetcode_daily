from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        def is_palindrome(substring):
            return substring == substring[::-1]

        def backtrack(start, path):
            # Base case: if we reach the end of the string
            if start == len(s):
                result.append(path[:])
                return

            # Try every possible partition
            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]
                if is_palindrome(substring):
                    path.append(substring)
                    backtrack(end, path)
                    path.pop()

        backtrack(0, [])
        return result
