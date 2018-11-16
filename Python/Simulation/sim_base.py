import tkinter
import time
import random
from PIL import Image, ImageTk
import numpy

#settings
width = 150
height = 100
scale = 3

img_width = width*scale
img_height = height*scale

#setup ui
main = tkinter.Tk()
main.geometry(str(img_width)+'x'+str(img_height))
main.resizable(width=False, height=False)
canvas = tkinter.Canvas(main, width=img_width, height=img_height)
canvas.pack()

#main data
#format is numpy array of shape (width,height,3) where rgb color values are stored. need some sort of way to turn environment data into this format for any type of job
data=numpy.array(numpy.random.random((height,width,3))*256,dtype=int)

#display agent, always on top of image
#agent is specified by a name/type, color?, and coordinates

class Agent():
    def __init__(self,name,x,y):
        self.name = name
        self.x = x
        self.y = y

def display_agent(agent):
    return canvas.create_text(agent.x * scale, agent.y * scale, text=agent.name)

def move_agent(agent,x,y):
    agent.x = (x + agent.x) % width
    agent.y = (y + agent.y) % height

test_agent = Agent("test",width/2,height/2)
    
#main update loop
while True:
    px=numpy.repeat(numpy.repeat(data,scale,axis=1),scale,axis=0)
    im=Image.frombytes('RGB', (img_width,img_height), px.astype('b').tostring())
    photo = ImageTk.PhotoImage(image=im)
    canvas.create_image(0,0,image=photo,anchor=tkinter.NW)
    agent = display_agent(test_agent)
    move_agent(test_agent,1,1)
    main.update()
    time.sleep(.001)

main.mainloop()

