from abc import ABC, abstractmethod

from src.billing import EnergyType, EnergyCompany



class EnergySource(ABC):
    @abstractmethod
    def consume(self, amount, time_delta):
        pass

    @abstractmethod
    def get_voltage(self):
        pass


class Cable(EnergySource):

    def __init__(self, source: EnergySource):
        self.source = source
        self.efficiency = 1

    def consume(self, amount, time_delta):
        consumed_current = self.source.consume(amount/self.efficiency, time_delta)
        return consumed_current*self.efficiency

    def get_voltage(self):
        return self.source.get_voltage()


class Battery(EnergySource):

    def __init__(self):
        pass

    def consume(self, amount, time_delta):
        pass

    def get_voltage(self):
        pass


class Transformer(EnergySource):

    def __init__(self, source: EnergySource, voltage_ratio):
        self.voltage_current_ratio = voltage_ratio
        self.source = source
        self.efficiency = 1

    def consume(self, amount, time_delta):
        consumed_current_from_source = self.source.consume((amount*self.voltage_current_ratio)/self.efficiency, time_delta)
        return (consumed_current_from_source * self.efficiency) / self.voltage_current_ratio

    def get_voltage(self):
        return self.source.get_voltage() * self.voltage_current_ratio


class Catenary(EnergySource):

    def __init__(self, energy_company: EnergyCompany, voltage):
        self.voltage = voltage
        self.energy_company = energy_company
        self.efficiency = 1

    def consume(self, amount, time_delta):
        self.energy_company.consume((self.get_voltage()*amount)/self.efficiency, EnergyType.ELECTRICITY, .1)
        return amount

    def get_voltage(self):
        return self.voltage


class Pantograph(EnergySource):

    def __init__(self, catenary: Catenary):
        self.catenary = catenary
        self.efficiency = 1

    def consume(self, amount, time_delta):
        consumed_current = self.catenary.consume(amount / self.efficiency, time_delta)
        return consumed_current * self.efficiency

    def get_voltage(self):
        return self.catenary.get_voltage()


