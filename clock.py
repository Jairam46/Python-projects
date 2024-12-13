from time import *
from tkinter import*

def update():
    current_time=strftime('%I:%M:%S %p')
    time_label.config(text=current_time)
    current_day=strftime('%A')
    day_label.config(text=current_day)
    current_date=strftime('%B %D,%Y')
    date_label.config(text=current_date)
    window.after(1000,update)
    


window=Tk()

time_label=Label(window,font=('Arial',50),fg='red',bg='black')
time_label.pack()
day_label=Label(window,font=('Arial',25))
day_label.pack()
date_label=Label(window,font=('Arial',25))
date_label.pack()

update()


window.mainloop()