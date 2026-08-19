class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        path, res = [], []

        vert = [0] * n
        diag1 = [0] * (2 * n - 1)
        diag2 = diag1.copy()

        def backtrack(row):
            if row == n:
                res.append(path.copy())
                return
            for col in range(n):
                if vert[col] or diag1[row + col] or diag2[row - col + n - 1]:
                    continue
                vert[col] = diag1[row + col] = diag2[row - col + n - 1] = 1
                path.append(self.buildString(col, n))
                backtrack(row + 1)
                vert[col] = diag1[row + col] = diag2[row - col + n - 1] = 0
                path.pop()

        backtrack(0)
        
        return res

    def buildString(self, i, n):
        s = []
        for j in range(n):
            if j == i:
                s.append("Q")
            else:
                s.append(".")

        return "".join(s)

        