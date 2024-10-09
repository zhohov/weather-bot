import pytest
from src.core.shared.entity import Entity
from src.core.shared.value_object import ValueObject

from src.core.logs.domain.entities import WeatherLog, TelegramUserID, UserCommand, BotAnswer


class TestWeatherLog:
    def test_create_weather_log(self) -> None:
        telegram_user_id = TelegramUserID.create(value="1234567")
        command = UserCommand.create(value="/weather Moscow")
        weather_answer = "Temperature: 12°C, Feels like: 10°C"
        answer = BotAnswer.create(value=weather_answer)
        log = WeatherLog(telegram_user_id=telegram_user_id, command=command, answer=answer)

        assert isinstance(log, WeatherLog)
        assert log.command.value == "/weather Moscow"
        assert log.telegram_user_id.value == "1234567"
        assert log.answer.value == weather_answer

    def test_create_weather_log_without_user_id(self) -> None:
        command = UserCommand.create(value="/weather Moscow")
        
        weather_answer = "Temperature: 12°C, Feels like: 10°C"
        answer = BotAnswer.create(value=weather_answer)

        with pytest.raises(ValueError):
            WeatherLog(command=command, answer=answer)

    def test_create_weather_log_without_answer(self) -> None:
        telegram_user_id = TelegramUserID.create(value="1234567")
        command = UserCommand.create(value="/weather Moscow")

        with pytest.raises(ValueError):
            WeatherLog(telegram_user_id=telegram_user_id, command=command)


class TestUser:
    def test_create_user(self) -> None:
        ...

    def test_create_user_without_telegram_id(self) -> None:
        ...
