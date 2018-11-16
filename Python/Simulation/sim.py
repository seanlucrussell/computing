import tkinter
import time
import random

'''

some simulation ideas and constraints:
NxM cellular grid for now. If we wanna do continuous stuff later
we can worry about that later.


'''


width = 500
height = 300

main = tkinter.Tk()
main.geometry(str(width)+'x'+str(height))
main.resizable(width=False, height=False)
canvas = tkinter.Canvas(main, width=width, height=height)
canvas.pack()

person = canvas.create_text(0,0,text="Person")

background = tkinter.PhotoImage(width=width,height=height)
canvas.create_image((width/2,height/2), image=background, state="normal")

def move(agent,x,y):
    #could maybe somehow be done with modulus?
    canvas.move(agent,x,y)
    agent_position = canvas.coords(agent)
    if agent_position[0] > width:
        canvas.move(agent,-width,0)
    elif agent_position[0] < 0:
        canvas.move(agent,width,0)
    if agent_position[1] > height:
        canvas.move(agent,0,-height)
    elif agent_position[1] < 0:
        canvas.move(agent,0,height)

def clamp(n,minn,maxn):
    return min(max(n, minn), maxn)

x_vel = 0
y_vel = 0
for x in range(0,2000):
    position = canvas.coords(person)
    background.put("#aaaaaa", (int(position[0]),int(position[1])))
    x_vel += random.randint(-1,1)
    y_vel += random.randint(-1,1)
    x_vel = clamp(x_vel,-5,5)
    y_vel = clamp(y_vel,-5,5)
    move(person,x_vel,y_vel)
    main.update()
    time.sleep(.01)
main.mainloop()

