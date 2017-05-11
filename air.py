from random import randint

def remove(board, ai, pp):
    if pp == 0:
        temp = []
        temp = possiblemill(board, ai, 1)
        temp = [x for x in temp if x in removecheck(board, ai)]
        if len(temp) != 0:
            return temp[randint(0,len(temp)-1)]
    am = removecheck(board, ai)
    r21 = remove21(board, ai)
    r11 = remove11(board, ai)
    if len(r21) != 0:
        return r21[randint(0,len(r21)-1)]
    elif len(r11) != 0:
        return r11[randint(0,len(r11)-1)]
    else:
        return am[randint(0,len(am)-1)]

def add(board, ai):
    stop = stopmill(board, ai)
    form = formmill(board, ai, 2)
    preform = formmill(board, ai, 1)
    advance = advancemill(board, ai)
    last = juststop(board, ai)
    if len(form) != 0:
        return form[0]
    elif len(stop) != 0:
        return stop[randint(0,len(stop)-1)]
    elif len(preform) != 0:
        return preform[randint(0,len(preform)-1)]
    elif len(advance) != 0:
        return advance[randint(0,len(advance)-1)]
    elif len(last) != 0:
        return last[randint(0,len(last)-1)]
    else:
        misc = randint(0, 23)
        while board[misc] != 0:
            misc = randint(0, 23)
        return misc

def selectstop(board, ai):
    ans = possiblemill(board, ai, 0)
    return ans

def select(board, ai, pp):
    if pp == 3:
        #temp1 = possiblemill(board, ai, 0)
        temp2 = brutemill(board, ai)
        #if len(temp1) != 0:
        #    return temp1[range(0,randint(len(temp1)-1))]
        #elif len(temp2) != 0:
        if len(temp2) != 0:
            return temp2
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
        pos = mp(board, e, 0)
        if len(pos) != 0:
            temp.append([e, pos[randint(0,len(pos)-1)]])
    ans = temp
    if len(selectm) != 0:
        return selectm[randint(0,len(selectm)-1)]
    elif len(selectc) != 0:
        return selectc[randint(0,len(selectc)-1)]
    else:
        return ans[randint(0,len(ans)-1)]

def brutemill(board, ai):
    ans = []
    i=0
    for e in index_check_list:
        if (board[e[0]] == ai or board[e[0]] == 0) and (board[e[1]] == ai or board[e[1]] == 0) and\
            (board[e[2]] == ai or board[e[2]] == 0):
            cur = 0
            theempty = [e[0], e[1], e[2]]
            ap = []
            i=0
            for z in board:
                if z == ai:
                    ap.append(i)
                i+=1
            if board[e[0]] != 0:
                theempty.remove(e[0])
                try:
                    ap.remove(e[0])
                except ValueError:
                    pass
                cur+=1
            if board[e[1]] != 0:
                theempty.remove(e[1])
                try:
                    ap.remove(e[1])
                except ValueError:
                    pass
                cur+=1
            if board[e[2]] != 0:
                theempty.remove(e[2])
                try:
                    ap.remove(e[2])
                except ValueError:
                    pass
                cur+=1
            if cur == 2:
                return (ap[0], theempty[0])
            else:
                for a,b in zip(ap,theempty):
                    ans.append([a,b])      
    return ans[randint(0,len(ans)-1)]

def swap(v1, v2):
    return v2, v1

def possiblemill(board, ai, m):
    empty21 = []
    theempty = []
    for e in index_check_list:
        if board[e[0]] == 0 or board[e[1]] == 0 or board[e[2]] == 0:
            cur = 0
            if board[e[0]] != ai and board[e[0]] != 0:
                cur +=1
            if board[e[1]] != ai and board[e[1]] != 0:
                cur+=1
            if board[e[2]] != ai and board[e[2]] != 0:
                cur+=1
            if cur == 2:
                temp = []
                if board[e[0]] != 0:
                    temp.append(e[0])
                if board[e[1]] != 0:
                    temp.append(e[1])
                if board[e[2]] != 0:
                    temp.append(e[2])
                empty21.append(temp)
                if board[e[0]] == 0:
                    theempty.append(e[0])
                if board[e[1]] == 0:
                    theempty.append(e[1])
                if board[e[2]] == 0:
                    theempty.append(e[2])
    pos = []
    i=0
    if m == 1:
        for e in theempty:
            if ai == 1:
                temp = mp(board, e, 2)
            else:
                temp = mp(board, e, 1)
            temp3 = [x for x in temp if x not in empty21[i]]
            pos+=temp3
            i+=1
    else:
        return theempty
    return pos

def selectmill(board, ai, ans):
    res = []
    for e in ans:
        for f in mp(board, e, 0):
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
                pos = mp(board, e, 0)
                res.append([e, pos[randint(0,len(pos)-1)]])
    return res       
    
def mp(board, index, t):
    ans = []
    for e in select_check_list2:
        if index == e[0] and (board[e[1]] == t or board[e[2]] == t):
            if board[e[1]] == t:
                ans.append(e[1])
            if board[e[2]] == t:
                ans.append(e[2]) 
    for e in select_check_list3:
        if index == e[0] and (board[e[1]] == t or board[e[2]] == t or board[e[3]] == t):
            if board[e[1]] == t:
                ans.append(e[1])
            if board[e[2]] == t:
                ans.append(e[2])
            if board[e[3]] == t:
                ans.append(e[3])
    for e in select_check_list4:
        if index == e[0] and (board[e[1]] == t or board[e[2]] == t or board[e[3]] == t or board[e[4]] == t):
            if board[e[1]] == t:
                ans.append(e[1])
            if board[e[2]] == t:
                ans.append(e[2])
            if board[e[3]] == t:
                ans.append(e[3]) 
            if board[e[4]] == t:
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
    if len(ans) == 0:
        ans = list(range(24))
    return ans

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