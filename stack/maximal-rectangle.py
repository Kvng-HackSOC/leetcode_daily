class Solution:
    def maximalRectangle(self, matrix):
        if not matrix or not matrix[0]:
            return 0

        n = len(matrix[0])
        heights = [0] * n
        max_area = 0

        for row in matrix:
            for i in range(n):
                heights[i] = heights[i] + 1 if row[i] == "1" else 0

            # calculate largest rectangle in histogram for this row
            stack = []
            for j, h in enumerate(heights):
                start = j
                while stack and stack[-1][1] > h:
                    index, height = stack.pop()
                    max_area = max(max_area, height * (j - index))
                    start = index
                stack.append((start, h))

            for j, h in stack:
                max_area = max(max_area, h * (n - j))

        return max_area
