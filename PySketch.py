import tkinter as tk
import turtle

root=tk.Tk()

root.geometry("800x675")

canvas=tk.Canvas(root,width=800,height=500)

screen=turtle.TurtleScreen(canvas)
t=turtle.RawTurtle(screen)
t.pensize(2)

def Forward():
    t.forward(int(tEntry.get()))
def Back():
    t.backward(int(tEntry.get()))
def Left():
    t.left(int(tEntry.get()))
def Right():
    t.right(int(tEntry.get()))
def Home():
    t.home()
def PenUp():
    t.penup()
def PenDown():
    t.pendown()
x=0
def ToggleColor():
    global x
    if x==0:
        t.pencolor("Red")
        x=1
    elif x==1:
        t.pencolor("Blue")
        x=2
    else:
        t.pencolor("Black")
        x=0

fMovement=tk.Frame(root,bd=3,relief=tk.SUNKEN)
bForward=tk.Button(fMovement,text="Forward",command=Forward)
bBack=tk.Button(fMovement,text="Back",command=Back)
bLeft=tk.Button(fMovement,text="Left",command=Left)
bRight=tk.Button(fMovement,text="Right",command=Right)
bHome=tk.Button(fMovement,text="Home",command=Home)
tEntry=tk.Entry(root)
bPenUp=tk.Button(root,text="Pen UP",command=PenUp)
bPenDown=tk.Button(root,text="Pen DOWN",command=PenDown)
bColorToggle=tk.Button(root,text="Toggle Color",command=ToggleColor)

canvas.grid(row=0,column=0,columnspan=2,padx=10,pady=10)
fMovement.grid(row=1,column=0,rowspan=4,sticky="nsew")
bForward.grid(row=0,column=0,columnspan=2,sticky="nsew")
bBack.grid(row=2,column=0,columnspan=2,sticky="nsew")
bLeft.grid(row=1,column=0,sticky="nsew")
bRight.grid(row=1,column=1,sticky="nsew")
bHome.grid(row=3,column=0,columnspan=2,sticky="nsew")
tEntry.grid(row=1,column=1,sticky="nsew")
bPenUp.grid(row=2,column=1,sticky="nsew")
bPenDown.grid(row=3,column=1,sticky="nsew")
bColorToggle.grid(row=4,column=1,sticky="nsew")

fMovement.grid_columnconfigure(0,weight=1)
fMovement.grid_columnconfigure(1,weight=1)
fMovement.grid_rowconfigure(0,weight=1)
fMovement.grid_rowconfigure(1,weight=1)
fMovement.grid_rowconfigure(2,weight=1)
fMovement.grid_rowconfigure(3,weight=1)

root.mainloop()
