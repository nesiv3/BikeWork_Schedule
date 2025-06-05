import pytest
from datetime import datetime
from zoneinfo import ZoneInfo
from unittest.mock import AsyncMock, MagicMock

from application.schedule.commands.update_schedule import UpdateScheduleCommand, UpdateScheduleHandler
from application.schedule.schedule_update_dto import ScheduleDTO
from domain.models.user import User
from domain.models.store import Store

@pytest.mark.asyncio
async def test_update_schedule_handler_updates_main_fields():
    # Arrange
    fake_uow = MagicMock()
    fake_uow.__aenter__ = AsyncMock(return_value=fake_uow)
    fake_uow.__aexit__ = AsyncMock(return_value=None)
    fake_uow.schedule_repository.update = AsyncMock()

    user = User(id="1", full_name="Test User", email="user@example.com", phone_number="123")
    store = Store(id=1, name="Test Store", email="store@example.com", phone="123", address="Test Address")
    dto = ScheduleDTO(
        date=datetime(2024, 6, 1, 10, 0, tzinfo=ZoneInfo("America/Bogota")),
        period="AM",
        maintenance_type=1,
        status="pending",
        observation="Test observation",
        cost=100.0,
        estimated_time_minutes=60,
        user=user,
        store=store,
        created_at=datetime(2024, 5, 1, 10, 0, tzinfo=ZoneInfo("America/Bogota")),
        updated_at=datetime(2024, 5, 1, 10, 0, tzinfo=ZoneInfo("America/Bogota")),
    )
    command = UpdateScheduleCommand("fake_id", dto)
    handler = UpdateScheduleHandler(fake_uow)

    # Act
    await handler.handle(command)

    # Assert
    fake_uow.schedule_repository.update.assert_awaited_once()
    args, kwargs = fake_uow.schedule_repository.update.call_args
    assert args[0] == "fake_id"
    updated_schedule = args[1]
    assert updated_schedule.date == dto.date
    assert updated_schedule.maintenance_type == dto.maintenance_type
    assert updated_schedule.status == dto.status
    assert updated_schedule.observation == dto.observation
    assert updated_schedule.cost == dto.cost
    assert updated_schedule.estimated_time_minutes == dto.estimated_time_minutes

@pytest.mark.asyncio
async def test_update_schedule_handler_does_not_modify_user_or_store():
    # Arrange
    fake_uow = MagicMock()
    fake_uow.__aenter__ = AsyncMock(return_value=fake_uow)
    fake_uow.__aexit__ = AsyncMock(return_value=None)
    fake_uow.schedule_repository.update = AsyncMock()

    user = User(id="1", full_name="Test User", email="user@example.com", phone_number="123")
    store = Store(id=1, name="Test Store", email="store@example.com", phone="123", address="Test Address")
    dto = ScheduleDTO(
        date=datetime(2024, 6, 1, 10, 0, tzinfo=ZoneInfo("America/Bogota")),
        period="AM",
        maintenance_type=1,
        status="pending",
        observation="Test observation",
        cost=100.0,
        estimated_time_minutes=60,
        user=user,
        store=store,
        created_at=datetime(2024, 5, 1, 10, 0, tzinfo=ZoneInfo("America/Bogota")),
        updated_at=datetime(2024, 5, 1, 10, 0, tzinfo=ZoneInfo("America/Bogota")),
    )
    command = UpdateScheduleCommand("fake_id", dto)
    handler = UpdateScheduleHandler(fake_uow)

    # Act
    await handler.handle(command)

    # Assert
    args, kwargs = fake_uow.schedule_repository.update.call_args
    updated_schedule = args[1]
    assert updated_schedule.user == user
    assert updated_schedule.store == store