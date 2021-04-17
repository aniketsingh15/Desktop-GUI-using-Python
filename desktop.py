from tkinter import *
import os
import webbrowser
root= Tk()

root.title('Desktop')
root.iconbitmap('Desktop.ico')
# Adjust size 
root.geometry("750x470")

bg = PhotoImage(file= "background_750x550.png")

#creating canvas
my_canvas = Canvas(root, width=750, height=550)
my_canvas.pack(fill='both', expand= True)

#set image in canvas
my_canvas.create_image(0,0, image=bg, anchor='nw')

#adding buttons

#creating google chrome
new = 1
url = "https://www.google.com"

def openweb():
    webbrowser.open(url,new=new)

chrome_btn = PhotoImage(file='chrome.png')
img_label = Label(image=chrome_btn)
button = Button(root, text='Google Chrome', image=chrome_btn,command=openweb, borderwidth=0)
button.pack()

button_window= my_canvas.create_window(10, 10, anchor='nw', window=button)

#creating calculator

def calc():
    os.system('python calculator.py')
calculator_btn = PhotoImage(file='calculator.png')
img_label = Label(image=calculator_btn)
button2 = Button(root, text='Google Chrome', image=calculator_btn, borderwidth=0, command=calc)
button2.pack()

button2_window= my_canvas.create_window(10, 110, anchor='nw', window=button2)

#creating paint
def paint():
    os.system('python paint.py')
paint_btn = PhotoImage(file='paint.png')
img_label = Label(image=paint_btn)
button3 = Button(root, text='Google Chrome', image=paint_btn, borderwidth=0,command=paint)
button3.pack()

button3_window= my_canvas.create_window(10, 210, anchor='nw', window=button3)

#creating notepad

def open():
    os.system('cmd /c notepad')
notepad_btn = PhotoImage(file='notepad.png')
img_label = Label(image=notepad_btn)
button4 = Button(root, text='Google Chrome', image=notepad_btn, borderwidth=0, command=open)
button4.pack()

button4_window= my_canvas.create_window(10, 310, anchor='nw', window=button4)

#creating start

start_btn = PhotoImage(file='start.png')
img_label = Label(image=start_btn)
button4 = Button(root, text='Google Chrome', image=start_btn, borderwidth=0)
button4.pack()

button4_window= my_canvas.create_window(10, 410, anchor='nw', window=button4)


#creating recycle_bin

recycle_bin_btn = PhotoImage(file='recycle_bin.png')
img_label = Label(image=recycle_bin_btn)
button5 = Button(root, text='Google Chrome', image=recycle_bin_btn, borderwidth=0)
button5.pack()

button5_window= my_canvas.create_window(110, 10, anchor='nw', window=button5)


#creating computer

computer_btn = PhotoImage(file='computer.png')
img_label = Label(image=computer_btn)
button6 = Button(root, text='Google Chrome', image=computer_btn, borderwidth=0)
button6.pack()

button6_window= my_canvas.create_window(110, 110, anchor='nw', window=button6)


#creating input

e = Entry(root, width= 70)
e.pack(fill=X, ipadx=8, pady=10, padx=10)

e_window= my_canvas.create_window(70, 420, anchor='nw', window=e)


root.mainloop()

