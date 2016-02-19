from ev3dev.auto import * # Imports all the necessary variables and functions
import time # This library is used for the sleep commands

# IO Aliases. This makes working with the sensors a little easier

MtCannon = Motor(OUTPUT_A)
MtLeft = Motor(OUTPUT_B)
MtRight = Motor(OUTPUT_C)
MtGrab = Motor(OUTPUT_D)

InInfra = InfraredSensor(INPUT_3)
InColor = ColorSensor(INPUT_1)
InTouch = TouchSensor(INPUT_4)

# Musical tones (In Hertz). These are implemented for fun

C = 261.63
Cs = 277.18
D = 293.66
Ds = 311.13
E = 329.63
F = 349.23
Fs = 369.99
G = 392
Gs = 415.3
A = 440
As = 466.16
B = 493.88
C2 = 523.25

MajArp = (C,100),(E,100),(G,100),(C2,100)   # C major arpeggio
MinArp = (C,100),(Ds,100),(G,100),(C2,100)  # C minor arpeggio

# The code below was used to test the sensor reading.
# It's commented out so that it doesn't affect the main program.

#while True:
#    InColor.value()
#    InTouch.value()
#    print InColor.value()
#    print InTouch.value()
#    time.sleep(1)

# This is the main part of the program

Sound.tone(MajArp)                          # Plays a C major arpeggio to indicate the program starting up

while True:                                 # Unless false, this loop repeats forever
    MtRight.run_forever(duty_cycle_sp=100)  # Starts the right and left drive motors at 100% and 85% respectively
    MtLeft.run_forever(duty_cycle_sp=85)    # This makes the robot constantly veer to the left
    InColor.value()                         # These two lines update the sensors,
    InTouch.value()                         # enabling the robot to sense its environment
    if InTouch.value() == 1:                # Checks if the touch sensor is pressed
        break                               # If it is, the loop is broken and execution continues to line 62
    else:
        if InColor.value() < 30:            # Otherwise, the robot checks if the color sensor is
            MtRight.stop()                  # receiving little reflected light (30% or less)
            time.sleep(0.3)                 # This makes the robot turn right for 0,3 seconds

MtRight.stop()                              # The motors stop and the robot expresses its excitement
MtLeft.stop()                               # over how fun the program is to run
Sound.speak("That was fun. We should try that again!") # You should do what he says :)

# Have fun! -Aksel Holm 2016
