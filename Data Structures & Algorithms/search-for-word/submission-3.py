class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        ROWS, COLS = len(board), len(board[0])
        visited = [[False] * COLS for _ in range(ROWS)]
        
        def dfs(x, y, position):
            if position == len(word):
                return True
            if (x < 0 or y < 0 or x >= ROWS or y >= COLS or
                word[position] != board[x][y] or visited[x][y]):
                return False
            visited[x][y] = True
            res = (dfs(x + 1, y, position + 1) or
                   dfs(x - 1, y, position + 1) or
                   dfs(x, y + 1, position + 1) or
                   dfs(x, y - 1, position + 1))
            visited[x][y] = False
            return res

            


        for x in range(ROWS):
            for y in range(COLS):
                if dfs(x, y, 0):
                    return True
        return False
        