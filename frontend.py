import tkinter
from tkinter import *
import backend


def get_selected_row(event):
    global selected_row
    index = list.curselection()[0]
    selected_row = list.get(index)

    e1.delete(0,END)
    e1.insert(END,selected_row[1])
    e2.delete(0, END)
    e2.insert(END, selected_row[2])
    e3.delete(0, END)
    e3.insert(END, selected_row[3])
    e4.delete(0, END)
    e4.insert(END, selected_row[4])
    e5.delete(0, END)
    e5.insert(END, selected_row[5])
    e6.delete(0, END)
    e6.insert(END, selected_row[6])



def view_command():
    list.delete(0,END)
    for row in backend.view():
        list.insert(END,row)

def search_command():
    list.delete(0,END)
    for row in backend.search(datetext.get(), earningstext.get(), exercisetext.get(), studytext.get(), diettext.get(), pythontext.get()):
        list.insert(END, row)

def add_command():
    list.delete(0, END)
    backend.insert(datetext.get(), earningstext.get(), exercisetext.get(), studytext.get(), diettext.get(), pythontext.get())
    list.insert(END, (datetext.get(), earningstext.get(), exercisetext.get(), studytext.get(), diettext.get(), pythontext.get()))
    datetext.set(''),earningstext.set(''),datetext.set(''),exercisetext.set(''), studytext.set(''), diettext.set(''),pythontext.set('')

def delete_command():
    backend.delete(selected_row[0])


win = Tk()
win.wm_title('Database project')
win.geometry("700x300")




l1=Label(win, text='Date')
l1.grid(row=0, column=0)
l2=Label(win, text='Exercise')
l2.grid(row=1, column=0)
l3=Label(win, text='Diet')
l3.grid(row=2, column=0)
l4=Label(win, text='Study')
l4.grid(row=0, column=2)
l5=Label(win, text='Python')
l5.grid(row=1, column=2)
l6=Label(win, text='Earnings')
l6.grid(row=2, column=2)



datetext=StringVar()
e1=Entry(win,textvariable=datetext)
e1.grid(row=0, column=1)

exercisetext=StringVar()
e2=Entry(win,textvariable=exercisetext)
e2.grid(row=1, column=1)

diettext=StringVar()
e3=Entry(win,textvariable=diettext)
e3.grid(row=2, column=1)

studytext=StringVar()
e4=Entry(win,textvariable=studytext)
e4.grid(row=0, column=3)

pythontext=StringVar()
e5=Entry(win,textvariable=pythontext)
e5.grid(row=1, column=3)

earningstext=StringVar()
e6=Entry(win,textvariable=earningstext)
e6.grid(row=2, column=3)

b1=Button(win, text='add', width=16, pady=5 ,command=add_command )
b1.grid(row=4, column=3)
b2=Button(win, text='search',width=16, pady=5, command=search_command)
b2.grid(row=5, column=3)
b3=Button(win, text='delete date',width=16, pady=5, command=delete_command)
b3.grid(row=6, column=3)
b4=Button(win, text='view all',width=16, pady=5, command=view_command)
b4.grid(row=7, column=3)
b5=Button(win, text='close',width=16, pady=5,  command=win.destroy)
b5.grid(row=8, column=3)

scrollbar=Scrollbar(win)
scrollbar.grid(row=3 , column=0, rowspan=8)


list=Listbox(win, yscrollcommand=scrollbar.set)
list.grid(row=3 , column=1, rowspan=8)

list.bind('<<ListboxSelect>>', get_selected_row)

win.mainloop()