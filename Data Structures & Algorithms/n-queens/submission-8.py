class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        path, res = [], []

        vert = [0] * n
        diag1 = [0] * (2 * n - 1)
        diag2 = diag1.copy()

        strings = ["." * col + "Q" + "." * (n - col - 1) for col in range(n)] 

        def backtrack(row):
            if row == n:
                res.append(path.copy())
                return
            for col in range(n):
                d1 = row + col
                d2 = row - col + n - 1
                if vert[col] or diag1[d1] or diag2[d2]:
                    continue
                vert[col] = diag1[d1] = diag2[d2] = 1
                path.append(strings[col])
                backtrack(row + 1)
                vert[col] = diag1[d1] = diag2[d2] = 0
                path.pop()

        backtrack(0)
        
        return res