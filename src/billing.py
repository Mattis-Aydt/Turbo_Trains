from enum import Enum


class EnergyType(Enum):
    ELECTRICITY = 1


class EnergyCompany:

    def __init__(self):
        self.electricity_price = 0  # euroCent/kwh
        self.electricity_used = 0  # Joule

    def consume(self, amount, energy_type: EnergyType, time_delta):
        if not type(energy_type) == EnergyType:
            raise ValueError("energy_type has to be of type EnergyType")

        if energy_type == EnergyType.ELECTRICITY:
            self.electricity_used += amount * time_delta  # Watts * seconds = Joule

    def get_price(self, energy_type: EnergyType):
        if not type(energy_type) == EnergyType:
            raise ValueError("energy_type has to be of type EnergyType")

        if energy_type == EnergyType.ELECTRICITY:
            return (self.electricity_used / 3600000) * self.electricity_price  # Magic number can be replaced with converter in future


