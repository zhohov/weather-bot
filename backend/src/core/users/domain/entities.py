from typing import Set

from src.core.shared.domain.entities import Entity
from src.core.shared.domain.value_objects import TelegramUserID
from src.core.logs.domain.entities import WeatherLog


class TelegramUser(Entity):
    def __init__(self, telegram_user_id: TelegramUserID) -> None:
        super().__init__()
        self.telegram_user_id = telegram_user_id
        self.logs: Set[WeatherLog] = set()

    def add_log(self, log: WeatherLog) -> None:
        self.logs.add(log)
