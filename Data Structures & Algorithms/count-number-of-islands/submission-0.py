class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
         
        rows, cols = len(grid), len(grid[0])
        res = 0
        
        def dfs(row, col):
            if (row < 0 or col < 0 or row >= rows or col >= cols or grid[row][col] == "0"):
                return
        
            grid[row][col] = "0"
            for dy, dx in directions:
                dfs(row + dy, col + dx)
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    dfs(row, col)
                    res += 1

        return res            