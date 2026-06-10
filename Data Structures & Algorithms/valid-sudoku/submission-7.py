class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_hash = [set() for _ in range(9)]
        col_hash = [set() for _ in range(9)]
        box_hash = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                item = board[i][j]
                row, col = i//3, j//3
                box_num = 3 * row + col
                if item == ".":
                    continue
                if item not in row_hash[i]:
                    row_hash[i].add(item)
                else: return False
                if item not in col_hash[j]:
                    col_hash[j].add(item)
                else: return False
                if item not in box_hash[box_num]:
                    box_hash[box_num].add(item)
                else: return False

        return True
    
                




        
        
