import tkinter
import time
import random
from PIL import Image, ImageTk
import numpy

width = 40
height = 40
scale = 15

def out_of_bounds(x,y):
    return x < 0 or x >= width or y < 0 or y >= height
def set_square(x,y,value,caves):
    if out_of_bounds(x,y): return
    caves[x,y] = value
    for square in [(x-1,y-1),(x-1,y),(x-1,y+1),(x,y+1),(x+1,y+1),(x+1,y),(x+1,y-1),(x,y-1)]:
        avoid_corners(*square,caves)
def generate_caves(x,y):
    caves = create_data()
    caves[x,y] = 2
    update_caves(x,y,caves)
    return caves
def adjacent_squares(x,y):
    return (s for s in [(x-1,y), (x+1,y), (x,y-1), (x,y+1)] if not out_of_bounds(*s))
def avoid_corners(x,y,caves):
    if out_of_bounds(x,y) or caves[x,y] != 0: return
    adj = [(x-1,y-1),(x-1,y),(x-1,y+1),(x,y+1),(x+1,y+1),(x+1,y),(x+1,y-1),(x,y-1)]
    for n in range(0,8,2):
        if out_of_bounds(*adj[n]): continue
        side1,side2,corner = caves[adj[(n-1)%8]],caves[adj[(n+1)%8]],caves[adj[n]]
        if side1 == side2 and side1 != corner and side1 != 0 and corner != 0:
            set_square(x,y,side1,caves)
            return
def update_caves(x,y,caves):
    frontier, explored = [(x,y)], set()
    for i in range(100):
        next_frontier = []
        while frontier:
            exploring = frontier.pop(0)
            explored.add(exploring)
            for successor in adjacent_squares(*exploring):
                if successor in explored: continue
                if  caves[successor] == 0: set_square(*successor, random.randint(1,2), caves)
                if caves[successor] == 2: next_frontier.append(successor)
        frontier = next_frontier
        if not frontier: break

def create_window():
    main = tkinter.Tk()
    main.geometry(str(width*scale)+'x'+str(height*scale))
    main.resizable(width=False, height=False)
    canvas = tkinter.Canvas(main, width=width*scale, height=height*scale)
    canvas.pack()
    return main,canvas
def create_data():
    return numpy.zeros((height,width),dtype=int)
def display_data(canvas,data):
    px=numpy.repeat(numpy.repeat(data*80,scale,axis=1),scale,axis=0)
    im=Image.frombytes('L', (width*scale,height*scale), px.astype('b').tostring())
    canvas.photo = ImageTk.PhotoImage(image=im)
    canvas.create_image(0,0,image=canvas.photo,anchor=tkinter.NW)
def key(event):
    global move
    key = event.keysym
    if key == 'Up' or key == 'Down' or key == 'Left' or key == 'Right': move = key
def move_player(move,x,y,caves):
    if move == 'Left' and not out_of_bounds(x,y-1) and caves[x,y-1] == 2: return x,y-1
    elif move == 'Right' and not out_of_bounds(x,y+1) and caves[x,y+1] == 2: return x,y+1
    elif move == 'Up' and not out_of_bounds(x-1,y) and caves[x-1,y] == 2: return x-1,y
    elif move == 'Down' and not out_of_bounds(x+1,y) and caves[x+1,y] == 2: return x+1,y
    else: return x,y

main,canvas = create_window()    
main.bind_all('<Key>', key)
move = None
x,y = width//2, height//2
caves = generate_caves(x,y)
while True:
    update_caves(x,y,caves)
    data = numpy.copy(caves)
    data[x,y] = 3
    display_data(canvas,data)
    main.update()
    time.sleep(.1)
    x,y = move_player(move,x,y,caves)
    move = None

main.mainloop()
