from dataclasses import dataclass, field
from enum import StrEnum, auto


class ConnectivityStatus(StrEnum):
    ONLINE = auto()
    OFFLINE = auto()
    LIMITED = "Limited Connectivity"


@dataclass
class IoTDevice:
    name: str
    device_type: str
    connectivity: ConnectivityStatus
    sensors: list[str] = field(default_factory=list)
    location: str = "Unknown"
    firmware_version: int = 1

    def add_sensor(self, sensor_name: str):
        """Add a new sensor to the device."""
        self.sensors.append(sensor_name)
