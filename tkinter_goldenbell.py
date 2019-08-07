from tkinter import Tk, Label, Button, Entry
from goldenbell_pptx import making_PPT

root = Tk()
root.title("골든벨 문제 만들기")
root.geometry("900x600+100+100")
label = Label(root, text = '문제와 정답을 입력하세요.', font=("HY헤드라인M", 15), width=30, height=2, relief='solid', bg='white')
label.grid(row=0, column=0)


q_a_list = []

tx = Label(root, text='문           제', font=('HY헤드라인M', 15), width=50, height=2, relief='groove')
tx.grid(row=1, column=0)
tx = Label(root, text='정           답', font=('HY헤드라인M', 15), width=20, height=2, relief='groove')
tx.grid(row=1, column=1)
q_ent = Entry(root, font=('HY헤드라인M', 15), width=50, relief='groove')
q_ent.grid(row=2, column=0)
a_ent = Entry(root, font=('HY헤드라인M', 15), width=20, relief='groove')
a_ent.grid(row=2, column=1)
q_a_list.append([q_ent, a_ent])
count = 2


def make_line():
    global count, q_a_list
    count += 1
    print(count)
    q_ent = Entry(root, font=('HY헤드라인M', 15), width=50, relief='groove')
    q_ent.grid(row=count, column=0)
    a_ent = Entry(root, font=('HY헤드라인M', 15), width=20, relief='groove')
    a_ent.grid(row=count, column=1)
    q_a_list.append([q_ent, a_ent])


def delete_line():
    global count, q_a_list
    count -= 1
    print(count)
    print(q_a_list)
    if len(q_a_list) > 1:
        q_ent, a_ent = q_a_list.pop(-1)
        print(q_ent, a_ent)
        q_ent.grid_forget()
        a_ent.grid_forget()

def goto_PPT():
    global q_a_list
    q_a_li = [[q.get(), a.get()] for q, a in q_a_list]
    making_PPT(q_a_li)



button = Button(root, text='+', overrelief="solid", width=2, height=1, command=make_line, repeatdelay=1000, repeatinterval=100)
button.grid(row=1, column=2)
button = Button(root, text='-', overrelief="solid", width=2, height=1, command=delete_line, repeatdelay=1000, repeatinterval=100)
button.grid(row=2, column=2)
button = Button(root, text='PPT만들기',font=("HY헤드라인M", 15), command=goto_PPT, overrelief="solid", width=15, height=2, repeatdelay=1000, repeatinterval=100)
button.grid(row=0, column=1, columnspan=2)



root.mainloop()
