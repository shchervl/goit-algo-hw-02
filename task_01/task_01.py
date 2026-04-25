import logging
import random
from queue import Full, Queue
from time import sleep

from utils import Request, Status

# ANSI color codes
_RESET  = "\033[0m"
_GREEN  = "\033[32m"
_CYAN   = "\033[36m"
_YELLOW = "\033[33m"
_RED    = "\033[31m"

_LOGGER_COLORS = {
    "producer": _GREEN,
    "consumer": _CYAN,
}


class ColorFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        color = _LOGGER_COLORS.get(record.name, "")
        if record.levelno >= logging.ERROR:
            color = _RED
        elif record.levelno >= logging.WARNING:
            color = _YELLOW
        return color + super().format(record) + _RESET


def _setup_logging() -> None:
    handler = logging.StreamHandler()
    handler.setFormatter(ColorFormatter(
        fmt="%(asctime)s  %(levelname)-8s  %(message)s",
        datefmt="%H:%M:%S",
    ))
    logging.root.setLevel(logging.INFO)
    logging.root.addHandler(handler)


_setup_logging()
log      = logging.getLogger(__name__)
producer = logging.getLogger("producer")
consumer = logging.getLogger("consumer")

# Tune these to simulate different load scenarios:
#
#   Queue overflow (ERROR logs appear):
#       MAX_PRODUCERS_AMOUNT > MAX_CONSUMERS_AMOUNT  e.g. producers=5, consumers=1
#
#   Stable balanced load (queue stays mid-size):
#       producers ≈ consumers  e.g. producers=3, consumers=3
#
#   Mostly empty queue (consumers drain faster than producers fill):
#       MIN_CONSUMERS_AMOUNT >> MAX_PRODUCERS_AMOUNT  e.g. producers=1, consumers=10

MAX_QUEUE_SIZE       = 20
MIN_PRODUCERS_AMOUNT = 1
MAX_PRODUCERS_AMOUNT = 5
MIN_CONSUMERS_AMOUNT = 3
MAX_CONSUMERS_AMOUNT = 20

queue: Queue[Request] = Queue(maxsize=MAX_QUEUE_SIZE)


def generate_request() -> None:
    req = Request()
    try:
        queue.put_nowait(req)
        producer.info("Generated request: %s  (queue size: %d)", req.id, queue.qsize())
    except Full:
        producer.error("Can't accept new request, please try later  (queue size: %d)", queue.qsize())


def process_request() -> None:
    if not queue.empty():
        request = queue.get()
        request.status = Status.RUNNING
        sleep(random.uniform(0.1, 0.3))
        request.status = Status.COMPLETED
        consumer.info("Processed request: %s  (queue size: %d)", request.id, queue.qsize())
        queue.task_done()
    else:
        consumer.warning("Queue is empty — no requests to process")


def emulate_requests_flow() -> None:
    for _ in range(random.randint(MIN_PRODUCERS_AMOUNT, MAX_PRODUCERS_AMOUNT)):
        generate_request()
    consumers_amount = MAX_CONSUMERS_AMOUNT if queue.qsize() > MAX_QUEUE_SIZE else MIN_CONSUMERS_AMOUNT
    for _ in range(random.randint(MIN_CONSUMERS_AMOUNT, consumers_amount)):
        process_request()
    sleep(0.3)


def main() -> None:
    log.info("Service center started. Press Ctrl+C to stop.")
    while True:
        try:
            emulate_requests_flow()
        except KeyboardInterrupt:
            log.info("Exiting.")
            break


if __name__ == "__main__":
    main()
