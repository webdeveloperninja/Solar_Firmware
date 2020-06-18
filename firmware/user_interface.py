from machine import Pin
import time


class UserInterface:
    def __init__(self, solar_panel):
        self.solar_panel = solar_panel

    def on_button_press(self):
        print("SW2 button has been pressed")
        self.solar_panel.publish_current_state()

        time.sleep_ms(500)

    def start(self):
        button = Pin('D0', Pin.IN, Pin.PULL_UP)

        while True:
            self.switch_press_handler(button, self.on_button_press)
            time.sleep(.2)

    @staticmethod
    def switch_press_handler(io_pin, press_handler):
        if io_pin.value() == 0:
            press_handler()
            return True
        return False
