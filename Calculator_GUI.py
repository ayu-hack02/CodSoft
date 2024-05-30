import math
import tkinter as tk

def on_click(event):
    current_text = entry.get()
    text = event.widget.cget("text")

    if text == "=":
        try:
            if "√" in current_text:
                num = float(current_text.replace("√", ""))
                result = math.sqrt(num)
                entry.delete(0, tk.END)
                entry.insert(tk.END, str(result))
            elif "^" in current_text:
                num = current_text.replace("^", "**")
                result = eval(num)
                entry.delete(0, tk.END)
                entry.insert(tk.END, str(result))
            elif "ln" in current_text:
                num = float(current_text.replace("ln", ""))
                result = math.log(num)
                entry.delete(0, tk.END)
                entry.insert(tk.END, str(result))
            else:
                result = eval(current_text)
                entry.delete(0, tk.END)
                entry.insert(tk.END, str(result))    
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    elif text == "D":
        entry.delete(len(current_text)-1, tk.END)
    else:
        entry.insert(tk.END, text)

def create_button(text, row, col, col_span=1):
    button = tk.Button(root, text=text, font=("Helvetica", 20), bd=5)
    button.grid(row=row, column=col, columnspan=col_span, padx=5, pady=5)
    button.bind("<Button-1>", on_click)  # Bind the button click event to the on_click() function
    return button

root = tk.Tk()
root.title("Calculator")
root.geometry("800x900")


heading_label = tk.Label(root, text="Calculator", font=("Helvetica", 16, "bold"),highlightcolor=("red"))
heading_label.grid(row=0, column=0, columnspan=4, pady=20)

entry = tk.Entry(root, font=("Helvetica", 24), bd=5, justify=tk.RIGHT)
entry.grid(row=1, column=0, columnspan=5, padx=10, pady=10)


create_button("7", 2, 0)
create_button("8", 2, 1)
create_button("9", 2, 2)
create_button("/", 2, 3)
create_button("^", 2, 4)

create_button("4", 3, 0)
create_button("5", 3, 1)
create_button("6", 3, 2)
create_button("*", 3, 3)
create_button("√", 3, 4)

create_button("1", 4, 0)
create_button("2", 4, 1)
create_button("3", 4, 2)
create_button("-", 4, 3)
create_button("ln", 4, 4)

create_button("0", 5, 0)
create_button(".", 5, 1)
create_button("=", 5, 2)
create_button("+", 5, 3)
create_button("%", 5, 4)

create_button("D", 6, 0, 2)
create_button("C", 6, 1, 3)

root.mainloop()