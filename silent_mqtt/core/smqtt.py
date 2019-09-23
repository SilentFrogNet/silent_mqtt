import logging

import paho.mqtt.client as mqtt

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


class SilentMQTT(object):
    """ The MQTT <-> Eventghost wrapper """

    def __init__(self, broker, port=1883, keepalive=60):
        self.broker = broker
        self.port = port
        self.keepalive = keepalive
        self.logger = logging.getLogger(__name__)

        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

    def start(self):
        self.client.connect(self.broker, self.port, self.keepalive)  # "iot.eclipse.org", 1883

        # Blocking call that processes network traffic, dispatches callbacks and
        # handles reconnecting.
        # Other loop*() functions are available that give a threaded interface and a
        # manual interface.
        self.client.loop_forever()

    def on_connect(self, client, userdata, flags, rc):
        """
        The callback for when the client receives a CONNACK response from the server.

        :param client:
        :param userdata:
        :param flags:
        :param rc:
        """
        self.logger.info("Connected with result code " + str(rc))

        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.
        client.subscribe("$SYS/#")

    def on_message(self, client, userdata, msg):
        """
        The callback for when a PUBLISH message is received from the server.

        :param client:
        :param userdata:
        :param msg:
        """
        self.logger.info(msg.topic + " " + str(msg.payload))

    def send_sol_packet(self, *macs, **kwargs):
        """
        Sends MQTT shutdown message to the brocker

        :param macs: the mac addresses to shutdown
        """
        for mac in macs:
            # send a MQTT message to Eventghost/IOTLink to shutdown PC
            pass
