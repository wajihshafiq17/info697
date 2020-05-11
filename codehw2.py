from microbit import *
import music
'''
This is a sub-task of the final project code. In this task, the user can start a timer when the start washing their hands.
The timer will run for approximately 20 seconds after which it will sound a buzzer.
The minutes since the last time the hands were washed will be recorded using run time.
'''
minutes = 0  # a variable to track the minutes since last time hands were washed
last = 0  # a variable to record the running_time when the hands are washed

# Main
while True:
    # subtracting the last handwash running time from current running time
    minutes = round(((running_time() - last) / 60000), 1)
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