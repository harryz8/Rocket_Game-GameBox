tm = 0
dot = 3
text_rq = "Loading Test Game"
import gb
def load():
    import tkinter, turtle
    window = tkinter.Tk()
    window.title("Test Game")
    #window.iconbitmap(
    img = tkinter.PhotoImage(file="./rocket2.png")
    imgl = tkinter.Label(window, image=img)
    imgl.pack()
    box = tkinter.Canvas(window, width=500, height=20)
    t = turtle.RawTurtle(box)
    box.pack()
    t.pensize(width=21)
    t.pencolor("blue")
    t.hideturtle()
    t.penup()
    t.backward(250)
    t.pendown()
    def go():
        global tm
        tm = tm + 1
        t.forward(4)
        if tm != 140:
            window.after(1, go)
        else:
            window.destroy()
    window.after(50, go)
    pad = tkinter.Label(window, text=text_rq)
    pad.pack()
    def change():
        global dot, text_rq
        if dot > 0:
            global text_rq
            text_rq = text_rq + '.'
            pad.config(text=text_rq)
            dot = dot - 1
        elif dot < 1:
            text_rq = "Loading Test Game"
            pad.config(text=text_rq)
            dot = 3
        window.after(200, change)
    window.after(200, change)
    window.mainloop()
def game_start():
    global gb
    root = gb.window()
    root.initialise("502x542","#FFFFFF", 500, 500, "#000000")
    root.config(title="Test Game")
    img1 = gb.imageimport("./rocket2.png")
    wallimg = gb.imageimport("./Asteroid2.png")
    sensorimg = gb.imageimport("./Sensor.png")
    sprite1 = gb.SpriteVar()
    sprite1.add(root, img1, XPad=250-16, YPad=500-58)
    wall1 = gb.SpriteVar()
    wall4 = gb.SpriteVar()
    wall7 = gb.SpriteVar()
    sensor = gb.SpriteVar()
    wall1.add(root, wallimg, XPad = 0, YPad=296-50-68-68)
    wall4.add(root, wallimg, XPad = 500-75, YPad=364-50-68)
    wall7.add(root, wallimg, XPad = 0, YPad=432-50)
    sensor.add(root, sensorimg, YPad = -20, XPad = 0)
    c_sprite1 = gb.CollisionBubble()
    c_sprite1.assign(sprite1, 58, 33)
    c_sprite1.stay_in_playing_area(root)
    c_wall1 = gb.CollisionBubble()
    c_wall1.assign(wall1, 50, 75)
    c_wall4 = gb.CollisionBubble()
    c_wall4.assign(wall4, 50, 75)
    c_wall7 = gb.CollisionBubble()
    c_wall7.assign(wall7, 50, 75)
    c_sensor = gb.CollisionBubble()
    c_sensor.assign(sensor, 20, 500)
    gb.KeyPresstoMove(root, "<Down>", sprite1, "d")
    gb.KeyPresstoMove(root, "<Up>", sprite1, "u")
    def crash_react():
        print("Smash!!!!")
        sprite1.move(root, 250-16, 500-58+1)
    gb.constant_collision_check(root, sprite1, wall1, crash_react)
    gb.constant_collision_check(root, sprite1, wall4, crash_react)
    gb.constant_collision_check(root, sprite1, wall7, crash_react)
    def win():
        print("You Won!")
        msg2 = gb.message(root, text="You Won!")
        msg2.config(bg_colour="#FFFFFF")
        root.config(window_geometry="502x561")
    gb.constant_collision_check(root, sprite1, sensor, win)
    wall1.autowalk(root, "E", 45, False, wall1.xpad, wall1.ypad, speed=90)
    wall4.autowalk(root, "W", 45, False, wall4.xpad, wall4.ypad, speed=80)
    wall7.autowalk(root, "E", 45, False, wall7.xpad, wall7.ypad, speed=70)
    msg1 = gb.message(root, text="Press the up and down arrow keys\nto launch the rocket into the sky!")
    msg1.config(bg_colour="#FFFFFF")
    root.window.mainloop()
load()
game_start()
