#When the MicroBit logo is touched the Kitronik horn will honk.
def honk_horn():
    Kitronik_Move_Motor.beep_horn()

input.on_logo_event(TouchButtonEvent.PRESSED, honk_horn)
