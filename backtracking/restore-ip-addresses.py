class Solution:
    def restoreIpAddresses(self, s):
        res = []

        def backtrack(start, path):
            # If we have 4 segments and used all characters, it's a valid IP
            if len(path) == 4 and start == len(s):
                res.append(".".join(path))
                return
            # If segments exceed 4, stop exploring
            if len(path) >= 4:
                return

            # Try segments of length 1 to 3
            for length in range(1, 4):
                if start + length > len(s):
                    break
                segment = s[start:start+length]

                # Skip leading zeros unless the segment is "0"
                if segment.startswith("0") and len(segment) > 1:
                    continue

                # Convert to int and check if valid range
                if int(segment) > 255:
                    continue

                # Recurse with next segment
                backtrack(start + length, path + [segment])

        backtrack(0, [])
        return res
