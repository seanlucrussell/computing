import tkinter
import time
import random
from PIL import Image, ImageTk
import numpy

width = 7
height = 7
scale = 30

#zero means empty
#one means block
def initialize_world():
    world = create_data()
    for i in range(height//2+1,height):
        for j in range(width):
            world[i,j] = 1
    return world

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
def in_bounds(x,y):
    return x >= 0 and x < height and y >= 0 and y < width
def climber_actions(x,y,world,holding_block):
    #can move left, right. places blocks as normal
    #if there is a one block step up, than can move in that direction
    actions = []
    if in_bounds(x,y-1) and world[x,y-1] == 0:
        actions.append(('m',0,-1))
    elif in_bounds(x-1,y-1) and world[x-1,y-1] == 0 and world[x-1,y] == 0:
        actions.append(('m',-1,-1))
    if in_bounds(x,y+1) and world[x,y+1] == 0:
        actions.append(('m',0,1))
    elif in_bounds(x-1,y+1) and world[x-1,y+1] == 0 and world[x-1,y] == 0:
        actions.append(('m',-1,1))
    if in_bounds(x-1,y) and world[x-1,y] == 0 and (
            (in_bounds(x-1,y-1) and world[x-1,y-1] == 1) or
            (in_bounds(x-1,y+1) and world[x-1,y+1] == 1)):
        actions.append(('m',-1,0))
    if in_bounds(x+1,y) and world[x+1,y] == 0:
        actions.append(('m',1,0))
    if holding_block:
        actions.append(None) # destroy block
        if in_bounds(x,y-1) and world[x,y-1] == 0: actions.append(('p',0,-1))
        if in_bounds(x,y+1) and world[x,y+1] == 0: actions.append(('p',0,1))
        if in_bounds(x-1,y) and world[x-1,y] == 0: actions.append(('p',-1,0))
        if in_bounds(x+1,y) and world[x+1,y] == 0: actions.append(('p',1,0))
    else:
        if in_bounds(x,y-1) and world[x,y-1] == 1: actions.append(('g',0,-1))
        if in_bounds(x,y+1) and world[x,y+1] == 1: actions.append(('g',0,1))
        if in_bounds(x-1,y) and world[x-1,y] == 1: actions.append(('g',-1,0))
        if in_bounds(x+1,y) and world[x+1,y] == 1: actions.append(('g',1,0))
    return actions
def actions(x,y,world,holding_block):
    actions = []
    if in_bounds(x,y-1) and world[x,y-1] == 0: actions.append(('m',0,-1))
    if in_bounds(x,y+1) and world[x,y+1] == 0: actions.append(('m',0,1))
    if in_bounds(x-1,y) and world[x-1,y] == 0: actions.append(('m',-1,0))
    if in_bounds(x+1,y) and world[x+1,y] == 0: actions.append(('m',1,0))
    if holding_block:
        actions.append(None) # destroy block
        if in_bounds(x,y-1) and world[x,y-1] == 0: actions.append(('p',0,-1))
        if in_bounds(x,y+1) and world[x,y+1] == 0: actions.append(('p',0,1))
        if in_bounds(x-1,y) and world[x-1,y] == 0: actions.append(('p',-1,0))
        if in_bounds(x+1,y) and world[x+1,y] == 0: actions.append(('p',1,0))
    else:
        if in_bounds(x,y-1) and world[x,y-1] == 1: actions.append(('g',0,-1))
        if in_bounds(x,y+1) and world[x,y+1] == 1: actions.append(('g',0,1))
        if in_bounds(x-1,y) and world[x-1,y] == 1: actions.append(('g',-1,0))
        if in_bounds(x+1,y) and world[x+1,y] == 1: actions.append(('g',1,0))
    return actions
def take_action_climber(x,y,world,holding_block,action):
    x,y,world,holding_block = take_action(x,y,world,holding_block,action)
    while in_bounds(x+1,y) and world[x+1,y] == 0 and in_bounds(x,y-1) and world[x,y-1] == 0 and in_bounds(x,y+1) and world[x,y+1] == 0:
        x += 1
    return x,y,world,holding_block
def take_action(x,y,world,holding_block,action):
    if action == None:
        return x,y,world,False
    if action[0] == 'm':
        return x+action[1],y+action[2],world,holding_block
    elif action[0] == 'p':
        world[x+action[1],y+action[2]] = 1
        return x,y,world,False
    elif action[0] == 'g':
        world[x+action[1],y+action[2]] = 0
        return x,y,world,True
def take_random_action(x,y,world,holding_block):
    possible_actions = climber_actions(x,y,world,holding_block)
    action = random.choice(possible_actions)
    return take_action_climber(x,y,world,holding_block,action)

def state_after_n_random_moves(x,y,world,holding_block,n):
    for i in range(n):
        x,y,world,holding_block = take_random_action(x,y,world,holding_block)
    return x,y,world,holding_block

def monte_carlo_distinct_states(x,y,world,holding_block,n,branches):
    states = []
    for i in range(branches):
        world_copy = numpy.copy(world)
        state = state_after_n_random_moves(x,y,world_copy,holding_block,n)
        #states.append((state[0],state[1],tuple(map(tuple,state[2])),state[3]))
        states.append((state[0],state[1]))
    return len(set(states))
    
def take_empowered_action(x,y,world,holding_block):
    possible_actions = climber_actions(x,y,world,holding_block)
    best_empowerment = 0
    best_action = possible_actions[0]
    for action in possible_actions:
        world_copy = numpy.copy(world)
        x_copy,y_copy,world_copy,holding_block_copy = take_action_climber(x,y,world_copy,holding_block,action)
        empowerment = monte_carlo_distinct_states(x_copy,y_copy,world_copy,holding_block_copy,15,1000)
        if best_empowerment < empowerment:
            best_empowerment = empowerment
            best_action = action
    print(best_empowerment)
    return take_action_climber(x,y,world,holding_block,best_action)

main,canvas = create_window()    
x,y,world,holding_block = height//2, width//2, initialize_world(), False
while True:
    data = numpy.copy(world)
    data[x,y] = 3
    display_data(canvas,data)
    main.update()
    time.sleep(.1)
    #x,y,world,holding_block = take_random_action(x,y,world,holding_block)
    x,y,world,holding_block = take_empowered_action(x,y,world,holding_block)

main.mainloop()
