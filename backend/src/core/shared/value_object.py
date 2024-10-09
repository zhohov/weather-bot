import abc
import dataclasses


@dataclasses.dataclass(frozen=True)
class ValueObject():
    @staticmethod
    @abc.abstractmethod
    def create(*args, **kwargs) -> 'ValueObject':
        raise NotImplementedError()
