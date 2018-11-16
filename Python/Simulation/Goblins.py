import tkinter
import time
import random
from random import randint
from PIL import Image, ImageTk
import numpy
'''
Goblins:
each one has a rank (for now immutable, but could change depending on number of followers)
each one has a leader
if one outranks another, the lower ranking one submits to the other
if both have equal rank, they and their followers go to war
war ends when one of the leaders dies, followers go to surviving leader

can attack neighbors. chance to kill neigbor depends on rank difference
can move one square square is unoccupied. If two move in to same square then what? also how do they decide how to move? (run from strong things, towards weak things, otherwise random) is it based on leader?

how do goblins reproduce?

goblins should have a home base (camp or whatever). Should this be a straight incentive or some emergent property from other factors (like they can't carry everything, or its useful to have some stuff set up, etc). Camp should move occassionally too, like when they get driven off by adventurers or when there are better opportunities elsewhere.

REMEMBER: you aren't trying to accurately simulate the world. The important thing is to come up with a system with good analogies to the real world.

also want the system to be resistant to major change. Like a single goblin death doesn't change the whole dynamics of the world or even its tribe, unless it was the leader. But the system does still change, so if there is a major campaign against a specific goblin camp then the camp might be permanently destroyed.
'''

attack_range = 5
sight_range = 5

'''
at each time step a goblin can either attack or move or dominate?

new idea, rank is based off of total number of followers. if you attack and lose, you become a follower of your enemy? and then their rank increases?
then, each time a subservient goblin encounters another goblin with a different leader, they can attack.

for cellular automata, total number of goblins remains constant except in cases where goblins reproduce or die.

'''

class Goblin():
    def __init__(self,rank,x,y):
        self.rank = rank
        self.x = x
        self.y = y
        self.leader = None
        self.followers = []

    def kill(self):
        for follower in self.followers:
            follower.leader = None
        goblins.remove(self)
        
    def move(self,x,y):
        self.x = (self.x + x) % width
        self.y = (self.y + y) % height
        for follower in self.followers:
            follower.move(x,y)

    def attack(self,other):
        rank_difference = self.rank - other.rank
        probability = (rank_difference + 10) * 5
        if random.random() > probability:
            other.kill()

def update_goblin(goblin):
    for other_goblin in goblins:
        if other_goblin == goblin:
            continue
        dist = distance(goblin,other_goblin)
        if dist <= attack_range:
            battle(goblin,other_goblin)
    if goblin.leader == None:
        goblin.move(randint(-1,1),randint(-1,1))
        
def update(goblins):
    for goblin in goblins:
        update_goblin(goblin)

def distance(goblin_1,goblin_2):
    x_diff = (goblin_2.x - goblin_1.x) % width
    y_diff = (goblin_2.y - goblin_1.y) % height
    dist = min(x_diff, width - x_diff) + min(y_diff, height - y_diff)
    return dist
    
def battle(goblin_1,goblin_2):
    if goblin_1.rank == goblin_2.rank:
        goblin_1.attack(goblin_2)
    elif goblin_1.rank > goblin_2.rank:
        if goblin_2.leader != None:
            goblin_2.leader.followers.remove(goblin_2)
        goblin_2.leader = goblin_1
        goblin_1.followers.append(goblin_2)
    elif goblin_1.rank < goblin_2.rank:
        if goblin_1.leader != None:
            goblin_1.leader.followers.remove(goblin_1)
        goblin_1.leader = goblin_2
        goblin_2.followers.append(goblin_1)
    
        
def as_numpy(goblins):
    array = numpy.zeros((height,width),dtype=int)
    for goblin in goblins:
        array[goblin.y,goblin.x] = goblin.rank
    return array

width = 30
height = 20
scale = 12

goblins = []

for i in range(50):
    new_goblin = Goblin(randint(1,7),randint(0,width-1),randint(0,height-1))
    goblins.append(new_goblin)


img_width = width*scale
img_height = height*scale

main = tkinter.Tk()
main.geometry(str(img_width)+'x'+str(img_height))
main.resizable(width=False, height=False)
canvas = tkinter.Canvas(main, width=img_width, height=img_height)
canvas.pack()

data=numpy.array(numpy.random.random((height,width))*7,dtype=int)

while True:
    data = as_numpy(goblins)
    px=numpy.repeat(numpy.repeat(data*100,scale,axis=1),scale,axis=0)
    im=Image.frombytes('L', (img_width,img_height), px.astype('b').tostring())
    photo = ImageTk.PhotoImage(image=im)
    canvas.create_image(0,0,image=photo,anchor=tkinter.NW)
    main.update()
    update(goblins)
    time.sleep(.1)
main.mainloop()
