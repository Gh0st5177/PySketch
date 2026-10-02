import tkinter as tk
import turtle

root=tk.Tk()

root.geometry("800x800")

canvas=tk.Canvas(root,width=800,height=500)

screen=turtle.TurtleScreen(canvas)
t=turtle.RawTurtle(screen)

def ReadValue():
    return int(tEntry.get())
def Forward():
    t.forward(ReadValue())
def Back():
    t.backward(ReadValue())
def Left():
    t.left(ReadValue())
def Right():
    t.right(ReadValue())

bForward=tk.Button(root,text="Forward",command=Forward)
bBack=tk.Button(root,text="Back",command=Back)
bLeft=tk.Button(root,text="Left",command=Left)
bRight=tk.Button(root,text="Right",command=Right)
tEntry=tk.Entry(root)

canvas.pack()
bForward.pack()
bBack.pack()
bLeft.pack()
bRight.pack()
tEntry.pack()

root.mainloop()
