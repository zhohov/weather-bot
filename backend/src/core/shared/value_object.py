import abc
import dataclasses


@dataclasses.dataclass(frozen=True)
class ValueObject():
    @abc.abstractmethod
    @staticmethod
    def create() -> 'ValueObject':
        raise NotImplementedError()
