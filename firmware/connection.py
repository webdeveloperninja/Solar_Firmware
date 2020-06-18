from umqtt.simple import MQTTClient
import time, network


class Connection:
    @staticmethod
    def create_cellular_connection():
        network_connection = network.Cellular()

        while not network_connection.isconnected():
            print("waiting for network connection...")
            time.sleep(4)

        return network_connection

    @staticmethod
    def create_mqtt_connection(client_id):
        aws_endpoint = 'a24e0i570zhegg.iot.us-east-2.amazonaws.com'

        ssl_params = {'keyfile': "/flash/cert/aws.key",
                      'certfile': "/flash/cert/aws.crt",
                      'ca_certs': "/flash/cert/aws.ca"}

        mqtt_connection = MQTTClient(client_id, aws_endpoint, ssl=True, ssl_params=ssl_params)
        mqtt_connection.connect()

        return mqtt_connection
