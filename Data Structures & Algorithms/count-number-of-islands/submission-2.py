class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        rows, cols = len(grid), len(grid[0])
        islands = 0

        for row in range(rows):
            for col in range(cols): 
                if grid[row][col] == "0":
                    continue
                
                grid[row][col] = "0"
                islands += 1
                stack = [(row, col)]

                while stack:
                    r, c = stack.pop()

                    for dy, dx in directions:
                        nr, nc = r + dy, c + dx
                        if (0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1"):   
                            grid[nr][nc] = "0"
                            stack.append((nr, nc))

        return islands
