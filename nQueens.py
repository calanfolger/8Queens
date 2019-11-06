import random

global N 
N = 8
  
def printSolution(board): 
    for i in range(N): 
        for j in range(N): 
            print (board[i][j], end = " ") 
        print() 

def isSafe(board, row, col): 
  
    # Check this row on left side 
    for i in range(col): 
        if board[row][i] == 1:
            # print("ROW COLLISION")
            return False
  
    # Check upper diagonal on left side 
    for i, j in zip(range(row, -1, -1),  
                    range(col, -1, -1)): 
        if board[i][j] == 1:
            # print("UPPER DIAG COLLISION")
            return False
  
    # Check lower diagonal on left side 
    for i, j in zip(range(row, N, 1),  
                    range(col, -1, -1)): 
        if board[i][j] == 1:
            # print("LOWER DIAG COLLISION") 
            return False
    return True

def placeRandK(board, col, K):
    
    if (K > 0):
        if (col <= K):
            row = random.randint(0,7)
            board[row][col] = 1
            # print()
            # printSolution(board)
            # print()
            return placeRandK(board, col + 1, K)
        else:
            col = col - 1
            for i in range(N):
                if board[i][col] == 1:
                    board[i][col] = 0
                    if isSafe(board, i, col) == False:
                        return False
                    else:
                        board[i][col] = 1
                        if (col == 0):
                            return True
                        col = col - 1
                        continue                
            
            if (K == 7):
                print("THIS IS WHAT IT THINKS THE SOLUTION IS: \n")
                printSolution(board)
                print()
                return True
        col = K + 1
        return solveNQUtil(board, col)
    
    elif (K == 0):
        return solveNQUtil(board, col)
  
def solveNQUtil(board, col):

        if col >= N:
            return True
        
        # Consider this column and try placing 
        # THE REST of the queens in all rows one by one 
        for i in range(N):

            # print()
            # printSolution(board)
            # print()    
            if isSafe(board, i, col):

                # Place this queen in board[i][col] 
                board[i][col] = 1
    
                # recur to place rest of the queens 
                if solveNQUtil(board, col + 1) == True: 
                    return True
    
                # If placing queen in board[i][col 
                # doesn't lead to a solution, then remove
                # queen from board[i][col] 
                board[i][col] = 0
    
        # if the queen can not be placed in any row in 
        # this colum col then return false 
        return False
  
def main(): 
    board = [ [0, 0, 0, 0, 0, 0, 0, 0], 
              [0, 0, 0, 0, 0, 0, 0, 0], 
              [0, 0, 0, 0, 0, 0, 0, 0], 
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0], 
              [0, 0, 0, 0, 0, 0, 0, 0], 
              [0, 0, 0, 0, 0, 0, 0, 0], 
              [0, 0, 0, 0, 0, 0, 0, 0] ] 

    K = 7
    print ("K = "+ str(K))
    
    while placeRandK(board, 0, K) == False:
        board = [ [0, 0, 0, 0, 0, 0, 0, 0], 
                  [0, 0, 0, 0, 0, 0, 0, 0], 
                  [0, 0, 0, 0, 0, 0, 0, 0], 
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0], 
                  [0, 0, 0, 0, 0, 0, 0, 0], 
                  [0, 0, 0, 0, 0, 0, 0, 0], 
                  [0, 0, 0, 0, 0, 0, 0, 0] ] 
    print ("Solution exists!")
    printSolution(board)
  
# Driver Code 
if __name__== "__main__":
    main()