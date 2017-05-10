from random import randint

def select(board, ai, pp):
    aip = []
    i = 0
    for e in board:
        if e == ai:
            aip.append(i)
        i+=1
    ans = []
    for e in aip:
        if selectcheck(board, e, pp):
            ans.append(e)
    selectm = selectmill(board, ai, ans)
    selectc = selectchoice(board, ai, ans)
    selects = selectstop(board, ai)
    temp = []
    for e in ans:
        pos = mp(board, e)
        temp.append([e, pos[randint(0,len(pos)-1)]])
    ans = temp
    if len(selectm) != 0:
        return selectm[0]
    elif len(selectc) != 0:
        return selectc[0]
    else:
        return ans[randint(0,len(ans)-1)]

def swap(v1, v2):
    return v2, v1

def selectstop(board, ai):
    pass

def selectmill(board, ai, ans):
    res = []
    for e in ans:
        for f in mp(board, e):
            num = nummillcheck(board, ai)
            board[e], board[f] = swap(board[e], board[f])
            if millcheck(board, ai, num):
                res.append([e, f])
            board[e], board[f] = swap(board[e], board[f])
    return res

def nummillcheck(board, ai):
    num = 0
    for e in index_check_list:
        if board[e[0]] == ai and board[e[1]] == ai and board[e[2]] == ai:
            num+=1
    return num

def millcheck(board, ai, num):
    temp = 0
    for e in index_check_list:
        if board[e[0]] == ai and board[e[1]] == ai and board[e[2]] == ai:
            temp += 1
    if temp>num:
        return True
    return False

def selectchoice(board, ai, ans):
    res = []
    for e in ans:
        for f in index_check_list:
            if (e in f) and (board[f[0]] == ai) and (board[f[1]] ==  ai) and (board[f[2]] == ai):
                pos = mp(board, e)
                res.append([e, pos[randint(0,len(pos)-1)]])
    return res       
    
def mp(board, index):
    ans = []
    for e in select_check_list2:
        if index == e[0] and (board[e[1]] == 0 or board[e[2]] == 0):
            if board[e[1]] == 0:
                ans.append(e[1])
            if board[e[2]] == 0:
                ans.append(e[2]) 
    for e in select_check_list3:
        if index == e[0] and (board[e[1]] == 0 or board[e[2]] == 0 or board[e[3]] == 0):
            if board[e[1]] == 0:
                ans.append(e[1])
            if board[e[2]] == 0:
                ans.append(e[2])
            if board[e[3]] == 0:
                ans.append(e[3])
    for e in select_check_list4:
        if index == e[0] and (board[e[1]] == 0 or board[e[2]] == 0 or board[e[3]] == 0 or board[e[4]] == 0):
            if board[e[1]] == 0:
                ans.append(e[1])
            if board[e[2]] == 0:
                ans.append(e[2])
            if board[e[3]] == 0:
                ans.append(e[3]) 
            if board[e[4]] == 0:
                ans.append(e[4]) 
    return ans

def selectcheck(board, index, pp):
    if pp == 3:
        return True
    else:
        for e in select_check_list2:
            if index == e[0] and (board[e[1]] == 0 or board[e[2]] == 0):
                return True
        for e in select_check_list3:
            if index == e[0] and (board[e[1]] == 0 or board[e[2]] == 0 or board[e[3]] == 0):
                return True
        for e in select_check_list4:
            if index == e[0] and (board[e[1]] == 0 or board[e[2]] == 0 or board[e[3]] == 0 or board[e[4]] == 0):
                return True
    return False

def remove(board, ai):
    am = removecheck(board, ai)
    r21 = remove21(board, ai)
    r11 = remove11(board, ai)
    if len(r21) != 0:
        return r21[0]
    elif len(r11) != 0:
        return r11[0]
    else:
        return am[0]

def remove11(board, ai):
    ans = []
    for e in index_check_list:
        if board[e[0]] == 0 or board[e[1]] == 0 or board[e[2]] == 0:
            cur1 = 0
            if board[e[0]] == ai:
                cur1+=1
            if board[e[1]] == ai:
                cur1+=1
            if board[e[2]] == ai:
                cur1+=1
            cur2 = 0
            if board[e[0]] != ai and board[e[0]] != 0:
                cur2+=1
            if board[e[1]] != ai and board[e[1]] != 0:
                cur2+=1
            if board[e[2]] != ai and board[e[2]] != 0:
                cur2+=1
            if cur1 == cur2:
                if board[e[0]] != ai and board[e[0]] != 0:
                    ans.append(e[0])
                if board[e[1]] != ai and board[e[1]] !=0:
                    ans.append(e[1])
                if board[e[2]] != ai and board[e[2]] !=0:
                    ans.append(e[2])
    return ans

def remove21(board, ai):
    ans = []
    for e in index_check_list:
        if board[e[0]] != 0 and board[e[1]] != 0 and board[e[2]] != 0:
            cur = 0
            if board[e[0]] == ai:
                cur +=1
            if board[e[1]] == ai:
                cur+=1
            if board[e[2]] == ai:
                cur+=1
            if cur == 2:
                if board[e[0]] != ai:
                    ans.append(e[0])
                if board[e[1]] != ai:
                    ans.append(e[1])
                if board[e[2]] != ai:
                    ans.append(e[2])
    return ans

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
    if len(form) != 0:
        return form[0]
    elif len(stop) != 0:
        return stop[0]
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
select_check_list2 = [[0,1,9], [2,1,14], [3,4,10], [5,4,13], [6,7,11], [8,7,12], 
                    [15,11,16], [17,12,16], [18,10,19], [20,13,19], [21,9,22],
                    [23,14,22]]
select_check_list3 = [[1,0,2,4], [7,4,6,8], [9,0,10,21], [11,6,10,15], [12,8,13,17],
                    [14,2,13,23], [16,15,17,19], [19,16,18,22], [22,19,21,23]]
select_check_list4 = [[4,1,3,5,7], [10,3,9,11,18], [13,5,12,14,20], [19,16,18,20,22]]