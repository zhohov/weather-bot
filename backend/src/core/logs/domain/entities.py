from datetime import datetime

from src.core.shared.domain.entities import Entity
from src.core.shared.domain.value_objects import TelegramUserID
from src.core.logs.domain.value_objects import BotAnswer, UserCommand


class WeatherLog(Entity):
    def __init__(self, telegram_user_id: TelegramUserID, command: UserCommand, answer: BotAnswer) -> None:
        super().__init__()
        self.telegram_user_id = telegram_user_id
        self.command = command
        self.answer = answer
        self.created = self.get_current_time()

    def get_current_time(self, ) -> datetime:
        return datetime.now().replace(microsecond=0)

