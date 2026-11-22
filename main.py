import pgzrun

WIDTH = 500
HEIGHT = 500

def draw():
    screen.fill("red")
    screen.draw.filled_circle((250,250),50,"blue")
    rect = Rect((200,200),(200,200))
    rect.center = 350,350
    screen.draw.rect(rect,"orange")

    screen.draw.line((50,500),(200,200),"white")


pgzrun.go()