[![Build Status](https://travis-ci.org/SilentFrogNet/silent_mqtt.svg?branch=master)](https://travis-ci.org/SilentFrogNet/silent_mqtt)
[![Coverage Status](https://coveralls.io/repos/github/SilentFrogNet/silent_mqtt/badge.svg?branch=master)](https://coveralls.io/github/SilentFrogNet/silent_mqtt?branch=master)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/f12f0230d5d14e3c917346b820e22250)](https://www.codacy.com/app/SilentFrogNet/silent_mqtt?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=SilentFrogNet/silent_mqtt&amp;utm_campaign=Badge_Grade)

# Silent MQTT

## What it is

**Silent MQTT** is a tiny MQTT interface for [Silent WoL](https://github.com/SilentFrogNet/silent_wol).

## How to install it

### What you need

 1. A working MQTT broker
    * Could be a Raspberry PI running `mosquitto`. See [here](configure_raspberry_as_broker) for details.
 
 2. IOTLink installed on the Windows machines you want to control, configured to work with the broker setup above. 

## How it works



# Support

##Configure Raspberry PI as Broker

To configure a Rasberry PI as a broker, follow this steps:

  * Update the Rasperry PI and install `mosquitto`
    
    ```shell script
      sudo apt update
      sudo apt install mosquitto mosquitto-clients
    ```
  
  * Enable the `mosquitto` broker
  
    ```shell script
      sudo systemctl enable mosquitto
    ```
    
  * That's done.

### Test it

You can test the broker as follows:

  1. Setup a subscriber connected to the broker on a specific topic
     
     ```shell script
       mosquitto_sub -h localhost -t "test/message"
     ```
     
  2. And then in another terminal window, try to publish a message on the same topic
     
     ```shell script
       mosquitto_pub -h localhost -t "test/message" -m "Hello, world"
     ```
  3. On the first terminal you should see that the message `Hello, world` is arrived.
