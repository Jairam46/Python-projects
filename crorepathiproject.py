from tkinter import*
import time

questions=['1) What is the pH value of the human body?',
           '2) Which of the following are called "Key Industrial animals"?',
           '3) Elections to panchayats in state are regulated by',
           '4) Which of the following Himalayan regions is called "Shivaliks"?',
           '5) Forming of Association in India is',
           '6) The Samkhya School of Philosophy was founded by',
           '7) Pustaz grasslands are situated at?',
           '8) Right to emergency medical aid is a'
           ]

options=(('A: 9.2 to 9.8','B: 7.0 to 7.8','C: 6.1 to 6.3','D: 5.4 to 5.6'),
         ('A: Producers','B:Tertiary consumers','C: Primary consumers','D: None of these'),
         ('A:Gram panchayat','B:Nagar Nigam','C:Election Commission of India','D:State Election Commission'),
         ('A:Upper Himalayas','B:Lower Himalayas','C:Outer Himalayas','D:nner Himalayas'),
         ('A:Legal Right','B:Illegal Right','C:Natural Right','D:Fundamental Right'),
         ("A:Gautam Buddha","B:Mahipala","C:Gopala","D:Kapila"),
         ('A:South Africa','B:China','C:Hungary','D:USA'),
         ('A:Legal Right','B:Illegal Right','C:Constitutional Right','D:Fundamental Right'))

answers=['b','c','d','c','d','d','c','d']
answer=''
ammount=['1000','3000','8000','10000','20000','40000','50000','70000']


def start():
    global i
    question_label.config(text=questions[i])
    ammount_label.config(text=f'question for {ammount[i]} rupees..')
    optionA.config(text=options[i][0])
    optionB.config(text=options[i][1])
    optionC.config(text=options[i][2])
    optionD.config(text=options[i][3])
    # i +=1


def ans(v):
    global x
    global i
    global answer   
    answer= answer+str(v)
    x.set(answer)
    option=x.get()
    print(option)
    
    if option[i]==answers[i]:
        i +=1
        

        start()
        
    else:
        question_label.config(text='WRONG ANSWER')
        ammount_label.config(text=f'you will take {ammount[i]} rupees to home')
        optionA.config(text='')
        optionB.config(text='')
        optionC.config(text='')
        optionD.config(text='')
        fail +=1
    x.set('')

    # window.update_idletasks()
    
    

window=Tk()
window.geometry('900x500')
window.configure(bg='#141c2b')
window.resizable(False,False)

x=StringVar()
i=0




frame=LabelFrame(window,width=800,height=800,bd=6,bg='#3c324a')
frame.place(relx=0.5,rely=0.5,anchor='center')
# for widget in frame:
#     widget.config(padx=4,pady=4)

# for widget in frame:
#     widget.pack(padx=10,pady=10)

question_label=Label(frame,width=40,text='question here',font=('Arial',20,'bold'),bd=6,bg='#b1b9c7',fg='black',padx=4,pady=4)
question_label.grid(row=0,column=0,columnspan=3)

ammount_label=Label(window,text='hello',width=20,font=('Arial',20,'bold'))
ammount_label.pack()

optionA=Button(frame,text='option a here',width=25,height=2,bg='#b1b9c7',command=lambda: ans('a'),padx=4,pady=4)
optionA.grid(row=3,column=0,sticky='new')
optionC=Button(frame,width=25,text='option c here',height=2,bg='#b1b9c7',command=lambda: ans('c'),padx=4,pady=4)
optionC.grid(row=5,column=0,sticky='new')


optionB=Button(frame,text='option B here',width=25,height=2,bg='#b1b9c7',command=lambda: ans('b'),padx=4,pady=4)
optionB.grid(row=3,column=1,sticky='new',columnspan=2)
optionD=Button(frame,text='option D here',width=25,height=2,bg='#b1b9c7',command=lambda: ans('d'),padx=4,pady=4)
optionD.grid(row=5,column=1,sticky='new',columnspan=2)



start()





window.mainloop()
