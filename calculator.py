from tkinter import *
import tkinter.messagebox as tkmsg
def click(event):
    global displayval # for update the value of global variable

    text = event.widget.cget("text")  # This funct gives the text associated with that widget
    # print(text)

    if text == "=":
        if displayval.get().isdigit():
            ans = int(displayval.get())
        else:
            try:
                ans = eval(screen.get()) # eval() function takes a expression as string and perform that operation

            except Exception as e:
                print(e)
                ans = "Error"

            

        displayval.set(ans)
        screen.update()

    elif text == "C":
        displayval.set("") # clearing the values on entry widget as we press "C"
        screen.update()

    elif text == "←":
        a = int(displayval.get())/10  # For clearing last digit
        displayval.set(int(a))

    else:
        displayval.set(displayval.get() + text) # all values are appended as we click on various buttons
        screen.update() # to update the values on entry widget   


root = Tk()
root.title(" Calculator")
root.geometry("370x400") 
root.wm_iconbitmap("calc.ico")
root.resizable(False, False)
root.config(background="#EBF5FB")
Label(root, text="GUI Calculator", padx=20, pady=5, fg="red2", font="Verdana 16 bold", bg="#EBF5FB", borderwidth=2, relief=GROOVE).pack(padx=50,pady=15)

displayval = StringVar()
displayval.set("")

screen = Entry(root, textvariable=displayval, bg="azure", font="TrebuchetMS 20 ")
screen.pack(padx=6, pady=10, fill=X)


f= Frame(root, bg="#EBF5FB")

b = Button(f, text="C", padx=29,pady=6,font="lucida 15 ")
b.pack(side=LEFT, padx=2, pady=2, anchor="sw")
b.config(background="light cyan")
b.bind("<Button-1>", click)

b = Button(f, text="%", padx=27,pady=6,font="lucida 15 ")
b.pack(side=LEFT, padx=2, pady=2, anchor="sw")
b.config(background="light cyan")
b.bind("<Button-1>", click)

b = Button(f, text="/", padx=32,pady=6,font="lucida 15 ")
b.pack(side=LEFT, padx=2, pady=2, anchor="sw")
b.config(background="light cyan")
b.bind("<Button-1>", click)

b = Button(f, text="←", padx=27,pady=6,font="lucida 15 ")
b.pack(side=LEFT, padx=2, pady=2, anchor="sw")
b.config(background="light cyan")
b.bind("<Button-1>", click)

f.pack()


f= Frame(root, bg="#EBF5FB")

b = Button(f, text="7", padx=30,pady=6,font="lucida 15 ")
b.pack(side=LEFT, padx=2, pady=2, anchor="sw")
b.config(background="ghost white")
b.bind("<Button-1>", click)

b = Button(f, text="8", padx=30,pady=6,font="lucida 15 ")
b.pack(side=LEFT, padx=2, pady=2, anchor="sw")
b.config(background="ghost white")
b.bind("<Button-1>", click)

b = Button(f, text="9", padx=30,pady=6,font="lucida 15 ")
b.pack(side=LEFT, padx=2, pady=2, anchor="sw")
b.config(background="ghost white")
b.bind("<Button-1>", click)

b = Button(f, text="*", padx=33,pady=6,font="lucida 15 ")
b.pack(side=LEFT, padx=2, pady=2, anchor="sw")
b.config(background="light cyan")
b.bind("<Button-1>", click)

f.pack()


f= Frame(root, bg="#EBF5FB")

b = Button(f, text="4", padx=30,pady=6,font="lucida 15 ")
b.pack(side=LEFT, padx=2, pady=2, anchor="sw")
b.config(background="ghost white")
b.bind("<Button-1>", click)

b = Button(f, text="5", padx=30,pady=6,font="lucida 15 ")
b.pack(side=LEFT, padx=2, pady=2, anchor="sw")
b.config(background="ghost white")
b.bind("<Button-1>", click)

b = Button(f, text="6", padx=30,pady=6,font="lucida 15 ")
b.pack(side=LEFT, padx=2, pady=2, anchor="sw")
b.config(background="ghost white")

b = Button(f, text="-", padx=33,pady=6,font="lucida 15 ")
b.pack(side=LEFT, padx=2, pady=2, anchor="sw")
b.config(background="light cyan")
b.bind("<Button-1>", click)

f.pack()


f= Frame(root, bg="#EBF5FB")

b = Button(f, text="1", padx=30,pady=6,font="lucida 15 ")
b.pack(side=LEFT, padx=2, pady=2, anchor="sw")
b.config(background="ghost white")
b.bind("<Button-1>", click)

b = Button(f, text="2", padx=30,pady=6,font="lucida 15 ")
b.pack(side=LEFT, padx=2, pady=2, anchor="sw")
b.config(background="ghost white")
b.bind("<Button-1>", click)

b = Button(f, text="3", padx=30,pady=6,font="lucida 15 ")
b.pack(side=LEFT, padx=2, pady=2, anchor="sw")
b.config(background="ghost white")
b.bind("<Button-1>", click)

b = Button(f, text="+", padx=30,pady=6,font="lucida 15 ")
b.pack(side=LEFT, padx=2, pady=2, anchor="sw")
b.config(background="light cyan")
b.bind("<Button-1>", click)

f.pack()


f= Frame(root, bg="#EBF5FB")

b = Button(f, text="00", padx=24,pady=6,font="lucida 15 ")
b.pack(side=LEFT, padx=2, pady=2, anchor="sw")
b.config(background="ghost white")
b.bind("<Button-1>", click)

b = Button(f, text="0", padx=30,pady=6,font="lucida 15 ")
b.pack(side=LEFT, padx=2, pady=2, anchor="sw")
b.config(background="ghost white")
b.bind("<Button-1>", click)

b = Button(f, text=".", padx=33,pady=6,font="lucida 15 ")
b.pack(side=LEFT, padx=2, pady=2, anchor="sw")
b.config(background="ghost white")
b.bind("<Button-1>", click)

b = Button(f, text="=", padx=30,pady=6,font="lucida 15 ")
b.pack(side=LEFT, padx=2, pady=2, anchor="sw")
b.config(background="lightskyblue1")
b.bind("<Button-1>", click)

f.pack()
root.mainloop()