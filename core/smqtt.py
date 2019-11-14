import logging

import paho.mqtt.client as mqtt

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


class SilentMQTT(object):

    def __init__(self, broker, port=1883, username=None, password=None, client_id=""):
        self.broker = broker
        self.port = port
        self.broker_username = username
        self.broker_password = password
        self.logger = logging.getLogger(__name__)

        self.client = mqtt.Client(client_id=client_id)
        self.client.on_connect = self._on_connect
        self.client.on_message = self._on_message
        self.client.on_publish = self._on_publish

    def __enter__(self):
        if self.broker_username and self.broker_password:
            self.client.username_pw_set(self.broker_username, self.broker_password)
        self.client.connect(self.broker, self.port)

        self.client.loop_start()

        return self.client

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.client.loop_stop(force=True)

    def _on_connect(self, client, userdata, flags, rc):
        """
        The callback for when the client receives a CONNACK response from the server.

        :param client:
        :param userdata:
        :param flags:
        :param rc:
        """
        print("Connected with result code " + str(rc))

        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.
        # client.subscribe("$SYS/#")

    def _on_message(self, client, userdata, msg):
        """
        The callback for when a MESSAGE is received from the server.

        :param client:
        :param userdata:
        :param msg:
        """
        print(msg.topic + " " + str(msg.payload))

    def _on_publish(self, client, userata, mid):
        """
        The callback for when a PUBLISH message is sent to the server

        :param client:
        :param userata:
        :param mid:
        """
        print("mid: " + str(mid))
