class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1
        
        if obstacleGrid[m - 1][n - 1] == 1:
            return 0
        
        for row in range(m):
            for col in range(n):
                if row > 0 and obstacleGrid[row -1][col] < 1:
                    dp[row][col] += dp[row -1][col]
                if col > 0 and obstacleGrid[row][col -1] < 1:
                    dp[row][col] += dp[row][col -1]
                    
        return dp[m - 1][n - 1]
        