import time
import random
from queue import Queue # import for type hinting

USE_MOCK_DATA = True

def fetch_data(data_queue: Queue):
    if USE_MOCK_DATA:
        _fetch_mock_data(data_queue)
    else:
        _fetch_real_serial_data(data_queue)

def _fetch_mock_data(data_queue: Queue):
    while True:
        time.sleep(0.5)
        payload = {
            "speed":random.uniform(-10,10),
            "rpm": random.uniform(20,25)
        }
        data_queue.put(payload)

def _fetch_real_serial_data(data_queue: Queue):
    # to be implemented later
    pass