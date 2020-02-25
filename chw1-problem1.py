from microbit import *
import random

number = 0

# The introductory message scrolls once before the main loop starts
display.scroll("Is the number odd or even?")
display.scroll("Press A for Even or press B for Odd")

# Main
while True:
    sleep(1000)  # waits one second before generating a new number
    number = random.randrange(100)  # generates a random number between 0 and 99
    button_a.was_pressed()  # clears any existing selection of button a
    button_b.was_pressed()  # clears any existing selection of button b
    # This scroll loop allows the user to make a selection before a new number is generated
    while True:
        display.scroll(number)
        if(number % 2 == 0):  # if number is even
            if(button_a.was_pressed()):
                display.show(Image.HAPPY)  # shows happy emoji for correct selection
                sleep(1000)
                break  # the scroll loop ends after a selection is made
            elif(button_b.was_pressed()):
                display.show(Image.SAD)  # shows sad emoji for incorrect selection
                sleep(1000)
                break
        else:  # if number is odd
            if(button_a.was_pressed()):
                display.show(Image.SAD)  # shows the sad emoji for incorrect selection
                sleep(1000)
                break
            elif(button_b.was_pressed()):
                display.show(Image.HAPPY)  # shows the happy emoji for correct selection
                sleep(1000)
                break