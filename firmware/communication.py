class Communication:
    def send(self, message):
        print("Try send message")
        print(message)

        # Purpose of this class is to handle sending messages
        # to the application broker. MQTT or Http or whatever
        # Need to throttle requests to not blow up data usage
        # Need to limit message size for cost