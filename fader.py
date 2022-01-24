from gpiozero import Button, PWMLED

led = PWM(18)
up_button = Button(23)
down_button = Button(7)

brightness = 1.0        # The LED brightness from 0.0 (off) to 1.0 (brightest)
increment = 0.1         # how much to increase or decrease brightness per press

def up_pressed():       # Called when up_button is pressed
    global brightness
    brightness += increment
    if brightness > 1.0:    # Brightness cannot be greater than 1.0
        brightness = 1.0
    led.value = brightness

def down_pressed():     # Called when down_button is pressed
    global brightness
    brightness -= increment
    if brightness < 0.0:    # Brightness cannot be less than 0.0
        brightness = 0.0
    led.value = brightness

up_button.when_pressed = up_pressed # link up_pressed to up_button
down_button.when_pressed = down_pressed

led.value = brightness          # so that the LED is lit even if buttons not pressed

input("Press ENTER to exit")    # avoid the program finishing
