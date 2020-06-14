from connection import Connection
from solar_panel import SolarPanel
from machine import Pin

import xbee

topic = "solar-panel/status"
client_id = "solar-panel-1"

dio0 = Pin('D0', Pin.IN, Pin.PULL_UP)
dio10 = Pin("P0", Pin.OUT, value=0)

get_device_id_at_command = "MY"

device = xbee.XBee()
device_id = device.atcmd(get_device_id_at_command)

connection_manager = Connection()
connection = connection_manager.create(client_id)

solar_panel = SolarPanel(device_id, connection)

solar_panel.publish_current_state()
