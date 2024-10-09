import abc
import uuid


class Entity(abc.ABC):
    def __init__(self) -> None:
        self.id = uuid.uuid4()

