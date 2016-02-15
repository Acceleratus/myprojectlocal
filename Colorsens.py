from ev3dev.auto import OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, INPUT_3, \
    INPUT_4, Motor, ColorSensor, InfraredSensor, Button, enter
import time

# IO Aliases

MtCannon = Motor(OUTPUT_A)
MtLeft = Motor(OUTPUT_B)
MtRight = Motor(OUTPUT_C)
MtGrab = Motor(OUTPUT_D)

InInfra = InfraredSensor(INPUT_3)
InColor = ColorSensor(INPUT_4)
InEnter = Button.enter()

# Main Sequence
"""
This sequence should let the robot drive forward until the Color Sensor detects
a dark line, at which point it will turn away from it. """

x = 1
while True:
    MtLeft.run_forever(duty_cycle_sp=75)
    MtRight.run_forever(duty_cycle_sp=75)

if InColor < 30:
    MtRight.stop()
    time.sleep(0.1)

if InEnter == True:
    quit()

x += 1
