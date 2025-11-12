import tkinter
globroot = 0

class window:
    def _init_(self):
        pass
    def initialise(self, window_geometry, window_bg_colour, playing_area_width, playing_area_height, playing_area_bg_colour):
        self.window = tkinter.Tk()
        self.window.config(bg=window_bg_colour)
        self.window.geometry(window_geometry)
        self.window.resizable(2000, 1000)
        geom = window_geometry.split('x')
        self.window_height = geom[0]
        self.window_width = geom[1]
        self.window_geometry = window_geometry
        self.playing_area_height = playing_area_height
        self.playing_area_width = playing_area_width
        self.playing_area = tkinter.Canvas(self.window, width=playing_area_width, height=playing_area_height, bg=playing_area_bg_colour)
        self.playing_area.pack()
    def config(self, **options):
        try:
            self.window.title(options["title"])
        except:
            pass
        try:
            self.window.geometry(options["window_geometry"])
            geom = options["window_geometry"].split('x')
            self.window_height = geom[0]
            self.window_width = geom[1]
            self.window_geometry = options["window_geometry"]
        except:
            pass
        try:
            self.window.config(bg=options["window_bg_colour"])
        except:
            pass
        try:
            self.playing_area.config(width=options["playing_area_width"])
            self.playing_area_width = options["playing_area_width"]
        except:
            pass
        try:
            self.playing_area.config(height=options["playing_area_height"])
            self.playing_area_height = options["playing_area_height"]
        except:
            pass
        try:
            self.playing_area.config(bg=options["playing_area_bg_colour"])
        except:
            pass
    def withdraw(self):
        self.window.withdraw()
    def imgbackground(self, window, file):
        bgimg = tkinter.PhotoImage(file=file)
        self.imgbg = window.playing_area.create_image(0, 0, image=bgimg, anchor=tkinter.NW)
def imageimport(file):
    img = tkinter.PhotoImage(file=file)
    return img
class SpriteVar:
    def _init_():
        pass
    def add(self, window, image, XPad=1, YPad=1):
        anchor=tkinter.NW
        self.character = window.playing_area.create_image(XPad, YPad, image=image, anchor=anchor)
        self.xpad = XPad
        self.ypad = YPad
        self.image = image
        self.anchor = anchor
    def up(self, window, step=10):
        window.playing_area.delete(self.character)
        self.ypad = self.ypad - step
        self.character = window.playing_area.create_image(self.xpad, self.ypad, image=self.image, anchor=self.anchor)
    def down(self, window, step=10):
        window.playing_area.delete(self.character)
        self.ypad = self.ypad + step
        self.character = window.playing_area.create_image(self.xpad, self.ypad, image=self.image, anchor=self.anchor)
    def left(self, window, step=10):
        window.playing_area.delete(self.character)
        self.xpad = self.xpad - step
        self.character = window.playing_area.create_image(self.xpad, self.ypad, image=self.image, anchor=self.anchor)
    def right(self, window, step=10):
        window.playing_area.delete(self.character)
        self.xpad = self.xpad + step
        self.character = window.playing_area.create_image(self.xpad, self.ypad, image=self.image, anchor=self.anchor)
    def move(self, window, xcoord, ycoord):
        window.playing_area.delete(self.character)
        self.xpad = xcoord
        self.ypad = ycoord
        self.character = window.playing_area.create_image(self.xpad, self.ypad, image=self.image, anchor=self.anchor)
    def autowalk(self, window, compass_direction, distance, walk_return, startx, starty, speed=75):
        window.playing_area.delete(self.character)
        self.xpad = startx
        self.ypad = starty
        self.autowalk_startx = startx
        self.autowalk_starty = starty
        self.autowalk_window = window
        self.autowalk_compass_direction = compass_direction.upper()
        self.autowalk_distance = distance
        self.autowalk_orig_distance = distance
        self.autowalk_walk_return = walk_return
        self.autowalk_return_d = 0
        self.autowalk_speed = 100 - speed
        window.window.after(self.autowalk_speed, self._auto_move_auto)
    def _auto_move_auto(self):
        if self.autowalk_distance > 0:
            self.autowalk_distance = self.autowalk_distance - 1
            if self.autowalk_compass_direction == "N":
                self.up(self.autowalk_window)
            elif self.autowalk_compass_direction == "S":
                self.down(self.autowalk_window)
            elif self.autowalk_compass_direction == "E":
                self.right(self.autowalk_window)
            elif self.autowalk_compass_direction == "W":
                self.left(self.autowalk_window)
            self.autowalk_window.window.after(self.autowalk_speed, self._auto_move_auto)
        elif self.autowalk_walk_return == True:
            if self.autowalk_return_d < self.autowalk_orig_distance:
                self.autowalk_return_d = self.autowalk_return_d + 1
                if self.autowalk_compass_direction == "N":
                    self.down(self.autowalk_window)
                elif self.autowalk_compass_direction == "S":
                    self.up(self.autowalk_window)
                elif self.autowalk_compass_direction == "E":
                    self.left(self.autowalk_window)
                elif self.autowalk_compass_direction == "W":
                    self.right(self.autowalk_window)
                self.autowalk_window.window.after(self.autowalk_speed, self._auto_move_auto)
            elif self.autowalk_return_d == self.autowalk_orig_distance:
                self.autowalk_return_d = 0
                self.autowalk_distance = self.autowalk_orig_distance
                self.autowalk_window.window.after(self.autowalk_speed, self._auto_move_auto)
        elif self.autowalk_walk_return == False:
            self.autowalk_distance = self.autowalk_orig_distance
            self.move(self.autowalk_window, self.autowalk_startx, self.autowalk_starty)
            self.autowalk_window.window.after(self.autowalk_speed, self._auto_move_auto)
def KeyPresstoMove(window, key, sprite, direction):
    global globroot
    globroot = window
    direction = direction.lower()
    def movedown(arg):
        global globroot
        sprite.down(globroot)
    def moveup(arg):
        global globroot
        sprite.up(globroot)
    def moveleft(arg):
        global globroot
        sprite.left(globroot)
    def moveright(arg):
        global globroot
        sprite.right(globroot)
    if direction == "d" or direction == "down":
        globroot.window.bind(key, movedown)
    elif direction == "u" or direction == "up":
        globroot.window.bind(key, moveup)
    elif direction == "l" or direction == "left":
        globroot.window.bind(key, moveleft)
    elif direction == "r" or direction == "right":
        globroot.window.bind(key, moveright)
def KeyBind(window, key, function):
    window.window.bind(key, function)
class CollisionBubble:
    def _init_(self):
        pass
    def assign(self, sprite, height_of_sprite, width_of_sprite):
        self.height = height_of_sprite
        self.width = width_of_sprite
        self.sprite = sprite
        self.NWx = sprite.xpad
        self.NWy = sprite.ypad
        sprite.CollisionBubble = self
    def stay_in_playing_area(self, window):
        self.temp_window_x1 = window
        window.window.after(100, self._internal_check)
    def _internal_check(self):
        self.can_height = self.temp_window_x1.playing_area_height
        self.can_width = self.temp_window_x1.playing_area_width
        if self.sprite.xpad < 0:
            self.sprite.right(self.temp_window_x1)
        elif self.sprite.ypad < 0:
            self.sprite.down(self.temp_window_x1)
        elif self.sprite.xpad+self.height > self.can_width:
            self.sprite.left(self.temp_window_x1)
        elif self.sprite.ypad+self.height > self.can_height:
            self.sprite.up(self.temp_window_x1)
        self.temp_window_x1.window.after(100, self._internal_check)
def CheckCollision(main_sprite,  other_sprite):
    collision_outcome = False
    x_outcome = False
    for chnum in range(main_sprite.xpad, main_sprite.xpad+main_sprite.CollisionBubble.width):
        for chnum2 in range(other_sprite.xpad, other_sprite.xpad+other_sprite.CollisionBubble.width):
            #print(str(chnum) + "\n" + "_"+str(chnum2))
            if chnum == chnum2:
                x_outcome = True
    if x_outcome == True:
        for chnum3 in range(main_sprite.ypad, main_sprite.ypad+main_sprite.CollisionBubble.height):
            #print("_/_"+str(chnum3))
            for chnum4 in range(other_sprite.ypad, other_sprite.ypad+other_sprite.CollisionBubble.height):
                #print("_/_/_"+str(chnum4))
                if chnum3 == chnum4:
                    collision_outcome = True
    return collision_outcome
class constant_collision_check:
    def __init__(self, window, main_sprite, other_sprite, function):
        self.temp_window_x2 = window
        self.temp_sprite_x2 = other_sprite
        self.temp_func_x2 = function
        self.temp_main_sprite_x2 = main_sprite
        window.window.after(100, self._internal_check)
    def _internal_check(self):
        self.collision_outcome = False
        self.x_outcome = False
        for self.chnum in range(self.temp_main_sprite_x2.xpad, self.temp_main_sprite_x2.xpad+self.temp_main_sprite_x2.CollisionBubble.width):
            for self.chnum2 in range(self.temp_sprite_x2.xpad, self.temp_sprite_x2.xpad+self.temp_sprite_x2.CollisionBubble.width):
                #print(str(chnum) + "\n" + "_"+str(chnum2))
                if self.chnum == self.chnum2:
                    self.x_outcome = True
        if self.x_outcome == True:
            for self.chnum3 in range(self.temp_main_sprite_x2.ypad, self.temp_main_sprite_x2.ypad+self.temp_main_sprite_x2.CollisionBubble.height):
                #print("_/_"+str(chnum3))
                for self.chnum4 in range(self.temp_sprite_x2.ypad, self.temp_sprite_x2.ypad+self.temp_sprite_x2.CollisionBubble.height):
                    #print("_/_/_"+str(chnum4))
                    if self.chnum3 == self.chnum4:
                        self.collision_outcome = True
        if self.collision_outcome == True:
            self.temp_func_x2()
            self.temp_window_x2.window.after(100, self._internal_check)
        else:
            self.temp_window_x2.window.after(100, self._internal_check)
class message:
    def __init__(self, window, text):
        self.label = tkinter.Label(window.window, text=text)
        self.label.pack()
    def config(self, **options):
        try:
            self.label.config(text=options["text"])
        except:
            pass
        try:
            self.label.config(bg=options["bg_colour"])
        except:
            pass
