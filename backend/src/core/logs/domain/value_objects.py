import dataclasses

from src.core.shared.value_object import ValueObject


@dataclasses.dataclass(frozen=True)
class Name(ValueObject):
    value: str

    @staticmethod
    def create(value) -> 'Name':
        return Name(value=value)
