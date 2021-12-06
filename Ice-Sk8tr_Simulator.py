import pgzrun
WIDTH = 420
HEIGHT = 210

rink = Actor("rink")
iceskater = Actor("ice-skater")

def draw():
    screen.clear()
    rink.draw()
    iceskater.draw()

def update():
    draw()

    if keyboard.left:
        iceskater.x = iceskater.x - 0.91
    elif keyboard.right:
        iceskater.x = iceskater.x + 0.91
    elif keyboard.up:
        iceskater.y = iceskater.y - 0.91
    elif keyboard.down:
        iceskater.y = iceskater.y + 0.91

pgzrun.go()
    
