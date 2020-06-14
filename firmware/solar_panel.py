import machine
import json


class SolarPanel:
    def __init__(self, panel_id, mqtt_connection):
        self.id = panel_id
        self.mqtt_connection = mqtt_connection

    def publish_current_state(self):
        current_state_topic = "solar-panel/state"
        panel_state = json.dumps(self.__get_current_state())

        print("--- start publish panel state ---")
        print("Topic: " + current_state_topic)
        print("State: " + panel_state)

        self.mqtt_connection.publish(current_state_topic, panel_state)
        print("--- end publish panel state ---")

    def __get_current_state(self):
        analog_1 = machine.ADC('D1')

        return {
            "id": self.__get_panel_id(),
            "analogOne": analog_1.read()
        }

    def __get_panel_id(self):
        delimiter = '-'
        return self.id + delimiter + 'solar-panel'
