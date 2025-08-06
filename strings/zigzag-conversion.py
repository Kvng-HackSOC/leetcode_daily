class Solution:
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s

        rows = ['' for _ in range(numRows)]
        current_row = 0
        direction = 1

        for char in s:
            rows[current_row] += char

            if current_row == 0:
                direction = 1
            elif current_row == numRows - 1:
                direction = -1

            current_row += direction

        return ''.join(rows)

# If you want to test manually:
if __name__ == "__main__":
    sol = Solution()
    print(sol.convert("PAYPALISHIRING", 3))  # PAHNAPLSIIGYIR
