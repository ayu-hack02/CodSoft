import tkinter as tk
from tkinter import *
from tkinter import messagebox, simpledialog

def add_task():
    global lt, et 
    task = et.get()
    if task:
        lt.insert(tk.END, task)
        et.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning!", "Please enter a task.")

def del_task():
    global lt
    try:
        selectedItemIndex = lt.curselection()[0]
        lt.delete(selectedItemIndex)
    except IndexError:
        messagebox.showwarning("Warning!", "Please select a task to delete.")

def edit_task():
    global lt
    try:
        index = lt.curselection()[0]
        old = lt.get(index)
        new = simpledialog.askstring("Edit Task","Edit the task selected: ", initialvalue = old)
        if new:
            lt.delete(index)
            lt.insert(index,new)
    except IndexError:
        messagebox.showwarning("Warning!", "Please select a task to edit.")    

def mark():
    marked = lt.curselection()
    temp = marked[0]
    temp_mark = lt.get(marked)
    temp_mark += "✔"  
    lt.delete(temp)
    lt.insert(temp,temp_mark)


w = Tk()
w.title("To-Do list")
w.geometry("400x500")


ft = Frame(w)
ft.pack()

lt = Listbox(ft, bg = "azure2", fg= "black", height= 10, font="Helvetica")
lt.pack(side=LEFT)

st = Scrollbar(ft)
st.pack(side = RIGHT, fill = Y)
lt.config(yscrollcommand = st.set)
st.config(command = lt.yview)

et = tk.Entry(w, width = 50)
et.pack(pady=10)

entry_button=Button(w,text="Add task",width=50,command=add_task)
entry_button.pack(pady=3)

edit_button=Button(w,text="Edit task",width=50,command=edit_task)
edit_button.pack(pady=3)

delete_button=Button(w,text="Delete selected task",width=50,command=del_task)
delete_button.pack(pady=3)

mark_button=Button(w,text="Mark as completed ",width=50,command=mark)
mark_button.pack(pady=3)

w.mainloop()