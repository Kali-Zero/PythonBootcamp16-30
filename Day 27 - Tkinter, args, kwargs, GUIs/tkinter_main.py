#Alternate way to call tkinter, which may be better
# if using more than one module from the library
from tkinter import *

#https://docs.python.org/3/library/tkinter.html

window = Tk()
window.title(" " * 45 + "Hello World!") #Hacky way to center it. :-P
window.minsize(500, 300)
window.config(padx=20, pady=20) #Adds padding!

#Items MUST have .pack(), .place(), or .grid() attached, or they will not show up!
#.pack() Centers things along one of the four sides of the window
#.place(x=0,y=0) Specifies exactly where the item is to go on the window
#.grid() Divides the window into rows and columns (starts a 0,0 in the top left corner)
#=====Note: Only one type per program (pack, place, or grid)

#Label
my_label = Label(text="Look! A Label!", font=("Arial", 15, "bold"))
#my_label.pack(side="top") #defaults to top-center if none selected.
my_label.grid(column=0, row=0)

#my_label["text"] = "Look! A NEW label!"
#my_label.config(text="Look! A NEW NEW label!")

def button_clicked():
    #my_label.config(text="Button was clicked!")
    my_label.config(text=input_box.get()) #Grabs the text from the textbox and puts it into the label

#Buttons
#button = Button(window, text="Click Me!", command=window.destroy) #closes window
button1 = Button(window, text="Click Me!", command=button_clicked)
button1.grid(column=1, row=1)

button2 = Button(window, text="Close!", command=window.destroy)
button2.grid(column=3, row=0)

#Entry (Text Input)
input_box = Entry(width=20)
#input_box.pack()
input_box.grid(column=4, row=3)
input_box.get() #Returns input as a string

#=Always put window.mainloop() at bottom
window.mainloop()

#===============================================================================================