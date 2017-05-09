from random import randint

def remove(board, ai):
    ans = removecheck(board, ai)
    


def removecheck(board, ai):
    ans = list(range(24))
    i = 0
    for e in board:
        if e == ai or e == 0:
            ans.remove(i)
        i+=1
    for e in index_check_list:
        if board[e[0]] == board[e[1]] and\
            board[e[0]] == board[e[2]] and\
            board[e[1]] == board[e[2]] and\
            board[e[0]] != 0 and board[e[0]] != ai:
            try:
                ans.remove(e[0])
            except ValueError:
                pass            
            try:
                ans.remove(e[1])
            except ValueError:
                pass           
            try:
                ans.remove(e[2])
            except ValueError:
                pass
    return ans

def add(board, ai):
    stop = stopmill(board, ai)
    form = formmill(board, ai, 2)
    preform = formmill(board, ai, 1)
    advance = advancemill(board, ai)
    last = juststop(board, ai)
    print(stop)
    print(form)
    print(preform)
    print(advance)
    print(last)
    print("-----------")
    if len(stop) != 0:
        return stop[0]
    elif len(form) != 0:
        return form[0]
    elif len(preform) != 0:
        return preform[0]
    elif len(advance) != 0:
        return advance[0]
    elif len(last) != 0:
        return last[0]
    else:
        misc = randint(0, 23)
        while board[misc] != 0:
            misc = randint(0, 23)
        return misc

def advancemill(board, ai):
    ans = []
    for e in advance_check_list2:
        if ((board[index_check_list[e[0]][0]] == ai) or (board[index_check_list[e[0]][1]] == ai) or\
            (board[index_check_list[e[0]][2]] == ai)) and ((board[index_check_list[e[1]][0]] == ai) or\
            (board[index_check_list[e[1]][1]] == ai) or (board[index_check_list[e[1]][2]] == ai)) and\
            not((board[index_check_list[e[0]][0]] != ai) and (board[index_check_list[e[0]][0]] != 0)) and\
            not((board[index_check_list[e[0]][1]] != ai) and (board[index_check_list[e[0]][1]] != 0)) and\
            not((board[index_check_list[e[0]][2]] != ai) and (board[index_check_list[e[0]][2]] != 0)) and\
            not((board[index_check_list[e[1]][0]] != ai) and (board[index_check_list[e[1]][0]] != 0)) and\
            not((board[index_check_list[e[1]][1]] != ai) and (board[index_check_list[e[1]][1]] != 0)) and\
            not((board[index_check_list[e[1]][2]] != ai) and (board[index_check_list[e[1]][2]] != 0)):
            x = [x for x in index_check_list[e[0]] if x in index_check_list[e[1]]]
            if board[x[0]] == 0:
                ans.append(x[0])
    for e in advance_check_list:
        if not((board[index_check_list[e[0]][0]] != ai and board[index_check_list[e[0]][0]] != 0) or\
            (board[index_check_list[e[0]][1]] != ai and board[index_check_list[e[0]][1]] != 0) or\
            (board[index_check_list[e[0]][2]] != ai and board[index_check_list[e[0]][2]] != 0)) and\
            not((board[index_check_list[e[1]][0]] != ai and board[index_check_list[e[1]][0]] != 0) or\
            (board[index_check_list[e[1]][1]] != ai and board[index_check_list[e[1]][1]] != 0) or\
            (board[index_check_list[e[1]][2]] != ai and board[index_check_list[e[1]][2]] != 0)) and\
            not ((board[index_check_list[e[0]][0]] == 0 and board[index_check_list[e[0]][1]] == 0 and\
            board[index_check_list[e[0]][2]] == 0) or (board[index_check_list[e[1]][0]] == 0 and\
            board[index_check_list[e[1]][1]] == 0 and board[index_check_list[e[1]][2]] == 0)):
            if board[index_check_list[e[0]][1]] == 0:
                ans.append(index_check_list[e[0]][1])
            if board[index_check_list[e[1]][1]] == 0:
                ans.append(index_check_list[e[1]][1])
    return ans

def juststop(board, ai):
    ans = []
    for e in index_check_list:
        cur = 0
        if board[e[0]] != ai:
            cur+=1
        if board[e[1]] != ai:
            cur+=1
        if board[e[2]] != ai:
            cur+=1
        if (board[e[0]] == 0 and board[e[1]] == 0 and board[e[2]] == 0) or\
            (board[e[0]] == ai or board[e[1]] == ai or board[e[2]] == ai):
            cur = 0
        if cur>=1:
            if board[e[0]] == 0:
                ans.append(e[0])
            if board[e[1]] == 0:
                ans.append(e[1])
            if board[e[2]] == 0:
                ans.append(e[2])
        cur = 0
    return ans

def stopmill(board, ai):
    ans = []
    for e in index_check_list:
        cur = 0
        if board[e[0]] != ai and board[e[0]] != 0:
            cur+=1
        if board[e[1]] != ai and board[e[1]] != 0:
            cur+=1
        if board[e[2]] != ai and board[e[2]] != 0:
            cur+=1
        if cur==2:
            if board[e[0]] == 0:
                ans.append(e[0])
            if board[e[1]] == 0:
                ans.append(e[1])
            if board[e[2]] == 0:
                ans.append(e[2])
        cur = 0
    return ans

def formmill(board, ai, weight):
    ans = []
    for e in index_check_list:
        cur = 0
        if board[e[0]] == ai:
            cur+=1
        if board[e[1]] == ai:
            cur+=1
        if board[e[2]] == ai:
            cur+=1
        if (board[e[0]] != ai and board[e[0]] != 0) or (board[e[1]] != ai and board[e[1]] != 0) or\
            (board[e[2]] != ai and board[e[2]] != 0):
            cur=0
        if cur>=weight:
            if board[e[0]] == 0:
                ans.append(e[0])
            if board[e[1]] == 0:
                ans.append(e[1])
            if board[e[2]] == 0:
                ans.append(e[2])
        cur = 0
    return ans

index_check_list = [[0,1,2], [3,4,5], [6,7,8], [9,10,11], [12,13,14], 
                    [15,16,17], [18,19,20], [21,22,23], [0,9,21], 
                    [3,10,18], [6,11,15], [16,19,22], [1,4,7], [8,12,17], 
                    [5,13,20], [2,14,23]]
advance_check_list = [[0, 1], [1, 2], [0, 2], [5, 6], [5, 7], [6, 7], [8, 9], [8, 10], 
                    [9, 10], [13, 14], [13, 15], [14, 15], [0, 12], [1, 12], [2, 12], 
                    [3, 8], [3, 9], [3, 10], [4, 13], [4, 14], [4, 15], [11, 5], [11, 6],
                    [11, 7]]
advance_check_list2 = [[0, 8], [0, 15], [7, 8], [7, 15], [1, 9], [1, 14], [6, 9], [6, 14], 
                        [5, 10], [5, 13], [2, 10], [2, 13]]