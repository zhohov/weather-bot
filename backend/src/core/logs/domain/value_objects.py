import dataclasses

from src.core.shared.value_object import ValueObject


@dataclasses.dataclass(frozen=True)
class Name(ValueObject):
    value: str

    @staticmethod
    def create(value) -> 'Name':
        return Name(value=value)


@dataclasses.dataclass(frozen=True)
class TelegramUserID(ValueObject):
    value: int

    @staticmethod
    def create(value: int) -> 'TelegramUserID':
        return TelegramUserID(value=value)


@dataclasses.dataclass(frozen=True)
class UserCommand(ValueObject):
    value: str

    @staticmethod
    def create(value: str) -> 'UserCommand':
        return UserCommand(value=value) 


@dataclasses.dataclass(frozen=True)
class BotAnswer(ValueObject):
    value: str

    @staticmethod
    def create(value: str) -> 'BotAnswer':
        return BotAnswer(value=value)

