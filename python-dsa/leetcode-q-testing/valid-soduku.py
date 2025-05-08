input= [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]


def validSodukuP(input):
    for i in range(9):
        seen = set()
        for j in range(9):
            checkVal = input[i][j]
            if checkVal in seen:
                return False
            if checkVal != ".":
                seen.add(checkVal)
    for j in range(9):
        seen = set()
        for i in range(9):
            checkVal = input[i][j]
            if checkVal in seen:
                return False
            if checkVal != ".":
                seen.add(checkVal)
    

    

validSodukuP(input)