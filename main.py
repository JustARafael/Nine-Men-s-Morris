from tkinter import *
from tkinter import messagebox
from random import randint

program=Tk()
program.title("9 Men's Morris")
program.resizable(width=False, height=False)

class parameter:
    def __init__(self):
        self.whoseturn = 0 # 1: x, 2: v
        self.xpp = 0
        self.xap = 9
        self.vpp = 0
        self.vap = 9
        self.move = []
        self.move_check = []
        self.remove = []
        self.select = -1
        self.ai = 0 # 0: Player vs. Player
                    # 1: Player vs. Machine
        self.aiturn = 0
        self.state = -1 # 0: add
                        # 1: select
                        # 2: move
                        # 3: remove

global current_parameter
current_parameter = parameter()

def reset_gui():
    for widget in program.winfo_children():
        widget.grid_remove()

def start_interface():
    reset_gui()
    button1a.grid(row=6, column=1)
    button1d.grid(row=6, column=4)
    button1g.grid(row=6, column=7)
    button2b.grid(row=5, column=2)
    button2d.grid(row=5, column=4)
    button2f.grid(row=5, column=6)
    button3c.grid(row=4, column=3)
    button3d.grid(row=4, column=4)
    button3e.grid(row=4, column=5)    
    button4a.grid(row=3, column=1)
    button4b.grid(row=3, column=2)
    button4c.grid(row=3, column=3)
    button4e.grid(row=3, column=5)
    button4f.grid(row=3, column=6)
    button4g.grid(row=3, column=7)
    button5c.grid(row=2, column=3)
    button5d.grid(row=2, column=4)
    button5e.grid(row=2, column=5)
    button6b.grid(row=1, column=2)
    button6d.grid(row=1, column=4)
    button6f.grid(row=1, column=6)
    button7a.grid(row=0, column=1)
    button7d.grid(row=0, column=4)
    button7g.grid(row=0, column=7)
    coord_1.grid(row=6, column=0)
    coord_2.grid(row=5, column=0)
    coord_3.grid(row=4, column=0)
    coord_4.grid(row=3, column=0)
    coord_5.grid(row=2, column=0)
    coord_6.grid(row=1, column=0)
    coord_7.grid(row=0, column=0)
    coord_a.grid(row=7, column=1)
    coord_b.grid(row=7, column=2)
    coord_c.grid(row=7, column=3)
    coord_d.grid(row=7, column=4)
    coord_e.grid(row=7, column=5)
    coord_f.grid(row=7, column=6)
    coord_g.grid(row=7, column=7)
    state_frame.grid(row=0, column=8, rowspan=8)
    legend_frame.grid(row=8, column=0, columnspan=8)

def start_game():
    if randint(1,10)%2 == 0:
        current_parameter.whoseturn = 1 # x
        current_parameter.aiturn = 1
        turn_image.config(image=x_image)
        for e in button_list:
            e.config(image=xb_image)
    else:
        current_parameter.whoseturn = 2 # v
        current_parameter.aiturn = 2
        turn_image.config(image=v_image)
        for e in button_list:
            e.config(image=vb_image)
    current_parameter.state = 0
    state_check()

def op(state, index):
    if state == 0 and place(current_parameter.whoseturn, index):
        if not board_check():
            turn_change()
        board_change()
        state_check()
    if state == 3:
        if remove_turn(index):
            turn_change()
            board_change()
            state_check()
    if state == 1 and select_turn(index):
        state_check()
    if state == 2 and move_turn(index, current_parameter.select):
        if not board_check():
            turn_change()
        board_change()
        state_check()
    if current_parameter.xpp == 2 and current_parameter.xap == 0:
        messagebox.showinfo("", "Green Win")
        reset()
        return
    if current_parameter.vpp == 2 and current_parameter.vap == 0:
        messagebox.showinfo("", "Red Win")
        reset()
        return
    if move_check(1):
        messagebox.showinfo("", "Green Win")
        reset()
        return
    if move_check(2):
        messagebox.showinfo("", "Red Win")
        reset()
        return

def reset():
    current_parameter.xpp = 0
    current_parameter.vpp = 0
    current_parameter.xap = 9
    current_parameter.vap = 9
    current_parameter.move = []
    current_parameter.remove = []
    current_parameter.move_check = []
    current_parameter.select = -1
    current_parameter.ai = 0
    current_parameter.aiturn = 0
    i=0
    while i<len(button_state_list):
        button_checked_list[i]=0
        button_state_list[i]=0
        i+=1
    start_game()      

def select_turn(index):
    if button_state_list[index] != current_parameter.whoseturn or not select_check(index, 0):
        messagebox.showwarning("", "Cannot select this")
        return False
    else:
        current_parameter.state = 2
        current_parameter.select = index
        return True

def move_check(num):
    move_index = []
    i=0
    for e in button_state_list:
        if e == num:
            move_index.append(i)
        i+=1
    if move_index == []:
        return False
    for e in move_index:
        select_check(e, 1)
    if current_parameter.move_check == []:
        return True
    else:
        current_parameter.move_check = []
        return False

def select_check(index, num ):
    if (current_parameter.whoseturn == 1 and current_parameter.xpp == 3) or\
        (current_parameter.whoseturn == 2 and current_parameter.vpp == 3):
        i=0
        for e in button_state_list:
            if e == 0:
                if num == 0:
                    current_parameter.move.append(i)
                else:
                    current_parameter.move_check.append(i)
            i+=1
        return True
    else:
        for e in select_check_list2:
            if index == e[0] and (button_state_list[e[1]] == 0 or button_state_list[e[2]] == 0):
                if button_state_list[e[1]] == 0:
                    if num == 0:
                        current_parameter.move.append(e[1])
                    else:
                        current_parameter.move_check.append(e[1])
                if button_state_list[e[2]] == 0:
                    if num == 0:
                        current_parameter.move.append(e[2]) 
                    else:
                        current_parameter.move_check.append(e[2]) 
                return True
        for e in select_check_list3:
            if index == e[0] and (button_state_list[e[1]] == 0 or button_state_list[e[2]] == 0 or button_state_list[e[3]] == 0):
                if button_state_list[e[1]] == 0:
                    if num == 0:
                        current_parameter.move.append(e[1])
                    else:
                        current_parameter.move_check.append(e[1])
                if button_state_list[e[2]] == 0:
                    if num == 0:
                        current_parameter.move.append(e[2])
                    else:
                        current_parameter.move_check.append(e[2])
                if button_state_list[e[3]] == 0:
                    if num == 0:
                        current_parameter.move.append(e[3])
                    else:
                        current_parameter.move_check.append(e[3]) 
                return True
        for e in select_check_list4:
            if index == e[0] and (button_state_list[e[1]] == 0 or button_state_list[e[2]] == 0 or button_state_list[e[3]] == 0 or button_state_list[e[4]] == 0):
                if button_state_list[e[1]] == 0:
                    if num == 0:
                        current_parameter.move.append(e[1])
                    else:
                        current_parameter.move_check.append(e[1])
                if button_state_list[e[2]] == 0:
                    if num == 0:
                        current_parameter.move.append(e[2])
                    else:
                        current_parameter.move_check.append(e[2])
                if button_state_list[e[3]] == 0:
                    if num == 0:
                        current_parameter.move.append(e[3])
                    else:
                        current_parameter.move_check.append(e[3]) 
                if button_state_list[e[4]] == 0:
                    if num == 0:
                        current_parameter.move.append(e[4])
                    else:
                        current_parameter.move_check.append(e[4]) 
                return True
    return False

def move_turn(new, old):
    if button_state_list[new] == 0 and (new in current_parameter.move):
        button_state_list[old] = 0
        button_checked_list[old] = 0
        button_state_list[new] = current_parameter.whoseturn
        current_parameter.move = []
        if current_parameter.whoseturn == 1:
            button_list[old].config(image=xb_image)
            button_list[new].config(image=x_image)
        if current_parameter.whoseturn == 2:
            button_list[old].config(image=vb_image)
            button_list[new].config(image=v_image)
        return True
    else:
        messagebox.showwarning("", "Cannot move to here")
        return False

def remove_check(index):
    if button_checked_list[index] == 0:
        current_parameter.remove = list(range(24))
    else:
        i=0
        current_parameter.remove = []
        for e in button_state_list:
            if e != current_parameter.whoseturn and e != 0:
                current_parameter.remove.append(i)
            i+=1
        for e in index_check_list:
            if button_state_list[e[0]] == button_state_list[e[1]] and\
            button_state_list[e[0]] == button_state_list[e[2]] and\
            button_state_list[e[1]] == button_state_list[e[2]] and\
            button_state_list[e[0]] != 0:
                try:
                    current_parameter.remove.remove(e[0])
                except ValueError:
                    pass            
                try:
                    current_parameter.remove.remove(e[1])
                except ValueError:
                    pass           
                try:
                    current_parameter.remove.remove(e[2])
                except ValueError:
                    pass
        if current_parameter.remove == []:
            current_parameter.remove = list(range(24))

def remove_turn(index):
    remove_check(index)
    if button_state_list[index] == 0 or current_parameter.whoseturn == button_state_list[index] or\
    (index not in current_parameter.remove):
        messagebox.showwarning("", "Cannot be removed")
        return False
    else:
        button_state_list[index] = 0
        button_checked_list[index] = 0
        current_parameter.state = 0
        if current_parameter.whoseturn == 1:
            button_list[index].config(image=xb_image)
            current_parameter.vpp -= 1
        if current_parameter.whoseturn == 2:
            button_list[index].config(image=vb_image)
            current_parameter.xpp -= 1
        return True

def turn_change():
    if current_parameter.whoseturn == 1:
        if current_parameter.vap == 0:
            current_parameter.state = 1
        current_parameter.whoseturn = 2
        turn_image.config(image=v_image)
        return
    if current_parameter.whoseturn == 2:
        if current_parameter.xap == 0:
            current_parameter.state = 1
        current_parameter.whoseturn = 1
        turn_image.config(image=x_image)
        return

def board_change():
    i=0
    for e in button_list:
        if button_state_list[i] == 0 and current_parameter.whoseturn == 1:
            e.config(image=xb_image)
        if button_state_list[i] == 0 and current_parameter.whoseturn == 2:
            e.config(image=vb_image)
        i+=1

def state_check():
    if current_parameter.state == 0:
        action_image.config(image=a_image)
    if current_parameter.state == 1:
        action_image.config(image=s_image)
    if current_parameter.state == 2:
        action_image.config(image=m_image)
    if current_parameter.state == 3:
        action_image.config(image=r_image)

def place(player, index):
    if player == 1 and button_state_list[index] == 0:
        button_list[index].config(image=x_image)
        button_state_list[index] = player
        if current_parameter.xap>0:
            current_parameter.xap-=1
            current_parameter.xpp+=1
        return True
    if player == 2 and button_state_list[index] == 0:
        button_list[index].config(image=v_image)
        button_state_list[index] = player
        if current_parameter.vap>0:
            current_parameter.vap-=1
            current_parameter.vpp+=1
        return True

def board_check():
    for e in index_check_list:
        if button_state_list[e[0]] == button_state_list[e[1]] and\
            button_state_list[e[0]] == button_state_list[e[2]] and\
            button_state_list[e[1]] == button_state_list[e[2]] and\
            button_state_list[e[0]] != 0 and\
            (button_checked_list[e[0]] == 0 or\
            button_checked_list[e[1]] == 0 or\
            button_checked_list[e[2]] == 0):
            button_checked_list[e[0]] = 1
            button_checked_list[e[1]] = 1
            button_checked_list[e[2]] = 1
            current_parameter.state = 3
            return True
    return False

def mode_selection():
    pvp_mode.grid(row=0, column=0)
    pvc_mode.grid(row=0, column=1)

def pvp():
    start_interface()
    start_game()

def pvm():
    current_parameter.ai = 1

pvp_mode = Button(text="Player vs. Player", command=pvp)
pvc_mode = Button(text="Player vs. Machine", command=None)
v_image = PhotoImage(file="images/v.gif").subsample(2,2)
x_image = PhotoImage(file="images/x.gif").subsample(2,2)
vb_image = PhotoImage(file="images/vb.gif").subsample(2,2)
xb_image = PhotoImage(file="images/xb.gif").subsample(2,2)
a_image = PhotoImage(file="images/a.gif").subsample(2,2)
r_image = PhotoImage(file="images/r.gif").subsample(2,2)
s_image = PhotoImage(file="images/s.gif").subsample(2,2)
m_image = PhotoImage(file="images/m.gif").subsample(2,2)
legend_frame = Frame(program)
a_action_frame = Frame(legend_frame)
a_action_label = Label(a_action_frame, text="Add")
a_action_image = Label(a_action_frame, image=a_image)
a_action_label.pack(side="top")
a_action_image.pack(side="top")
r_action_frame = Frame(legend_frame)
r_action_label = Label(r_action_frame, text="Remove")
r_action_image = Label(r_action_frame, image=r_image)
r_action_label.pack(side="top")
r_action_image.pack(side="top")
s_action_frame = Frame(legend_frame)
s_action_label = Label(s_action_frame, text="Select")
s_action_image = Label(s_action_frame, image=s_image)
s_action_label.pack(side="top")
s_action_image.pack(side="top")
m_action_frame = Frame(legend_frame)
m_action_label = Label(m_action_frame, text="Move")
m_action_image = Label(m_action_frame, image=m_image)
m_action_label.pack(side="top")
m_action_image.pack(side="top")
a_action_frame.pack(side="left")
r_action_frame.pack(side="left")
s_action_frame.pack(side="left")
m_action_frame.pack(side="left")
state_frame = Frame(program)
turn_frame = Frame(state_frame)
turn_label = Label(turn_frame, text="Whose Turn")
turn_image = Label(turn_frame, image=None)
action_frame = Frame(state_frame)
action_label = Label(action_frame, text="Turn Action")
action_image = Label(action_frame, image=None)
action_label.pack(side="top")
action_image.pack(side="top")
turn_label.pack(side="top")
turn_image.pack(side="top")
turn_frame.pack(side="top")
action_frame.pack(side="top")
button1a = Button(image=None, command=lambda: op(current_parameter.state, 0))
button1d = Button(image=None, command=lambda: op(current_parameter.state, 1))
button1g = Button(image=None, command=lambda: op(current_parameter.state, 2))
button2b = Button(image=None, command=lambda: op(current_parameter.state, 3))
button2d = Button(image=None, command=lambda: op(current_parameter.state, 4))
button2f = Button(image=None, command=lambda: op(current_parameter.state, 5))
button3c = Button(image=None, command=lambda: op(current_parameter.state, 6))
button3d = Button(image=None, command=lambda: op(current_parameter.state, 7))
button3e = Button(image=None, command=lambda: op(current_parameter.state, 8))
button4a = Button(image=None, command=lambda: op(current_parameter.state, 9))
button4b = Button(image=None, command=lambda: op(current_parameter.state, 10))
button4c = Button(image=None, command=lambda: op(current_parameter.state, 11))
button4e = Button(image=None, command=lambda: op(current_parameter.state, 12))
button4f = Button(image=None, command=lambda: op(current_parameter.state, 13))
button4g = Button(image=None, command=lambda: op(current_parameter.state, 14))
button5c = Button(image=None, command=lambda: op(current_parameter.state, 15))
button5d = Button(image=None, command=lambda: op(current_parameter.state, 16))
button5e = Button(image=None, command=lambda: op(current_parameter.state, 17))
button6b = Button(image=None, command=lambda: op(current_parameter.state, 18))
button6d = Button(image=None, command=lambda: op(current_parameter.state, 19))
button6f = Button(image=None, command=lambda: op(current_parameter.state, 20))
button7a = Button(image=None, command=lambda: op(current_parameter.state, 21))
button7d = Button(image=None, command=lambda: op(current_parameter.state, 22))
button7g = Button(image=None, command=lambda: op(current_parameter.state, 23))
button_list = [button1a, button1d, button1g,
                button2b, button2d, button2f,
                button3c, button3d, button3e,
                button4a, button4b, button4c,
                button4e, button4f, button4g,
                button5c, button5d, button5e,
                button6b, button6d, button6f,
                button7a, button7d, button7g]
coord_1 = Label(text="1")
coord_2 = Label(text="2")
coord_3 = Label(text="3")
coord_4 = Label(text="4")
coord_5 = Label(text="5")
coord_6 = Label(text="6")
coord_7 = Label(text="7")
coord_a = Label(text="a")
coord_b = Label(text="b")
coord_c = Label(text="c")
coord_d = Label(text="d")
coord_e = Label(text="e")
coord_f = Label(text="f")
coord_g = Label(text="g")
button_state_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
button_checked_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
index_check_list = [[0,1,2], [3,4,5], [6,7,8], [9,10,11], [12,13,14], 
                        [15,16,17], [18,19,20], [21,22,23], [0,9,21],
                        [3,10,18], [6,11,15], [16,19,22], [1,4,7], [8,12,17],
                        [5,13,20], [2,14,23]]
select_check_list2 = [[0,1,9], [2,1,14], [3,4,10], [5,4,13], [6,7,11], [8,7,12],
                    [15,11,16], [17,12,16], [18,10,19], [20,13,19], [21,9,22],
                    [23,14,22]]
select_check_list3 = [[1,0,2,4], [7,4,6,8], [9,0,10,21], [11,6,10,15], [12,8,13,17],
                    [14,2,13,23], [16,15,17,19], [19,16,18,22], [22,19,21,23]]
select_check_list4 = [[4,1,3,5,7], [10,3,9,11,18], [13,5,12,14,20], [19,16,18,20,22]]

mode_selection()
program.mainloop()