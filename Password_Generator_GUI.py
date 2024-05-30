import tkinter as tk
from tkinter import messagebox
import random
import string

generated_password = None
length = None

def pas():
    global generated_password
    l = int(length.get())
    if l < 6:
        messagebox.showwarning("Warning!"," Password length is short")
        return 
    
    ch = (string.digits + string.ascii_letters + string.punctuation)
    p = "".join(random.choice(ch) for _ in range (l))
    generated_password.delete(0,tk.END)
    generated_password.insert(tk.END, p)

def reset_f():
    global generated_password, length
    generated_password.delete(0, tk.END)
    length.delete(0, tk.END)
    
def main():  
    global length, generated_password
    w = tk.Tk()
    w.title("Password Generator")
    w.geometry("400x500")

    head_label = tk.Label(w, text="Password Generator", font=("Helvetica", 20, "bold"))
    head_label.grid(row=0, column=0, columnspan= 5, pady=25)

    label_l = tk.Label(w, text="Enter Password Length: ")
    label_l.grid(row=1, column=0, sticky=tk.E)

    length = tk.Entry(w, width=40)
    length.grid(row=1, column=1)
    
    label_p = tk.Label(w, text="Generated password: ")
    label_p.grid(row=2, column=0, sticky=tk.E)

    generated_password = tk.Entry(w, width= 40)
    generated_password.grid(row=2, column=1, columnspan=2)

    button_pas = tk.Button(w, text = "Generate Password", command = pas)
    button_pas.grid(row=3, column=0, padx=5, pady=10)

    button_reset_f = tk.Button(w, text = "Reset", command = reset_f)
    button_reset_f.grid(row=3, column=1, padx=5, pady=10)

    w.mainloop()

if __name__ == "__main__":
    main()

    