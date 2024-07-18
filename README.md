# azure-iot-operations-mqtt-demo-client
MQTT demo client for Azure IoT Operations

## Development

```shell
# Build snap
$ snapcraft

# Install snap
$ snap install azure-iot-operations-mqtt-demo-client_0.1_amd64.snap --dangerous

# Install mosquitto
$ snap install mosquitto

# Listen for messages
$ mosquitto_sub --topic smart-refrigerator --debug

# Run mqtt producer
$ azure-iot-operations-mqtt-demo-client.mqtt-producer
```

## Snap configuration

```shell
# Get configuration
$ snap get azure-iot-operations-mqtt-demo-client -d

# Update broker port
$ snap set azure-iot-operations-mqtt-demo-client broker.port=8883

# Update broker CA certificates
$ snap set azure-iot-operations-mqtt-demo-client broker.ca="$(cat ca.crt)"

# All configuration options listed on snap/hooks/configure
```