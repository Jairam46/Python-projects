from tkinter import *
from tkinter import ttk
from tkinter import messagebox


def details():
    reg=y.get()
    if reg=='agreed':
    
        name=entry1.get()
        states=state.get()
        titles=combobox.get()

        
        # age=
        # certificates=
        # course=
        # experiance=
        print('name is :',name)
        print('state :',states)
        print('title :',titles)
        print(reg)
        gender=x.get()
        print('gender : male') if gender==1 else print('gender: female')
    else:
        messagebox.showerror(title='ERROR',message='you are not agreed for the terms& conditions')
        


window=Tk()
window.geometry('700x600')
window.title('data entry form')

y=StringVar()
x=IntVar()
frame1=Frame(window)
frame1.pack(padx=10,pady=10)

label_frame=LabelFrame(frame1,text='USER INFO')
label_frame.grid(row=0,column=0,sticky='news')

label2=Label(label_frame,text="enter name")
label2.grid(row=0,column=0)

entry1=Entry(label_frame,)
entry1.grid(row=1,column=0)


title=Label(label_frame,text='title')
title.grid(row=0,column=2)

combobox=ttk.Combobox(label_frame,values=['Mr.','Ms'])
combobox.grid(row=1,column=2)


state_title=Label(label_frame,text='state')
state_title.grid(row=0,column=1)
state=ttk.Combobox(label_frame,values=['karnataka','kerala','tamilnadu'])
state.grid(row=1,column=1)

label3=Label(label_frame,text='age')
label3.grid(row=2,column=0)
spinbox=ttk.Spinbox(label_frame,from_=1,to_=80)
spinbox.grid(row=3,column=0)

rbutton1=Radiobutton(label_frame,text='male',value=1,variable=x)
rbutton1.grid(row=3,column=1)
rbutton2=Radiobutton(label_frame,text='female',value=2,variable=x)
rbutton2.grid(row=3,column=2)

for widget in label_frame.winfo_children():
    widget.grid_configure(padx=10,pady=10)
# ==========================-----------secondframe=======-------------

label_frame2=ttk.LabelFrame(frame1,text='infor')
label_frame2.grid(row=1,column=0,sticky='news')

label11=Label(label_frame2,text='certificates')
label11.grid(row=0,column=0)

certifiacte_spin_box=ttk.Spinbox(label_frame2,from_=0,to_=20)
certifiacte_spin_box.grid(row=1,column=0)

course=Label(label_frame2,text='course done')
course.grid(row=0,column=1)

course_spin=ttk.Combobox(label_frame2,values=["BCA","BSC-CS",'DIPLOMA','BTECH','MCA'])
course_spin.grid(row=1,column=1)

experiance_label=Label(label_frame2,text='you have any experiance')
experiance_label.grid(row=0,column=2)

experiance=ttk.Combobox(label_frame2,values=['yes','no'])
experiance.grid(row=1,column=2)

for widget in label_frame2.winfo_children():
    widget.grid_configure(padx=10,pady=10)


label3_frame=ttk.LabelFrame(frame1)
label3_frame.grid(row=2,column=0,sticky='news')

check=Checkbutton(label3_frame,text='i agree for the terms and condition',
                  onvalue='agreed',offvalue='disagreed',variable=y)
check.grid(row=0,column=0)


button1=Button(frame1,text='SUBMIT',fg='black',activeforeground='black',bg='#07edd6',activebackground='#07edd6',
               command=details)
button1.grid(row=3,column=0,sticky='new',padx=10,pady=10)



window.mainloop()