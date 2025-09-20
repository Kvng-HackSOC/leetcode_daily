class Solution:
    def numDecodings(self, s):
        n = len(s)
        if n == 0 or s[0] == '0':
            return 0

        dp = [0] * (n + 1)
        dp[0], dp[1] = 1, 1  # empty string = 1 way, first char = 1 way (if not '0')

        for i in range(2, n + 1):
            one = int(s[i-1:i])       # last single digit
            two = int(s[i-2:i])       # last two digits

            if 1 <= one <= 9:        # valid single digit
                dp[i] += dp[i-1]
            if 10 <= two <= 26:      # valid two-digit code
                dp[i] += dp[i-2]

        return dp[n]
