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
                print(t)
                t=[i for i in t if i!="."]
                if len(set(t))==len(t):
                    pass
                else:
                    print("Here",t)
                    return False
        return True


        #Little Optimized using Hashsets
        for row in board:
            rows={}
            for i in row:
                if i in rows:
                    return False
                elif i==".":
                    pass
                else:
                    rows[i]=1
        for i in range(9):
            tt=[]
            cols={}
            for t in range(9):
                if board[t][i] in cols:
                    return False
                elif board[t][i]==".":
                    pass
                else:
                    cols[board[t][i]]=1
        for i in range(0,9,3):
            for t in range(1,4):
                tt=board[i][(t-1)*3:t*3]+board[i+1][(t-1)*3:t*3]+board[i+2][(t-1)*3:t*3]
                squares={}
                print(t)
                for j in tt:
                    if j in squares:
                        print(squares,j)
                        return False
                    elif j==".":
                        pass
                    else:
                        squares[j]=1
        return True
