from collections import Counter

class Solution:
    def minWindow(self, s, t):
        if not s or not t:
            return ""

        need = Counter(t)
        window = {}
        have, need_count = 0, len(need)
        res, res_len = [-1, -1], float("inf")

        left = 0
        for right, ch in enumerate(s):
            window[ch] = window.get(ch, 0) + 1

            if ch in need and window[ch] == need[ch]:
                have += 1

            while have == need_count:
                # update result if smaller window
                if (right - left + 1) < res_len:
                    res = [left, right]
                    res_len = right - left + 1

                # pop from the left
                window[s[left]] -= 1
                if s[left] in need and window[s[left]] < need[s[left]]:
                    have -= 1
                left += 1

        l, r = res
        return s[l:r+1] if res_len != float("inf") else ""
