from sense_hat import SenseHat
import time
from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
from signal import pause

s = SenseHat()
s.low_light = True

green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255,255,255)
nothing = (0,0,0)
pink = (255,105, 180)

def trinket_logo():
    G = green
    Y = yellow
    B = blue
    O = nothing
    logo = [
    O, O, O, O, O, O, O, O,
    O, Y, Y, Y, B, G, O, O,
    Y, Y, Y, Y, Y, B, G, O,
    Y, Y, Y, Y, Y, B, G, O,
    Y, Y, Y, Y, Y, B, G, O,
    Y, Y, Y, Y, Y, B, G, O,
    O, Y, Y, Y, B, G, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo

def raspi_logo():
    G = green
    R = red
    O = nothing
    logo = [
    O, G, G, O, O, G, G, O, 
    O, O, G, G, G, G, O, O,
    O, O, R, R, R, R, O, O, 
    O, R, R, R, R, R, R, O,
    R, R, R, R, R, R, R, R,
    R, R, R, R, R, R, R, R,
    O, R, R, R, R, R, R, O,
    O, O, R, R, R, R, O, O,
    ]
    return logo

def plus():
    W = white
    O = nothing
    logo = [
    O, O, O, O, O, O, O, O, 
    O, O, O, W, W, O, O, O,
    O, O, O, W, W, O, O, O, 
    O, W, W, W, W, W, W, O,
    O, W, W, W, W, W, W, O,
    O, O, O, W, W, O, O, O,
    O, O, O, W, W, O, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo

def equals():
    W = white
    O = nothing
    logo = [
    O, O, O, O, O, O, O, O, 
    O, W, W, W, W, W, W, O,
    O, W, W, W, W, W, W, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, W, W, W, W, W, W, O,
    O, W, W, W, W, W, W, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo

def heart():
    P = pink
    O = nothing
    logo = [
    O, O, O, O, O, O, O, O,
    O, P, P, O, P, P, O, O,
    P, P, P, P, P, P, P, O,
    P, P, P, P, P, P, P, O,
    O, P, P, P, P, P, O, O,
    O, O, P, P, P, O, O, O,
    O, O, O, P, O, O, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo

images = [trinket_logo, trinket_logo, plus, raspi_logo, raspi_logo, equals, heart, heart]
count = 0

x = 3
y = 3
sense = SenseHat()

def clamp(value, min_value=0, max_value=7):
    return min(max_value, max(min_value, value))


def pushed_left(event):
    global x
    if event.action != ACTION_RELEASED:
        x = clamp(x - 1)

def pushed_right(event):
    global x
    if event.action != ACTION_RELEASED:
        x = clamp(x + 1)


sense.stick.direction_left = pushed_left
sense.stick.direction_right = pushed_right

pause()

while True: 

    event = s.stick.wait_for_event()
    sense.stick.direction_left = pushed_left
    s.set_pixels(images[count % len(images)]())
    count += 1
    time.sleep(5)
    event = s.stick.wait_for_event()
    sense.stick.direction_left = pushed_right
    s.set_pixels(images[count % len(images)]())
    count += 1
    time.sleep(3)
  