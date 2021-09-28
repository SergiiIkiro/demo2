from tkinter import *
window = Tk()
window.title("Calculator")
entry1 = Entry(window, width=60, borderwidth=10, bg="light green")
entry1.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def addButton(num):
    return Button(window, padx=20, bd=8, fg="blue", text=num, width=5, command=lambda: clickButton(str(num)))
def createButton():
    btton0 = addButton(0)
    btton1 = addButton(1)
    btton2 = addButton(2)
    btton3 = addButton(3)
    btton4 = addButton(4)
    btton5 = addButton(5)
    btton6 = addButton(6)
    btton7 = addButton(7)
    btton8 = addButton(8)
    btton9 = addButton(9)

    btton_add = addButton('+')
    btton_sub = addButton('-')
    btton_mult = addButton('*')
    btton_div = addButton('/')
    btton_clear = addButton('C')
    btton_equal = addButton('=')

    row1 = [btton7, btton8, btton9, btton_add]
    row2 = [btton4, btton5, btton6, btton_sub]
    row3 = [btton1, btton2, btton3, btton_mult]
    row4 = [btton_clear, btton0, btton_equal, btton_div]

    r = 1
    for row in [row1, row2, row3, row4]:
        c = 0
        for btton in row:
            btton.grid(row=r, column=c, columnspan=1)
            c += 1
        r += 1
def clickButton(value):
    current_eq = str(entry1.get())

    if value == 'C':
       entry1.delete(-1, END)
    elif value == '=':
       answer = str(eval(current_eq))
       entry1.delete(-1, END)
       entry1.insert(0, answer)
    else:
        entry1.delete(0, END)
        entry1.insert(0, current_eq+value)


createButton()
window.mainloop()
