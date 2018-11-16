from tkinter import Tk, Canvas, PhotoImage, mainloop
import time

WIDTH, HEIGHT = 640, 480

window = Tk()
canvas = Canvas(window, width=WIDTH, height=HEIGHT, bg="#000000")
canvas.pack()
img = PhotoImage(width=WIDTH, height=HEIGHT)
canvas.create_image((WIDTH/2, HEIGHT/2), image=img, state="normal")

for x in range(2000):
        img.put("#aaaa00", (x%WIDTH,x%HEIGHT))
        window.update()
        time.sleep(.01)
        
mainloop()
