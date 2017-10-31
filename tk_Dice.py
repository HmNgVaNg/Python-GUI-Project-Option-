'''
Tkinter_tutorial.py demonstrates some of the standard widgets  
and the grid() geometry manager
'''
from Tkinter import *
import random as rnd
def rollNsidedDie(N):
    number = rnd.randint(1,N)
    return number
root = Tk()

# A canvas widget
drawpad = Canvas(root, background='brown')
drawpad.grid(row=0, column=0)

def pressed():
    roll1 = rollNsidedDie(6)
    drawpad.create_text(rnd.randint(1,300),rnd.randint(1,300), text = str(roll1), fill='black',font="Helvetica 26 bold")
    #drawpad.create_text(0,50, text = 'tgytvhrfv', fill='black',font="Helvetica 26 bold underline")
    editor.insert(END, roll1)
    editor.see(END)
    
    

    
    
button = Button(root, text='Click me.', 
                command=pressed)
button.grid(row=1, column=0)


root.mainloop()