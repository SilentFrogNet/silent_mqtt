from mqtt.core.smqtt import SilentMQTT


class IOTLinkTopics:
    class Commands:
        BASE_COMMAND = '{prefix}/{domain}/{device_name}/commands'

        SHUTDOWN = f'{BASE_COMMAND}/shutdown'
        REBOOT = f'{BASE_COMMAND}/reboot'
        SUSPEND = f'{BASE_COMMAND}/suspend'

        LOGOFF = f'{BASE_COMMAND}/logoff'  # Payload: username (or empty for all current users)
        LOCK = f'{BASE_COMMAND}/lock'  # Payload: username (or empty for all current users)

        VOLUME = f'{BASE_COMMAND}/volume/set'  # Payload: 0-100
        MUTE = f'{BASE_COMMAND}/volume/mute'  # Payload: true/false/empty (toggle)
        MEDIA_PLAYPAUSE = f'{BASE_COMMAND}/media/playpause'
        MEDIA_STOP = f'{BASE_COMMAND}/media/stop'
        MEDIA_NEXT = f'{BASE_COMMAND}/media/next'
        MEDIA_PREVIOUS = f'{BASE_COMMAND}/media/previous'

        TURN_DISPLAY_ON = f'{BASE_COMMAND}/displays/on'
        TURN_DISPLAY_OFF = f'{BASE_COMMAND}/displays/off'

        SEND_KEYS = f'{BASE_COMMAND}/send-keys'  # Payload: JSON -> List of keys. https://docs.microsoft.com/en-us/dotnet/api/system.windows.forms.sendkeys?view=netframework-4.8

        RUN = f'{BASE_COMMAND}/run'  # Payload: JSON
        NOTIFY = f'{BASE_COMMAND}/notify'  # Payload: JSON

    class WindowsMonitor:
        BASE_COMMAND = '{prefix}/{domain}/{device_name}/windows-monitor/stats/'

        LWT = '{prefix}/{domain}/{device_name}/lwt/'  # Payload: ON/OFF
        POWER_STATUS = f'{BASE_COMMAND}/power/status'  # Payload: ON/OFF
        BATTERY_STATUS = f'{BASE_COMMAND}/battery/status'  # Payload: ON/OFF


class SilentEvents(object):
    """ A wrapper class to manage devices through MQTT messages """

    def __init__(self, broker, port=1883, username=None, password=None, prefix='iotlink'):
        self.smqtt = SilentMQTT(broker, port=port, username=username, password=password)
        self.prefix = prefix

    def send_sol_packet(self, *devs, **kwargs):
        """
        Sends MQTT shutdown message to the broker

        :param devs: the list o devices to shutdown
        :param kwargs['action']: if provided will change the command to send to the device. Allowed values are "suspend", "reboot", "shutdown"
        """
        topic = IOTLinkTopics.Commands.SHUTDOWN
        if 'action' in kwargs:
            if kwargs['action'] == 'suspend':
                topic = IOTLinkTopics.Commands.SUSPEND
            elif kwargs['action'] == 'reboot':
                topic = IOTLinkTopics.Commands.REBOOT

        with self.smqtt as client:
            for dev in devs:
                client.publish(topic.format(
                    prefix=self.prefix,
                    domain=dev['domain'],
                    device_name=dev['name']
                ))

    def send_mute(self, dev, action=None, **kwargs):
        """
        Sends MQTT mute message to the broker

        :param dev: the device to mute/unmute
        :param action: could be 'true', 'false', None. If None will toggle the status.
        """
        if action not in ['true', 'false', None]:
            action = None

        with self.smqtt as client:
            client.publish(
                IOTLinkTopics.Commands.MUTE.format(
                    prefix=self.prefix,
                    domain=dev['domain'],
                    device_name=dev['name']
                ),
                payload=action
            )

    def send_media_playpause(self, dev):
        """
        Sends MQTT play/pause message to the broker

        :param dev: the device to manage
        """

        with self.smqtt as client:
            client.publish(
                IOTLinkTopics.Commands.MEDIA_PLAYPAUSE.format(
                    prefix=self.prefix,
                    domain=dev['domain'],
                    device_name=dev['name']
                )
            )
