from connection import Connection
from solar_panel import SolarPanel
from user_interface import UserInterface
import xbee


def setup():
    client_id = "solar-panel-1"
    get_device_id_at_command = "MY"

    device = xbee.XBee()
    device_id = device.atcmd(get_device_id_at_command)

    connection_manager = Connection()

    cellular_connection = connection_manager.create_cellular_connection()
    mqtt_connection = connection_manager.create_mqtt_connection(client_id)

    solar_panel = SolarPanel(device_id, mqtt_connection)

    cellular_connection.sms_send(2604940140, 'Hey, your device is online')

    user_interface = UserInterface(solar_panel)
    user_interface.start()

setup()
