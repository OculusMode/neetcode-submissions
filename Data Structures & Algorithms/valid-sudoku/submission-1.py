class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for x in range(9):
            eles_row = set()
            eles_col = set()
            eles_box = set()
            for y in range(9):
                i = board[x][y]
                j = board[y][x]
                k = board[(x//3)*3 + y//3][(x%3)*3+y%3]
                if i != "." and i in eles_row:
                    return False
                if j != "." and j in eles_col:
                    return False
                if k != "." and k in eles_box:
                    return False
                eles_row.add(i)
                eles_col.add(j)
                eles_box.add(k)
        return True

                