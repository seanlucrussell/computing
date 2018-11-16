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
def generate_caves_v2(player_x,player_y):
    caves = numpy.zeros((height,width),dtype=int)
    caves[player_x,player_y] = 2
    update_caves(player_x,player_y,caves)
    return caves
def adjacent_squares(x,y):
    adjacent = [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]
    for square in adjacent:
        if not out_of_bounds(*square):
            yield square
def update_square(i,j):
    if caves[i,j] != 0:
        return
    directions = [(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1)]
    adjacent = [(i+x[0],j+x[1]) for x in directions]
    for n in range(0,8,2):
        if out_of_bounds(*adjacent[n]):
            continue
        one = caves[adjacent[(n-1)%8]]
        two = caves[adjacent[n]]
        three = caves[adjacent[(n+1)%8]]
        if one == three and one != two and one != 0 and two != 0:
            caves[i,j] = one
            return
def update_corner(i,j):
    one = caves[i,j]
    two = caves[i+1,j]
    three = caves[i,j+1]
    four = caves[i+1,j+1]
    if one == four:
        if two == 0 and three != 0 and three != one:
            caves[i+1,j] = one
        elif two != 0 and two != one and three == 0:
            caves[i,j+1] = one
    elif two == three:
        if one == 0 and four != 0 and four != two:
            caves[i,j] = two
        elif one != 0 and one != two and four == 0:
            caves[i+1,j+1] = two
def update_corners():
    for i in range(width):
        for j in range(height):
            update_square(i,j)
    '''
    for i in range(width-1):
        for j in range(height-1):
            update_corner(i,j)
    '''
def successors(x,y):
    for cell in adjacent_squares(x,y):
        square = caves[x,y]
        if square == 0 or square == 2:
            yield cell
def update_caves(player_x,player_y,caves):
    frontier = [(player_x,player_y)]
    depth = 10
    for i in range(depth):
        next_frontier = []
        while frontier:
            exploring = frontier.pop(0)
            for successor in successors(*exploring):
                update_square(*successor)
                if  caves[successor] == 0:
                    caves[successor] = 1 if random.random() < .45 else 2
                if caves[successor] == 2:
                    next_frontier.append(successor)
        frontier = next_frontier
    update_corners()

def create_window():
    main = tkinter.Tk()
    main.geometry(str(width*scale)+'x'+str(height*scale))
    main.resizable(width=False, height=False)
    canvas = tkinter.Canvas(main, width=width*scale, height=height*scale)
    canvas.pack()
    return main,canvas

def display_data(canvas,data):
    px=numpy.repeat(numpy.repeat(data*80,scale,axis=1),scale,axis=0)
    im=Image.frombytes('L', (width*scale,height*scale), px.astype('b').tostring())
    canvas.photo = ImageTk.PhotoImage(image=im)
    canvas.create_image(0,0,image=canvas.photo,anchor=tkinter.NW)

def key(event):
    """shows key or tk code for the key"""
    global move
    key = event.keysym
    if key == 'Escape':
        main.destroy()
    elif key == 'Up' or key == 'Down' or key == 'Left' or key == 'Right':
        move = key

def move_player(move,x,y,caves):
    if move == 'Left' and not out_of_bounds(x,y-1) and caves[x,y-1] == 2:
        return x,y-1
    elif move == 'Right' and not out_of_bounds(x,y+1) and caves[x,y+1] == 2:
        return x,y+1
    elif move == 'Up' and not out_of_bounds(x-1,y) and caves[x-1,y] == 2:
        return x-1,y
    elif move == 'Down' and not out_of_bounds(x+1,y) and caves[x+1,y] == 2:
        return x+1,y
    else:
        return x,y

main,canvas = create_window()    
main.bind_all('<Key>', key)
move = None
x = width//2
y = height//2
caves = generate_caves_v2(x,y)

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

y = 1/(1+e^-x)
1+e^-x = 1/y
e^-x = 1/y - 1
ln(e^-x) = ln(1/y - 1)
-x = ln(1/y - 1)
x = -ln(1/y - 1)
