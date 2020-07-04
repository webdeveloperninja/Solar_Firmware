from machine import Pin
import time


class Application:
    def __init__(self, solar_panel, uart):
        self.solar_panel = solar_panel
        self.uart = uart

    def on_button_press(self):
        print("SW2 button has been pressed")
        self.solar_panel.publish_current_state()

        time.sleep_ms(500)

    def start(self):
        print("Application: Start")
        button = Pin('D0', Pin.IN, Pin.PULL_UP)

        while True:
            self.switch_press_handler(button, self.on_button_press)
            self.comm_port_handler(self.uart)

    @staticmethod
    def switch_press_handler(io_pin, press_handler):
        if io_pin.value() == 0:
            press_handler()
            return True
        return False

    @staticmethod
    def comm_port_handler(comm_port):
        if comm_port.any() > 0:
            print('Reading UART')
            read_text = comm_port.read(comm_port.any())
            print(read_text)
            time.sleep(.5)
