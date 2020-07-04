from machine import Pin
import time
from communication import Communication


class Application:
    def __init__(self, solar_panel, uart):
        self.solar_panel = solar_panel
        self.uart = uart
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
            self.comm_port_handler(self.uart, self.on_client_message_received)

    @staticmethod
    def switch_press_handler(io_pin, press_handler):
        if io_pin.value() == 0:
            press_handler()

    @staticmethod
    def comm_port_handler(comm_port, comm_port_handler):
        if comm_port.any() > 0:
            print('Reading UART')
            message = comm_port.read(comm_port.any())
            comm_port_handler(message)
