from microbit import *


def draw_r(brightness):
    display.set_pixel(0, 4, brightness)
    display.set_pixel(0, 3, brightness)
    display.set_pixel(0, 2, brightness)
    display.set_pixel(0, 1, brightness)
    display.set_pixel(0, 0, brightness)
    display.set_pixel(0, 1, brightness)
    display.set_pixel(0, 2, brightness)
    display.set_pixel(0, 3, brightness)
    display.set_pixel(4, 0, brightness)
    display.set_pixel(4, 1, brightness)
    display.set_pixel(4, 2, brightness)
    display.set_pixel(3, 2, brightness)
    display.set_pixel(3, 3, brightness)
    display.set_pixel(4, 4, brightness)
    display.set_pixel(2, 2, brightness)
    display.set_pixel(1, 0, brightness)
    display.set_pixel(2, 0, brightness)
    display.set_pixel(3, 0, brightness)
    sleep(300)


brightness = 1
dif = 1
while True:
    draw_r(brightness)
    brightness += dif

    if brightness > 8:
        dif = -1
    elif brightness < 2:
        dif = 1


