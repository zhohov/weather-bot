import dataclasses

from src.core.shared.domain.value_objects import ValueObject


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

