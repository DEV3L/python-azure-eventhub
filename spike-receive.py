import time

from azure.eventhub import EventHubClient, Offset

from utils.env import env
from utils.logging_service import LoggingService

logger = LoggingService('Receive').logger

CONNECTION_STRING = env('EVENT_HUB_CONNECTION_STRING')
EVENT_HUB_TOPIC = env('EVENT_HUB_TOPIC_HELLO_WORLD_NAME')
EVENT_HUB_PARTITION = env('EVENT_HUB_TOPIC_HELLO_WORLD_PARTITION')

CONSUMER_GROUP = "$default"
PREFETCH = 300
OFFSET = Offset(-1, inclusive=True)


def receive():
    client, receiver = build_receiver_client()

    total = 0
    start_time = time.time()

    for event_data in receiver.receive(timeout=1000):
        offset = event_data.offset
        sequence_number = event_data.sequence_number
        message = event_data.message

        logger.info(f"Received:{offset}|{sequence_number}-Message:{message}")
        total += 1

    end_time = time.time()

    client.stop()
    run_time = end_time - start_time
    logger.info(f"Received {total} messages in {run_time} seconds")

    client.stop()


def build_receiver_client():
    client = EventHubClient.from_connection_string(CONNECTION_STRING, EVENT_HUB_TOPIC)
    receiver = client.add_receiver(CONSUMER_GROUP, EVENT_HUB_PARTITION, prefetch=PREFETCH, offset=OFFSET)
    client.run()
    return client, receiver


if __name__ == "__main__":
    if not CONNECTION_STRING:
        raise ValueError("No EventHubs URL supplied.")

    receive()
