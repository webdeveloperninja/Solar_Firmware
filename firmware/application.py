from machine import Pin
import time
from communication import Communication


class Application:
    def __init__(self, solar_panel, serial_port):
        self.solar_panel = solar_panel
        self.serial_port = serial_port
        self.communication = Communication()

    def on_button_press(self):
        print("SW2 button has been pressed")
        self.solar_panel.publish_current_state()

        time.sleep_ms(500)

    def on_client_message_received(self, message):
        self.communication.send(message)

    def start(self):
        print("Application: Start")
        button = Pin('D0', Pin.IN, Pin.PULL_UP)

        while True:
            self.switch_press_handler(button, self.on_button_press)
            self.serial_message_handler(self.serial_port, self.on_client_message_received)

    @staticmethod
    def switch_press_handler(io_pin, press_handler):
        if io_pin.value() == 0:
            press_handler()

    @staticmethod
    def serial_message_handler(serial_port, serial_message_handler):
        if serial_port.any() > 0:
            print('Reading Serial Port')
            message = serial_port.read(serial_port.any())
            serial_message_handler(message)
