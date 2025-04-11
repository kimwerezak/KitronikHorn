// When the MicroBit logo is touched the Kitronik horn will honk.
input.onLogoEvent(TouchButtonEvent.Pressed, function honk_horn() {
    Kitronik_Move_Motor.beepHorn()
})
