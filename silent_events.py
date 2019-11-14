from mqtt.core.smqtt import SilentMQTT


class IOTLinkTopics(object):
    BASE_COMMAND = 'iotlink/{domain}/{device_name}/commands'
    SHUTDOWN = f'{BASE_COMMAND}/shutdown'
    REBOOT = f'{BASE_COMMAND}/reboot'
    SUSPEND = f'{BASE_COMMAND}/suspend'
    MUTE = f'{BASE_COMMAND}/volume/mute'


class SilentEvents(object):
    """ A wrapper class to manage devices through MQTT messages """

    def __init__(self, broker, port=1883, username=None, password=None):
        self.smqtt = SilentMQTT(broker, port=port, username=username, password=password)

    def send_sol_packet(self, *devs, **kwargs):
        """
        Sends MQTT shutdown message to the broker

        :param devs: the list o devices to shutdown
        :param kwargs['action']: if provided will change the command to send to the device. Allowed values are "suspend", "reboot", "shutdown"
        """
        topic = IOTLinkTopics.SHUTDOWN
        if 'action' in kwargs:
            if kwargs['action'] == 'suspend':
                topic = IOTLinkTopics.SUSPEND
            elif kwargs['action'] == 'reboot':
                topic = IOTLinkTopics.REBOOT

        with self.smqtt as client:
            for dev in devs:
                client.publish(topic.format(
                    domain=dev['domain'],
                    device_name=dev['name']
                ))

    def send_mute(self, dev, action=None):
        """
        Seds MQTT mute message to the broker

        :param dev: the device to mute/unmute
        :param action: could be 'true', 'false', None. If None will toggle the status.
        """
        if action not in ['true', 'false', None]:
            action = None

        with self.smqtt as client:
            client.publish(
                IOTLinkTopics.MUTE.format(
                    domain=dev['domain'],
                    device_name=dev['name']
                ),
                payload=action
            )
