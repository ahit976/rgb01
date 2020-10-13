B = 0
G = 0
R = 0
strip = neopixel.create(DigitalPin.P15, 4, NeoPixelMode.RGB)

def on_forever():
    global R, G, B
    R = 0
    G = 0
    B = 0
    for index in range(255):
        R += 1
        B += -1
        strip.show_color(neopixel.rgb(R, G, B))
        basic.pause(1)
    for index2 in range(255):
        G += 1
        R += -1
        strip.show_color(neopixel.rgb(R, G, B))
        basic.pause(1)
    for index3 in range(255):
        B += 1
        G += -1
        strip.show_color(neopixel.rgb(R, G, B))
        basic.pause(1)
basic.forever(on_forever)
