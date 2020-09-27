from sense_hat import SenseHat

import time





yellow = (255, 255, 0)
nothing = (0,0,0)
pink = (255,105, 180)

def L():
    Y = yellow
    O = nothing
    logo = [
    O, O, O, O, O, O, O, O,
    O, Y, O, O, O, O, O, O,
    O, Y, O, O, O, O, O, O,
    O, Y, O, O, O, O, O, O,
    O, Y, O, O, O, O, O, O,
    O, Y, O, O, O, O, O, O,
    O, Y, Y, Y, Y, Y, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo



def Y():
    P = pink
    O = nothing
    logo = [
    O, O, O, O, O, O, O, O,
    O, P, O, O, O, O, P, O,
    O, O, P, O, O, P, O, O,
    O, O, P, P, P, P, O, O,
    O, O, O, P, P, O, O, O,
    O, O, O, P, P, O, O, O,
    O, O, O, P, P, O, O, O,
    O, O, O, P, P, O, O, O,
    ]
    return logo


s = SenseHat()
event = s.stick.wait_for_event()
s.set_pixels(Y)
event = s.stick.wait_for_event()
s.set_pixels(L)
    
