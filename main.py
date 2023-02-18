radio.set_group(1)

def on_forever():
    if input.button_is_pressed(Button.AB):
        basic.show_leds("""
            . . # . .
                        . # # # .
                        # . # . #
                        . . # . .
                        . . # . .
        """)
        radio.send_string("menj")
    elif input.button_is_pressed(Button.A):
        basic.show_leds("""
            . . # . .
                        . # . . .
                        # # # # #
                        . # . . .
                        . . # . .
        """)
        radio.send_string("balra")
    elif input.button_is_pressed(Button.B):
        basic.show_leds("""
            . . # . .
                        . . . # .
                        # # # # #
                        . . . # .
                        . . # . .
        """)
        radio.send_string("jobbra")
    elif input.logo_is_pressed():
        basic.show_leds("""
            . . # . .
                        . . # . .
                        # . # . #
                        . # # # .
                        . . # . .
        """)
        radio.send_string("tolass")
    else:
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
        """)
        radio.send_string("állj")
basic.forever(on_forever)
