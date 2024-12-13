from tkinter import*

window=Tk()
window.geometry('400x400')
window.resizable(False,False)
window.configure(bg='#535c59')
window.title('CALCULATOR')

equation=""

def clear():
    global equation
    equation=''
    label.config(text='')

def backspace():
    # global equation
    # equation=equation.delete(len(equation)-1,END)
    # label.config(text=equation)
    pass
def result():
    resultt=''
    global equation
    try:
        resultt=eval(equation)
        label.config(text=resultt)
    except ZeroDivisionError:
        print('zero canot be devided')
    except:
        print('something went wrong............')
    
   

def show(value):
    global equation 
    equation += value
    label.config(text=equation)


label=Label(window,text='',font=('Arial',25,'bold'),width=30,height=2)
label.pack()


button1=Button(window,text='C',width=8,height=3,bd=2,bg='#00e1ff',command=lambda : clear(),activebackground='#00e1ff')
button1.place(x=7,y= 85)
button2=Button(window,text='+',width=8,height=3,bd=2,bg='#ff00d9',command=lambda:show('+'),activebackground='#ff00d9')
button2.place(x=80,y= 85)
button3=Button(window,text='-',width=8,height=3,bg='#ff00d9',command=lambda:show('-'),activebackground='#ff00d9')
button3.place(x=160,y= 85)


button4=Button(window,text='backspace',width=20,height=3,bg='#ff00d9',activebackground='black',command=backspace)
button4.place(x=240,y= 85)
buttonmod=Button(window,text='%',width=20,height=3,bg='#ff00d9',activebackground='black',command=lambda:show('%'))
buttonmod.place(x=240,y= 150)
buttondiv=Button(window,text='/',width=20,height=3,bg='#ff00d9',activebackground='black',command=lambda:show('/'))
buttondiv.place(x=240,y= 210)
buttonmul=Button(window,text='*',width=20,height=3,bg='#ff00d9',activebackground='black',command=lambda:show('*'))
buttonmul.place(x=240,y= 270)
buttonequal=Button(window,text='=',width=20,height=3,bg='#ff00d9',activebackground='black',command=result)
buttonequal.place(x=240,y= 340)


button5=Button(window,text='1',width=8,height=3,bg='white',activebackground='black',command=lambda:show('1'))
button5.place(x=7,y= 150)
button6=Button(window,text='2',width=8,height=3,bg='white',activebackground='black',command=lambda:show('2'))
button6.place(x=80,y= 150)
button7=Button(window,text='3',width=8,height=3,bg='white',activebackground='black',command=lambda:show('3'))
button7.place(x=160,y= 150)


button8=Button(window,text='4',width=8,height=3,bg='white',activebackground='black',command=lambda:show('4'))
button8.place(x=7,y= 210)
button9=Button(window,text='5',width=8,height=3,bg='white',activebackground='black',command=lambda:show('5'))
button9.place(x=80,y= 210)
button10=Button(window,text='6',width=8,height=3,bg='white',activebackground='black',command=lambda:show('6'))
button10.place(x=160,y= 210)


button11=Button(window,text='7',width=8,height=3,bg='white',activebackground='black',command=lambda:show('7'))
button11.place(x=7,y= 270)
button12=Button(window,text='8',width=8,height=3,bg='white',activebackground='black',command=lambda:show('8'))
button12.place(x=80,y= 270)
button13=Button(window,text='9',width=8,height=3,bg='white',activebackground='black',command=lambda:show('9'))
button13.place(x=160,y= 270)
button14=Button(window,text='0',bg='white',width=30,height=3,command=lambda:show('0'))
button14.place(x=7,y=340)





window.mainloop()

