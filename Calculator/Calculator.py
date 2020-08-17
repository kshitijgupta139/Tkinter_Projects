from tkinter import *


root=Tk()
w = 328
h = 520

ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws / 2) - (w / 2)
y = (hs / 2) - (h / 2)

root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.title("Calculator")
root.config(bg="black")
root.wm_iconbitmap("cal.ico")
root.minsize(328,520)
root.maxsize(328,520)

def click(event):
    global scvalue
    text = event.widget.cget("text")
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())

            except Exception as e:
                print(e)
                value = "Error"


        scvalue.set(value)
        screen.update()

    elif text == "C":
        scvalue.set("")
        screen.update()

    else:
        scvalue.set(scvalue.get() + text)
        screen.update()



def cancel(event):
    global scvalue
    text = screen.get()[:-1]
    screen.delete(0, END)
    screen.insert(0, text)


scvalue=StringVar()
scvalue.set("")


Label(root,text="Calculator by Kshitij Gupta",font="lucida 15 bold",fg="red",bg="black").pack()

screen=Entry(root,textvar=scvalue,font="lucida 30 bold")
screen.pack(padx=10,fill=X,pady=10)

f = Frame(root, bg="black")
b = Button(f, text="9", padx=28, pady=22,  font="lucida 15 bold",bg="grey")
b.pack(side=LEFT)
b.bind("<Button-1>", click)


b = Button(f, text="8", padx=28, pady=22,  font="lucida 15 bold",bg="grey")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="7", padx=28, pady=22,   font="lucida 15 bold",bg="grey")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="6", padx=28, pady=22,  font="lucida 15 bold",bg="grey")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

f.pack()

f = Frame(root, bg="black")
b = Button(f, text="5", padx=28, pady=22,  font="lucida 15 bold",bg="grey")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="4", padx=28, pady=22,  font="lucida 15 bold",bg="grey")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="3", padx=28, pady=22,   font="lucida 15 bold",bg="grey")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="2", padx=28, pady=22,  font="lucida 15 bold",bg="grey")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

f.pack()

f = Frame(root, bg="black")
b = Button(f, text="1", padx=28, pady=22,  font="lucida 15 bold",bg="grey")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="0", padx=28, pady=22,  font="lucida 15 bold",bg="grey")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="+", padx=28, pady=22,   font="lucida 15 bold",bg="grey")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="-", padx=28, pady=22,  font="lucida 15 bold",bg="grey")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

f.pack()

f = Frame(root, bg="black")
b = Button(f, text="/", padx=30, pady=22,  font="lucida 15 bold",bg="grey")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="*", padx=30, pady=22,  font="lucida 15 bold",bg="grey")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="C", padx=30, pady=27,   font="lucida 13 bold",bg="grey")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="=", padx=30, pady=22,  font="lucida 15 bold",bg="grey")
b.pack(side=LEFT)
b.bind("<Button-1>", click)


f.pack()

f = Frame(root, bg="black")
b = Button(f, text=".", pady=22,  font="lucida 15 bold",bg="grey",padx=30)
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="00", pady=30,  font="lucida 10 bold",bg="grey",padx=30)
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="%",  pady=30,   font="lucida 10 bold",bg="grey",padx=32)
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="CE", pady=30,  font="lucida 10 bold",bg="grey",padx=30)
b.pack(side=LEFT)
b.bind("<Button-1>", cancel)

f.pack()


root.mainloop()

