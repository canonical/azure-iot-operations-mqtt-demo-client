import argparse
import sys
import time

import paho.mqtt.client as mqtt

from mqtt_client.device import SmartRefrigerator


def get_mqtt_client(
    host: str,
    port: int,
    username: str,
    password: str,
    cert_file: str,
    key_file: str,
    ca_file: str,
):
    # Create client instance
    client = mqtt.Client(transport="tcp")

    # Set client username and password
    if username:
        client.username_pw_set(username, password)

    # Set broker and client certificates
    client.tls_set(ca_certs=ca_file, certfile=cert_file, keyfile=key_file)

    # Connect to broker
    client.connect(host=host, port=port)
    return client


def define_argument_parser():
    parser = argparse.ArgumentParser(description="MQTT demo client")
    parser.add_argument("--host", type=str, required=True, help="broker host")
    parser.add_argument("--port", type=int, required=True, help="broker port")
    parser.add_argument("--username", type=str, help="client username")
    parser.add_argument("--password", type=str, help="client password")
    parser.add_argument("--cert-file", type=str, help="client certificate file")
    parser.add_argument("--key-file", type=str, help="client key file")
    parser.add_argument("--ca-file", type=str, help="broker CA certificate file")
    return parser


def main():
    parser = define_argument_parser()
    args = parser.parse_args()
    print(args)

    client = get_mqtt_client(
        args.host,
        args.port,
        args.username,
        args.password,
        args.cert_file,
        args.key_file,
        args.ca_file,
    )

    # Get smart refrigerator instance
    smart_refrigerator = SmartRefrigerator()

    # Define topic
    topic = "smart-refrigerator"

    # Simulate data streaming
    try:
        while True:
            message = next(smart_refrigerator)
            client.publish(topic, message.model_dump_json(), 0)
            print(f"Published on topic: {topic} message: {message}")
            time.sleep(5)
    except KeyboardInterrupt:
        sys.exit()


if __name__ == "__main__":
    main()
