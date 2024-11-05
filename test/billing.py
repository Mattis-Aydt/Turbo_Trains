import unittest
from unittest.mock import patch
from src.billing import EnergyCompany, EnergyType


class TestEnergyCompany(unittest.TestCase):
    def test_consume_once(self):
        energyCompany = EnergyCompany()
        energyCompany.electricity_price = 32  # 1cent/kwh
        energyCompany.consume(1000, energy_type=EnergyType.ELECTRICITY, time_delta=3600)  # Consuming 1kw for 1h
        self.assertEqual(energyCompany.get_price(EnergyType.ELECTRICITY), 32)
