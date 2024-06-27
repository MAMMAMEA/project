import tkinter
import random
window=tkinter.Tk()
window.title('PWeator')
window.geometry('380x320+100+100')



def f():
    
    global ent7
    ent7.delete(0, tkinter.END)
    

    



    
    
    aa=int(ent1.get())
    bb=int(ent2.get())
    cc=int(ent3.get())
    
    
    aaa=random.sample(a, aa)
    
    bbb=random.sample(b, bb)
    
    ccc=random.sample(c, cc)
    
    PW=aaa+bbb+ccc

    
    
    PPWW=''.join(PW)

    ent7.insert(0, PPWW)
    
def ff():
    global ent7
    ent7.delete(0, tkinter.END)
    ee=random.sample(d, 4)
    eee=''.join(ee)
    ent7.insert(0, eee)


def fff():
    global ent7
    ent7.delete(0, tkinter.END)
    gg=random.sample(d, 8)
    ggg=''.join(gg)
    ent7.insert(0, ggg)


def ffff():
    global ent7
    ent7.delete(0, tkinter.END)
    hh=random.sample(d, 12)
    hhh=''.join(hh)
    ent7.insert(0, hhh)


    



#리스트 설정
a = ['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k','l','m', 'n', 'o', 'p',
'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
b = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
c = ['@', '*', '!', '#', '$', '-', '%', '&', '(', ')']


d=['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k','l','m', 'n', 'o', 'p',
'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'L', 'M', 'N', 'O',
'P','Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','0', '1', '2', '3', '4',
'5', '6', '7', '8', '9','@', '*', '!', '#', '$', '-', '%', '&', '(', ')']

#입력 칸
ent1=tkinter.Entry(window , width=20)
ent2=tkinter.Entry(window ,width=20)
ent3=tkinter.Entry(window ,width=20)
ent4=tkinter.Entry(window ,width=10)
ent5=tkinter.Entry(window ,width=10)
ent6=tkinter.Entry(window ,width=10)


#라벨 텍스트
l1=tkinter.Label(window, text='몇개의 문자를 사용하시겠습니까?')
l2=tkinter.Label(window, text='몇개의 숫자를 사용하시겠습니까?')
l3=tkinter.Label(window, text='몇개의 특수기호를 사용하시겠습니까?')

#버튼 만들기
b2=tkinter.Button(window, text='4자리', width=10, command=ff)
b3=tkinter.Button(window, text='8자리', width=10, command=fff)
b4=tkinter.Button(window, text='12자리', width=10, command=ffff)



#입력 칸 보이게 하기
ent1.grid(row=1, column=1)
ent2.grid(row=3, column=1)
ent3.grid(row=5, column=1)


#라벨 보이게 하기
l1.grid(row=0, column=1)
l2.grid(row=2, column=1)
l3.grid(row=4,column=1)

#버튼 보이게 하기
b2.place(x=230, y=10)
b3.place(x=230, y=50)
b4.place(x=230, y=90)




#아이디 생성 창
ent7=tkinter.Entry(window,width=30)
ent7.place(x=80, y=210)
#생성 버튼
b1=tkinter.Button(window, text='생성', width=10, command=f)
b1.place(x=140, y=235)


window.mainloop()
