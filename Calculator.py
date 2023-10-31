from tkinter import *

def button_click(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, current + str(number))

def clear():
    entry.delete(0, END)

def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, END)
        entry.insert(0, result)
    except:
        entry.delete(0, END)
        entry.insert(0, "Error")

root = Tk()
root.title("CodersCave Python Internship")

entry = Entry(root, width=20, font=('Arial', 20))
entry.grid(row=0, column=0, columnspan=4)

button1 = Button(root, text="1", command=lambda: button_click(1), font=('Arial', 16))
button2 = Button(root, text="2", command=lambda: button_click(2), font=('Arial', 16))
button3 = Button(root, text="3", command=lambda: button_click(3), font=('Arial', 16))
button4 = Button(root, text="4", command=lambda: button_click(4), font=('Arial', 16))
button5 = Button(root, text="5", command=lambda: button_click(5), font=('Arial', 16))
button6 = Button(root, text="6", command=lambda: button_click(6), font=('Arial', 16))
button7 = Button(root, text="7", command=lambda: button_click(7), font=('Arial', 16))
button8 = Button(root, text="8", command=lambda: button_click(8), font=('Arial', 16))
button9 = Button(root, text="9", command=lambda: button_click(9), font=('Arial', 16))
button0 = Button(root, text="0", command=lambda: button_click(0), font=('Arial', 16))

button_clear = Button(root, text="C", command=clear, font=('Arial', 16))
button_add = Button(root, text="+", command=lambda: button_click("+"), font=('Arial', 16))
button_subtract = Button(root, text="-", command=lambda: button_click("-"), font=('Arial', 16))
button_multiply = Button(root, text="*", command=lambda: button_click("*"), font=('Arial', 16))
button_divide = Button(root, text="/", command=lambda: button_click("/"), font=('Arial', 16))
button_equal = Button(root, text="=", command=calculate, font=('Arial', 16))

button1.grid(row=1, column=0)
button2.grid(row=1, column=1)
button3.grid(row=1, column=2)
button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
button7.grid(row=3, column=0)
button8.grid(row=3, column=1)
button9.grid(row=3, column=2)
button0.grid(row=4, column=1)

button_clear.grid(row=4, column=0)
button_add.grid(row=1, column=3)
button_subtract.grid(row=2, column=3)
button_multiply.grid(row=3, column=3)
button_divide.grid(row=4, column=3)
button_equal.grid(row=4, column=2)

root.mainloop()
