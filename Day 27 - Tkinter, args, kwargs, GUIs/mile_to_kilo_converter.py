from tkinter import *

window = Tk()
window.title(" " * 10 + "Miles to Kilometers Converter") #Hacky way to center it.
window.minsize(300, 100)
window.config(padx=20, pady=20)

kilometers = 0.0

my_label1 = Label(text="Miles", font=("Arial", 12, "bold"))
my_label1.grid(column=3, row=0)

input_box = Entry(width=10)
input_box.grid(column=1, row=0)
input_box.get()

my_label2 = Label(text="is equal to", font=("Arial", 12, "bold"))
my_label2.grid(column=0, row=1)

my_label3 = Label(text=kilometers, font=("Arial", 15, "bold"))
my_label3.grid(column=1, row=1)

my_label4 = Label(text="kilometers", font=("Arial", 12, "bold"))
my_label4.grid(column=3, row=1)

def button_clicked():
    #"{:.2f}".format keeps the decimal to two places.
    my_label3.config(text="{:.2f}".format(1.60934 * float(input_box.get())))

button1 = Button(window, text="Calculate", command=button_clicked)
button1.grid(column=1, row=2)

window.mainloop()