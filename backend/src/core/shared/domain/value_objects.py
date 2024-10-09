import abc
import dataclasses


@dataclasses.dataclass(frozen=True)
class ValueObject():
    @staticmethod
    @abc.abstractmethod
    def create(*args, **kwargs) -> 'ValueObject':
        raise NotImplementedError()


@dataclasses.dataclass(frozen=True)
class TelegramUserID(ValueObject):
    value: int

    @staticmethod
    def create(value: int) -> 'TelegramUserID':
        if not value:
            raise ValueError()
        return TelegramUserID(value=value)
