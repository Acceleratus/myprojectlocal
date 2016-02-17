from ev3dev.auto import *
import time

# IO Aliases

MtCannon = Motor(OUTPUT_A)
MtLeft = Motor(OUTPUT_B)
MtRight = Motor(OUTPUT_C)
MtGrab = Motor(OUTPUT_D)

InInfra = InfraredSensor(INPUT_3)
InColor = ColorSensor(INPUT_1)
InTouch = TouchSensor(INPUT_4)

#Musical tones (In Hertz)

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
# Main Sequence
"""
This tests various features of the robot. """


while Button.on_enter(1) == False:
    MtLeft.run_forever(duty_cycle_sp=100)
    MtRight.run_forever(duty_cycle_sp=100)

Sound.tone(440,100).Wait()

