class Solution:
    def productQueries(self, n, queries):
        MOD = 10**9 + 7
        
        # Step 1: Get the list of powers of 2 that sum to n
        powers = []
        bit = 0
        while n > 0:
            if n & 1:
                powers.append(1 << bit)  # 1 << bit is 2**bit
            n >>= 1
            bit += 1
        
        # Step 2: Precompute prefix products to answer queries fast
        prefix = [1] * (len(powers) + 1)
        for i in range(len(powers)):
            prefix[i + 1] = (prefix[i] * powers[i]) % MOD
        
        # Step 3: Answer each query using prefix products
        result = []
        for left, right in queries:
            prod = (prefix[right + 1] * pow(prefix[left], MOD - 2, MOD)) % MOD
            result.append(prod)
        
        return result
