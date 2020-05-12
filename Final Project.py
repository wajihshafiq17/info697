from microbit import *
import music

count = 0  # a variable to track the face proximity movement
minutes = 0  # a variable to track the minutes since last time hands were washed
last = 0  # a variable to record the running_time when the hands are washed

# The introductory message scrolls once before the main loop starts
display.scroll("Welcome to the Habit Tracker")
display.scroll("At any time, press A for number of face touches or press B for minutes since last handwash")

# Main
while True:
    # subtracting the last handwash running time from current running time
    minutes = round(((running_time() - last) / 60000), 1)
    # the user can press A or B at any point to immediately know the required number
    if(button_a.was_pressed()):
        display.show(count)
        sleep(500)
        display.clear()
    if(button_b.was_pressed()):
        display.show(minutes)
        sleep(500)
        display.clear()
    # recording a face touch using the magnet sensor
    if(pin8.read_digital() == 0):
        count = count + 1
        display.show(count)
        music.pitch(440, 1000)  # plays the buzzer
        sleep(1000)
        music.stop()
        display.clear()
        sleep(500)
    # starting the handwash timer
    if(pin12.read_digital() == 0):
        timer = 20
        # a loop that runs for around 20 seconds
        while timer >= 0:
            display.show(timer)
            timer = timer - 1
            sleep(1000)
        music.pitch(660, 500)  # plays the buzzer to show the end of the timer
        sleep(1000)
        display.clear()
        music.stop()
        last = running_time()  # records the running time when the hands were washed