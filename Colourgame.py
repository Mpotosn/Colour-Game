from tkinter import *
import random

win = Tk()
win.title("Color Game ")

colors = ["red","yellow","purple","blue","green","brown"]
time = 30
points = 0

def startGame(event):
    nextColor()
    if time == 30:
        countdown()


def countdown():
    global time
    if time > 0:
        time -= 1
        timer.configure(text="Time:"+str(time))
        timer.after(1000,countdown)





def nextColor():
    global points
    if time >0:
        if e.get() == colors[1]:
            points +=1
            print(points)
            score.configure(text="Score:"+str(points))
        e.delete(0,END)
        random.shuffle(colors)
        print(colors)
        lbl.configure(text=colors[0], fg=colors[1])

descr = Label(win, text="Type the Color of the Big word")
score = Label(win, text="Score:")
timer = Label(win, text="Time:")
lbl = Label(win, text="Yellow",fg="red", font=("Tahoma",40))
e = Entry(win)


descr.pack()
score.pack()
timer.pack()
lbl.pack()
e.pack()
e.focus_set()   #vasei amesos ton kersora sto entry / m glitonei ena click
win.bind('<Return>', startGame)




win.mainloop()