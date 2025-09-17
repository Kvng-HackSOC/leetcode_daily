class Solution:
    def isScramble(self, s1, s2):
        if len(s1) != len(s2):
            return False

        if s1 == s2:
            return True

        if sorted(s1) != sorted(s2):
            return False

        memo = {}

        def dfs(a, b):
            if (a, b) in memo:
                return memo[(a, b)]

            if a == b:
                memo[(a, b)] = True
                return True

            if sorted(a) != sorted(b):
                memo[(a, b)] = False
                return False

            n = len(a)
            for i in range(1, n):
                # No swap
                if dfs(a[:i], b[:i]) and dfs(a[i:], b[i:]):
                    memo[(a, b)] = True
                    return True
                # Swap
                if dfs(a[:i], b[-i:]) and dfs(a[i:], b[:-i]):
                    memo[(a, b)] = True
                    return True

            memo[(a, b)] = False
            return False

        return dfs(s1, s2)


# Example test
if __name__ == "__main__":
    sol = Solution()
    print(sol.isScramble("great", "rgeat"))  # True
    print(sol.isScramble("abcde", "caebd"))  # False
    print(sol.isScramble("a", "a"))          # True
