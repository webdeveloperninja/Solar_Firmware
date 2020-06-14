class SolarPanel:
    def __init__(self, panel_id, mqtt_connection):
        self.id = panel_id
        self.mqtt_connection = mqtt_connection

    def publish_current_state(self):
        current_state = '{"' + self.__get_panel_id() + '": "Encoded data"}'
        current_state_topic = "solar-panel/state"

        self.mqtt_connection.publish(current_state_topic, current_state)

    def __get_panel_id(self):
        delimiter = '-'
        return self.id + delimiter + 'solar-panel'
