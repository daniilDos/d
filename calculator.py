from tkinter import *

root = Tk()

def click_handler(event=None):
    assert type(event) == int
    current = entry_field.get()
    entry_field.delete(0, END)
    entry_field.insert(0, str(current) + str(event))
    
    
   
   
root.title('Simpel Calculator 2000')
def click_event():
    pass

entry_field = Entry(root, width=40, borderwidth=5)
entry_field.grid(row=0, column=0,columnspan=3,padx=10,pady=10)

button_1 = Button(root, text='1', padx=40, pady=20, command=lambda: click_handler(1))
button_2 = Button(root, text='2', padx=40, pady=20, command=click_event)
button_3 = Button(root, text='3', padx=40, pady=20, command=click_event)
button_4 = Button(root, text='4', padx=40, pady=20, command=click_event)
button_5 = Button(root, text='5', padx=40, pady=20, command=click_event)
button_6 = Button(root, text='6', padx=40, pady=20, command=click_event)
button_7 = Button(root, text='7', padx=40, pady=20, command=click_event)
button_8 = Button(root, text='8', padx=40, pady=20, command=click_event)
button_9 = Button(root, text='9', padx=40, pady=20, command=click_event)
button_0 = Button(root, text='0', padx=40, pady=20, command=click_event)

button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)

button_equal = Button(root, text='=', padx=90, pady=20, command=click_event)
button_add = Button(root, text='+', padx=90, pady=20, command=click_event)
button_clear = Button(root, text='Clear', padx=80, pady=20, command=click_event)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)



root.mainloop()
