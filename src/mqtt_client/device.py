import datetime
import random
import uuid

from pydantic import BaseModel, Field


class SmartRefrigeratorMessage(BaseModel):
    id: uuid.UUID
    refrigerator_temp: float
    freezer_temp: float
    timestamp: datetime.datetime = Field(
        default_factory=lambda: datetime.datetime.now(datetime.timezone.utc)
    )


class SmartRefrigerator:
    def __init__(
        self,
        min_refrigerator_temp: float = 2,
        max_refrigerator_temp: float = 5,
        max_refrigerator_temp_change: float = 0.5,
        min_freezer_temp: float = -20,
        max_freezer_temp: float = -16,
        max_freezer_temp_change: float = 0.5,
    ):
        self.min_refrigerator_temp = min_refrigerator_temp
        self.max_refrigerator_temp = max_refrigerator_temp
        self.max_refrigerator_temp_change = max_refrigerator_temp_change
        self.min_freezer_temp = min_freezer_temp
        self.max_freezer_temp = max_freezer_temp
        self.max_freezer_temp_change = max_freezer_temp_change
        self.refrigerator_temp = random.uniform(
            min_refrigerator_temp, max_refrigerator_temp
        )
        self.freezer_temp = random.uniform(min_freezer_temp, max_freezer_temp)
        self.device_id = uuid.uuid4()

    def _random_change(
        self, val: float, min_val: float, max_val: float, max_change: float
    ) -> float:
        change = random.uniform(-max_change, max_change)
        return min(max(val + change, min_val), max_val)

    def _update_temperatures(self):
        self.refrigerator_temp = self._random_change(
            self.refrigerator_temp,
            self.min_refrigerator_temp,
            self.max_refrigerator_temp,
            self.max_refrigerator_temp_change,
        )
        self.freezer_temp = self._random_change(
            self.freezer_temp,
            self.min_freezer_temp,
            self.max_freezer_temp,
            self.max_freezer_temp_change,
        )

    def __iter__(self):
        return self

    def __next__(self) -> SmartRefrigeratorMessage:
        self._update_temperatures()
        message = SmartRefrigeratorMessage(
            id=self.device_id,
            refrigerator_temp=self.refrigerator_temp,
            freezer_temp=self.freezer_temp,
        )
        return message
