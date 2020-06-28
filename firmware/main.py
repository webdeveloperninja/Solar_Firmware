from connection import Connection
from solar_panel import SolarPanel
from user_interface import UserInterface
import xbee
from machine import UART

uart = UART(1, 9600)


def setup():
    client_id = "solar-panel-1"
    get_device_id_at_command = "MY"
    print('Initializing')
    device = xbee.XBee()
    print('Created device')
    device_id = device.atcmd(get_device_id_at_command)
    print('Create connection manager')
    connection_manager = Connection()
    print('create cell connection')
    connection_manager.create_cellular_connection()
    print('create mqtt')
    mqtt_connection = connection_manager.create_mqtt_connection(client_id)
    print('create solar panel')
    solar_panel = SolarPanel(device_id, mqtt_connection)
    print('create user interface')
    user_interface = UserInterface(solar_panel, uart)
    print('try start UI')
    user_interface.start()


setup()
