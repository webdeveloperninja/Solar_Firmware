from connection import connect, subscribe_forever
from machine import Pin


dio10 = Pin("P0", Pin.OUT, value=0)
client_id = "oasidfjoasidfjasdf"
connection = connect(client_id)
topic = "sample/xbee"


def message_handler(topic_name, message_payload):
    print(topic_name, message_payload)
    dio10.toggle()


subscribe_forever(connection, message_handler, topic)