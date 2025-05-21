import tkinter

#https://docs.python.org/3/library/tkinter.html

window = tkinter.Tk()
window.title(" " * 45 + "Hello World!") #Hacky way to center it. :-P
window.minsize(400, 200)

#Label
my_label = tkinter.Label(text="Look! A Label!", font=("Arial", 15, "bold"))
my_label.pack(side="top") #defaults to top-center if none selected.

my_label["text"] = "Look! A NEW label!"
my_label.config(text="Look! A NEW NEW label!")

#Button
button = tkinter.Button(window, text="Click Me!", command=window.destroy)

#=Always put window.mainloop() at bottom
window.mainloop()