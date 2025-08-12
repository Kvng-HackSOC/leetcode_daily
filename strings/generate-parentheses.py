# backtracking/generate-parentheses.py

class Solution:
    def generateParenthesis(self, n):
        res = []
        def backtrack(open_count, close_count, path):
            # If we've used n open and n close parentheses, we have a valid combo
            if open_count == n and close_count == n:
                res.append("".join(path))
                return

            # We can add an open parenthesis if we haven't used n yet
            if open_count < n:
                path.append("(")
                backtrack(open_count + 1, close_count, path)
                path.pop()

            # We can add a close parenthesis only if there are more opens used than closes
            if close_count < open_count:
                path.append(")")
                backtrack(open_count, close_count + 1, path)
                path.pop()

        backtrack(0, 0, [])
        return res

# Quick test
if __name__ == "__main__":
    print(Solution().generateParenthesis(3))
    # Expected output (order may vary):
    # ["((()))", "(()())", "(())()", "()(())", "()()()"]
