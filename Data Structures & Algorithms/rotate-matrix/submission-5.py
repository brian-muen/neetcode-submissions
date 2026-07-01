class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        m = len(matrix)

        for i in range(m // 2):
            for j in range(i, m - i - 1):
                temp = matrix[i][j]
                matrix[i][j] = matrix[m-1-j][i]
                matrix[m-1-j][i] = matrix[m-1-i][m-1-j]
                matrix[m-1-i][m-1-j] = matrix[j][m-1-i]
                matrix[j][m-1-i] = temp
        return 
        