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
drawpad.grid(row=0, column=1)
item = drawpad.create_oval(10, 50, 100, 100, fill='green')
# A checkbox widget
box = Checkbutton(root, text="Check here.")
box.grid(row=0, column=0)


# An editor widget
editor = Text(width=30, height=4)
editor.grid(row=2, column=1, rowspan=2, sticky=SE)

# A button. This widget is demonstrating using an event handler with 
# the command argument
times_pressed = 0
def pressed():
    roll1 = rollNsidedDie(6)
    drawpad.create_text(roll1, fill='green')
    editor.insert(END, roll1)
    editor.see(END)
    
   '''
    global times_pressed
    times_pressed = times_pressed + 1
    editor.insert(END, times_pressed)
    editor.see(END)
    '''
    
button = Button(root, text='Click me.', 
                command=pressed)
button.grid(row=1, column=0)

'''    
num_dice = raw_input("How many dice do you want to row? ")
num_side = raw_input("How many sided dices do you want to roll? ")

for i in range(int(num_dice)):
    print "Roll " + str(i)
    roll1 = rollNsidedDie(int(num_side))
    roll2 = rollNsidedDie(int(num_side))
    

    
    print "roll1 = " + str(roll1)
    print "roll2 = " + str(roll2)
    
    print "cp " + str(roll1*roll2)
    ''' 
root.mainloop()