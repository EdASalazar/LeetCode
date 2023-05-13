class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        ans = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    ans = max(ans, self.dfs(grid, i, j))
        return ans
    
    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != 1:
            return 0
        print(i, j)

        ans = 1
        grid[i][j] = "x"
        ans += self.dfs(grid, i, j +1)
        ans += self.dfs(grid, i +1, j)
        ans += self.dfs(grid, i, j -1)
        ans += self.dfs(grid, i -1, j)
            
            
        return ans



        