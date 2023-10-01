class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def validateRow():
            nonlocal board
            for row in board:
                dict = {"1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0, "9":0}
                for element in row:
                    if element == ".":
                        continue
                    else:
                        if dict[element] != 0:
                            return False
                        dict[element] += 1
            return True
        
        def validateCol():
            nonlocal board
            for j in range(9):
                dict = {"1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0, "9":0}
                for i in range(9):
                    if board[i][j] == ".":
                        continue
                    else:
                        if dict[board[i][j]] != 0:
                            return False
                        dict[board[i][j]] += 1
            return True
        
        def validate3by3():
            nonlocal board
            for s_row in range(3):
                for s_col in range(3):
                    dict = {"1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0, "9":0}
                    for i in range(3):
                        for j in range(3):
                            if board[s_row*3 + i][s_col*3 + j] == ".":
                                continue
                            else:
                                if dict[board[s_row*3 + i][s_col*3 + j]] != 0:
                                    return False
                                dict[board[s_row*3 + i][s_col*3 + j]] += 1
            return True
        # print(validateRow(), validateCol(), validate3by3())
        return validateRow() and validateCol() and validate3by3()