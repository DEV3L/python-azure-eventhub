import time

from azure.eventhub import EventHubClient, EventData

from utils.env import env
from utils.logging_service import LoggingService

logger = LoggingService('Send').logger

CONNECTION_STRING = env('EVENT_HUB_CONNECTION_STRING')

message = "Hello, World!"

if not CONNECTION_STRING:
    raise ValueError("No EventHubs URL supplied.")

client = EventHubClient.from_connection_string(CONNECTION_STRING, "hello")
sender = client.add_sender()
client.run()

start_time = time.time()

try:
    logger.info(f"Sending message: {message}")
    sender.send(EventData(message))
except:
    raise
finally:
    end_time = time.time()
    client.stop()
    run_time = end_time - start_time
    logger.info("Runtime: {} seconds".format(run_time))
