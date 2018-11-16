import tkinter
import time
import random
from PIL import Image, ImageTk
import numpy

width = 150
height = 100
scale = 5
img_width = width*scale
img_height = height*scale

main = tkinter.Tk()
main.geometry(str(img_width)+'x'+str(img_height))
main.resizable(width=False, height=False)
canvas = tkinter.Canvas(main, width=img_width, height=img_height)
canvas.pack()

data=numpy.array(numpy.random.random((height,width))*7,dtype=int)

def next_state(state):
    n = numpy.copy(state)
    for i in range(state.shape[0]):
        for j in range(state.shape[1]):
            if state[i,j] == 0:
                continue
            x_move = random.randint(-1,1)
            y_move = random.randint(-1,1)
            n[(i+x_move)%height,(j+y_move)%width] = state[i,j]
    return n

while True:
    px=numpy.repeat(numpy.repeat(data*100,scale,axis=1),scale,axis=0)
    im=Image.frombytes('L', (img_width,img_height), px.astype('b').tostring())
    photo = ImageTk.PhotoImage(image=im)
    canvas.create_image(0,0,image=photo,anchor=tkinter.NW)
    main.update()
    data=next_state(data)
    time.sleep(.1)
main.mainloop()

