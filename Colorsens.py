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

# Musical tones (In Hertz)

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

MajArp = (C,100),(E,100),(G,100),(C2,100)
MinArp = (C,100),(Ds,100),(G,100),(C2,100)
# Main Sequence
"""
This tests various features of the robot. """

#Sound.tone(MajArp)
col = InColor.value
tch = InTouch.value

while True:
    InColor.value()
    InTouch.value()
    print InColor.value()
    print InTouch.value()
    time.sleep(1)
#while True:
#    MtRight.run_forever(duty_cycle_sp=85)
#    MtLeft.run_forever(duty_cycle_sp=100)
#    if tch == 1:
#        break
#    else:
#        if col < 30:
#            MtLeft.stop()
#            time.sleep(0.3)

#MtRight.stop()
#MtLeft.stop()
#Sound.speak("That was fun. We should try that again!")
