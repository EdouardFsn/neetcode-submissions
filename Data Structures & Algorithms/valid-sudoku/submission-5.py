class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for i in range(9):
            for j in range(9):
                case = board[i][j]
                if case in seen:
                    return False
                else: 
                    if (case !="."):
                        seen.add(case)
            seen = set()
        for j in range(9):
            for i in range(9):
                case = board[i][j]
                if case in seen:
                    return False
                else: 
                    if (case !="."):
                        seen.add(case)
            seen = set() 
        for j in range(9):
            for i in range(9):
                if (j % 3 == 0 ) and (i % 3 == 0 ):
                    for k in range(3):
                        for l in range(3):
                            case = board[k+j][l+i]
                            if case in seen:
                                return False
                            else: 
                                if (case !="."):
                                    seen.add(case)
                    seen = set() 
        return True


                

            


        