from tkinter import Tk, Label, Button, Entry, Frame, Text

window = Tk()
window.title("Tkinter Sample Window")
window.geometry("300x300")

greetings = Label(text="Hello User", fg="black", bg="white")
greetings.pack()

button = Button(text="Click me", bg="black", fg="white")
button.pack()

entry = Entry(fg="yellow", bg="blue", width=50)
entry.pack()

frame = Frame(master=window, borderwidth=5)
frame.pack()

label = Label(master=frame, text="Sample Frame")
label.pack()

textbox = Text(fg="green", bg="yellow", height=5, width=40)
textbox.pack()

window.mainloop()
