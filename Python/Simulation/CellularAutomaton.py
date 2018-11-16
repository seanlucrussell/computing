import tkinter
import time
import random
from PIL import Image, ImageTk
import numpy

width = 150
height = 150
scale = 4
img_width = width*scale
img_height = height*scale

main = tkinter.Tk()
main.geometry(str(img_width)+'x'+str(img_height))
main.resizable(width=False, height=False)
canvas = tkinter.Canvas(main, width=img_width, height=img_height)
canvas.pack()

data=numpy.array(numpy.random.random((height,width))*2,dtype=int)
#data = numpy.zeros((height,width),dtype=int)
'''
#glider
data[50,50] = 1
data[50,51] = 1
data[50,49] = 1
data[51,51] = 1
data[52,50] = 1
'''
'''
data[40,50] = 1
data[41,50] = 1
data[40,51] = 1
data[41,51] = 1
data[50,50] = 1
data[50,51] = 1
data[50,52] = 1
data[51,49] = 1
data[51,53] = 1
data[52,48] = 1
data[52,54] = 1
data[53,48] = 1
data[53,54] = 1
data[54,51] = 1
data[55,49] = 1
data[55,53] = 1
data[56,50] = 1
data[56,51] = 1
data[56,52] = 1
data[57,51] = 1
data[60,48] = 1
data[60,49] = 1
data[60,50] = 1
data[61,48] = 1
data[61,49] = 1
data[61,50] = 1
data[62,47] = 1
data[62,51] = 1
data[64,46] = 1
data[64,47] = 1
data[64,51] = 1
data[64,52] = 1
data[74,48] = 1
data[74,49] = 1
data[75,48] = 1
data[75,49] = 1
'''

def next_state(state):
    n = numpy.copy(state)
    for i in range(state.shape[0]):
        for j in range(state.shape[1]):
            neighbors = 0
            for x in range(-1,2):
                for y in range(-1,2):
                    if x == 0 and y == 0:
                        continue
                    if state[(i+x)%height,(j+y)%width] == 1:
                        neighbors += 1
            if neighbors < 2 or neighbors > 3:
                n[i,j] = 0
            elif state[i,j] == 0 and neighbors == 3:
                n[i,j] = 1
    return n

while True:
    px=numpy.repeat(numpy.repeat(data*100,scale,axis=1),scale,axis=0)
    im=Image.frombytes('L', (img_width,img_height), px.astype('b').tostring())
    photo = ImageTk.PhotoImage(image=im)
    canvas.create_image(0,0,image=photo,anchor=tkinter.NW)
    data=next_state(data)
    main.update()
    time.sleep(.01)

main.mainloop()

