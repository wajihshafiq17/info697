from microbit import *

temp = 0
cheading = 0
sleepcount = 0
loopcount = 0

# compass.calibrate()
# if(compass.is_calibrated()):
#     display.scroll("Done!")

while True:
    temp = str(temperature())
    cheading = str(compass.heading())
    # the first time the loop runs we don't need to read the file
    if(loopcount == 0):
        tempstore = temp + "," + cheading
        with open('wajihs-data.csv', 'w') as my_file:
            my_file.write(tempstore)
        loopcount = 1
        continue
    # second time on wards we will first read and then write to the file
    with open('wajihs-data.csv') as my_file:
        tempstore = my_file.read()
    tempstore = tempstore + "\n" + temp + "," + cheading  # appending the new readings
    with open('wajihs-data.csv', 'w') as my_file:  # writing to the file
        my_file.write(tempstore)
    # this loop keeps the latest reading displayed for the user
    while(sleepcount < 10):  # the loop will run 10 times giving roughly 10 seconds b/w each reading
        display.scroll(temp + "," + cheading)
        sleep(700)
        sleepcount = sleepcount + 1
    sleepcount = 0