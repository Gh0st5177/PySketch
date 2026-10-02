import tkinter as tk
import turtle

root=tk.Tk()

root.geometry("800x800")

canvas=tk.Canvas(root,width=800,height=500)

screen=turtle.TurtleScreen(canvas)
t=turtle.RawTurtle(screen)

def Forward():
    t.forward(int(tEntry.get()))
def Back():
    t.backward(int(tEntry.get()))
def Left():
    t.left(int(tEntry.get()))
def Right():
    t.right(int(tEntry.get()))
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
bForward=tk.Button(root,text="Forward",command=Forward)
bBack=tk.Button(root,text="Back",command=Back)
bLeft=tk.Button(root,text="Left",command=Left)
bRight=tk.Button(root,text="Right",command=Right)
tEntry=tk.Entry(root)
bPenUp=tk.Button(root,text="Pen UP",command=PenUp)
bPenDown=tk.Button(root,text="Pen DOWN",command=PenDown)
bColorToggle=tk.Button(root,text="Toggle Color",command=ToggleColor)

canvas.pack()
bForward.pack()
bBack.pack()
bLeft.pack()
bRight.pack()
tEntry.pack()
bPenUp.pack()
bPenDown.pack()
bColorToggle.pack()

root.mainloop()
