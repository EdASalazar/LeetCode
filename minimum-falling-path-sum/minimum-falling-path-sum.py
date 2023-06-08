class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)

        for i in reversed(range(n - 1)):
            for j in range(n):
                left = inf if j == 0 else matrix[i+1][j-1]
                right = inf if j == n-1 else matrix[i+1][j+1]
                down = matrix[i+1][j]

                matrix[i][j]+= min(left, right, down)

        return min(matrix[0])