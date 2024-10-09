import pytest
from src.core.shared.domain.value_objects import ValueObject, TelegramUserID
from src.core.logs.domain.value_objects import UserCommand, BotAnswer


class TestTelegramUserID:
    def test_create_telegram_user_id(self) -> None:
        telegram_user_id = TelegramUserID.create(value=1234567)

        assert isinstance(telegram_user_id, TelegramUserID)
        assert telegram_user_id.value == 1234567

    def test_create_telegram_user_id_without_value(self) -> None:
        with pytest.raises(ValueError):
            telegram_user_id = TelegramUserID.create(value=None)


class TestUserCommand:
    def test_create_telegram_user_id(self) -> None:
        command = UserCommand.create(value="/weather Moscow")

        assert isinstance(command, UserCommand)
        assert command.value == "/weather Moscow"

    def test_create_telegram_user_id_without_value(self) -> None:
        with pytest.raises(ValueError):
            command = UserCommand.create(value="")


class TestBotAnswer:
    def test_create_telegram_user_id(self) -> None:
        weather_answer = "Temperature: 12°C, Feels like: 10°C"
        answer = BotAnswer.create(value=weather_answer)

        assert isinstance(answer, BotAnswer)
        assert answer.value == weather_answer

    def test_create_telegram_user_id_without_value(self) -> None:
        with pytest.raises(ValueError):
            answer = BotAnswer.create(value="")



