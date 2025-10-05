class Solution:
    def minimumTotal(self, triangle):
        # Start from the second to last row, move upward
        for row in range(len(triangle) - 2, -1, -1):
            for col in range(len(triangle[row])):
                # Each cell becomes the sum of itself and the min of the two below it
                triangle[row][col] += min(triangle[row + 1][col], triangle[row + 1][col + 1])
        # Top element now contains the minimum total path sum
        return triangle[0][0]
