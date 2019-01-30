import turtle

def recaman(n):
  sequence = set(); pos = 0
  for i in range(n):
    pos += i if i > pos or pos-i in sequence else -i
    sequence.add(pos); yield pos

def draw_arc(jump, up):
  turtle.circle(-jump if up else jump, 180)

def draw(scale=5):
  turtle.speed('fastest'); turtle.reset(); turtle.setheading(90)
  rec = recaman(400); N = 0; up = True
  for n in rec:
    draw_arc((n-N)*scale,up)
    N = n; up = not up

draw()
