from collections import Counter

class Solution:
    def findSubstring(self, s, words):
        if not s or not words:
            return []
        L = len(words[0])
        k = len(words)
        total = L * k
        n = len(s)
        if n < total:
            return []

        need = Counter(words)
        ans = []

        for start in range(L):
            left = start
            seen = Counter()
            count = 0

            for right in range(start, n - L + 1, L):
                w = s[right:right + L]

                if w in need:
                    seen[w] += 1
                    count += 1

                    while seen[w] > need[w]:
                        left_word = s[left:left + L]
                        seen[left_word] -= 1
                        left += L
                        count -= 1

                    if count == k:
                        ans.append(left)
                        left_word = s[left:left + L]
                        seen[left_word] -= 1
                        left += L
                        count -= 1
                else:
                    seen.clear()
                    count = 0
                    left = right + L

        return ans
