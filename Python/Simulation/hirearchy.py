import tkinter
import time
import random
from PIL import Image, ImageTk
import numpy

#settings
width = 300
height = 200
scale = 1

img_width = width*scale
img_height = height*scale

#setup ui
main = tkinter.Tk()
main.geometry(str(img_width)+'x'+str(img_height))
main.resizable(width=False, height=False)
canvas = tkinter.Canvas(main, width=img_width, height=img_height)
canvas.pack()

#GOALS
'''
Want several things:
Strategy-game scale dynamics, where leaders can influence the world
Monsters that get more powerful as you get further from civilization. (power means both individual and group, a horde of goblins can be every bit as scary as a lone giant)
Tribal interactions between monsters. Warfare and conquerors and such, or just the occasional dragon swooping down and destroying a goblin camp. (also remenants and history of these interactions would be cool, for instance dragon scales and claw marks littered about the smoldering ruins)
Good individual interactions between players and other agents. Buying stuff at the blacksmith or running from trolls, what have you.
Ability for agents to influence the environment, building walls and forts and houses and clearing roads and the like.

Goblins:
each one has a rank (for now immutable, but could change depending on number of followers)
each one has a leader
if one outranks another, the lower ranking one submits to the other
if both have equal rank, they and their followers go to war
war ends when one of the leaders dies, followers go to surviving leader

can attack neighbors. chance to kill neigbor depends on rank difference
can move one square square is unoccupied. If two move in to same square then what? also how do they decide how to move? is it based on leader?

how do goblins reproduce?

'''


class Agent():
    def __init__(self,name,x,y):
        self.name = name
        self.x = x
        self.y = y

class HirearchyAgent(Agent):
    def __init__(self,name,x,y,rank):
        Agent.__init__(self,name,x,y)
        self.rank = rank

def display_agent(agent):
    return canvas.create_text(agent.x * scale, agent.y * scale, text=agent.name)

def move_agent(agent,x,y):
    agent.x = (x + agent.x) % width
    agent.y = (y + agent.y) % height


agents = []
for i in range(5):
    new_agent = HirearchyAgent(str(i),random.randint(0,width-1),random.randint(0,height-1),i)
    agents.append(new_agent)

def update(agents):
    for agent in agents:
        move_agent(agent,1,1)
    
while True:
    display_agents = []
    for agent in agents:
        display_agents.append(display_agent(agent))
    main.update()
    for display in display_agents:
        canvas.delete(display)
    update(agents)
    time.sleep(.01)

main.mainloop()

