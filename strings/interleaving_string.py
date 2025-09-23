class Solution(object):
    def isInterleave(self, s1, s2, s3):
        # If lengths don't add up, it's not possible
        if len(s1) + len(s2) != len(s3):
            return False

        # dp[i][j] means if s3[:i+j] can be formed by interleaving s1[:i] and s2[:j]
        dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        dp[0][0] = True

        # Fill first column (only s1)
        for i in range(1, len(s1) + 1):
            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]

        # Fill first row (only s2)
        for j in range(1, len(s2) + 1):
            dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]

        # Fill the rest
        for i in range(1, len(s1) + 1):
            for j in range(1, len(s2) + 1):
                dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or \
                           (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1])

        return dp[-1][-1]
