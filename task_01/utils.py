import random
import string
import uuid
from enum import Enum


class Status(Enum):
    PENDING = 1
    RUNNING = 2
    COMPLETED = 3


class Request:
    def __init__(self):
        self.id = uuid.uuid4()
        self.title = _random_string(20)
        self.description = _random_string(200)
        self.status = Status.PENDING


def _random_string(length: int) -> str:
    chars = string.ascii_letters + string.digits
    return "".join(random.choice(chars) for _ in range(length))
