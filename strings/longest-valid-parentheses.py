# strings/longest-valid-parentheses.py

class Solution:
    def longestValidParentheses(self, s):
        stack = [-1]  # base index for length calculation
        max_len = 0
        
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)  # push index of '('
            else:
                stack.pop()  # pop last '(' index
                if not stack:
                    stack.append(i)  # reset base if stack empty
                else:
                    max_len = max(max_len, i - stack[-1])
        
        return max_len
