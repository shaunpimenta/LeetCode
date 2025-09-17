#Brute force solution taking O(n^2) time and O(n) space
#Check each row, column and 3x3 subgrid for duplicates

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols=set()
        squares=set()
        for row in board:
            rows=set()
            for i in row:
                if i in rows:
                    return False
                elif i==".":
                    pass
                else:
                    rows.add(i)

        # for col in board:
        #     cols=set()
        #     for i in col:
        #         if i in cols:
        #             return False
        #         elif i==".":
        #             pass
        #         else:
        #             cols.add(i)
        for i in range(9):
            tt=[]
            for t in range(9):
                tt+=board[t][i]
                tt=[i for i in tt if i!="."]
                if len(tt)!=len(set(tt)):
                    return False
        t=1
        for i in range(0,9,3):
            for t in range(1,4):
                t=board[i][(t-1)*3:t*3]+board[i+1][(t-1)*3:t*3]+board[i+2][(t-1)*3:t*3]
                # print(board[i+2:t*3],t,i)
                # t+=board[i+2:t*3]
                # t+=board[i+1:t*3]
                print(t)
                t=[i for i in t if i!="."]
                if len(set(t))==len(t):
                    pass
                else:
                    print("Here",t)
                    return False
        return True
