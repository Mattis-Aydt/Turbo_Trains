import unittest
from unittest.mock import patch
from src.train.electricity import Cable, Transformer, Pantograph, Catenary
from src.billing import EnergyType


class TestCable(unittest.TestCase):

    @patch('src.train.electricity.EnergySource')
    def test_consume_once(self, MockEnergySource):
        mock_source = MockEnergySource()
        mock_source.consume.return_value = 100
        cable = Cable(mock_source)

        result = cable.consume(100, .1)
        self.assertEqual(result, 100)
        mock_source.consume.assert_called_once_with(100, .1)

    @patch('src.train.electricity.EnergySource')
    def test_consume_with_energy_source_limit(self, MockEnergySource):
        mock_source = MockEnergySource()
        mock_source.consume.return_value = 50
        cable = Cable(mock_source)

        result = cable.consume(100, .1)
        self.assertEqual(result, 50)
        mock_source.consume.assert_called_once_with(100, .1)

    @patch('src.train.electricity.EnergySource')
    def test_consume_two_cables(self, MockEnergySource):
        mock_source = MockEnergySource()
        mock_source.consume.return_value = 200
        cable1 = Cable(mock_source)
        cable2 = Cable(cable1)
        cable1.efficiency = .5

        result = cable2.consume(100, .1)
        self.assertEqual(result, 100)
        mock_source.consume.assert_called_once_with(200, .1)


class TestTransformer(unittest.TestCase):

    @patch('src.train.electricity.EnergySource')
    def test_get_voltage(self, MockEnergySource):
        mock_source = MockEnergySource()
        mock_source.get_voltage.return_value = 2000
        transformer = Transformer(mock_source, 2)

        self.assertEqual(transformer.get_voltage(), 4000)

    @patch('src.train.electricity.EnergySource')
    def test_consume(self, MockEnergySource):
        mock_source = MockEnergySource()
        mock_source.consume.return_value = 60
        transformer = Transformer(mock_source, 2)

        result = transformer.consume(30, .1)
        self.assertEqual(result, 30)
        mock_source.consume.assert_called_once_with(60, .1)

    @patch('src.train.electricity.EnergySource')
    def test_consume_with_efficiency(self, MockEnergySource):
        mock_source = MockEnergySource()
        mock_source.consume.return_value = 120
        transformer = Transformer(mock_source, 2)
        transformer.efficiency = .5

        result = transformer.consume(30, .1)
        self.assertEqual(result, 30)
        mock_source.consume.assert_called_once_with(120, .1)


class TestPantograph(unittest.TestCase):

    @patch('src.train.electricity.Catenary')
    def test_get_voltage(self, MockEnergySource):
        mock_catenary = MockEnergySource()
        mock_catenary.get_voltage.return_value = 2000
        pantograph = Pantograph(mock_catenary)

        self.assertEqual(pantograph.get_voltage(), 2000)

    @patch('src.train.electricity.Catenary')
    def test_consume(self, MockCatenary):
        mock_catenary = MockCatenary()
        mock_catenary.consume.return_value = 30
        pantograph = Pantograph(mock_catenary)

        result = pantograph.consume(30, .1)
        self.assertEqual(result, 30)
        mock_catenary.consume.assert_called_once_with(30, .1)


class TestCatenary(unittest.TestCase):

    @patch('src.billing.EnergyCompany')
    def test_get_voltage(self, MockEnergyCompany):
        mock_EnergyCompany = MockEnergyCompany
        catenary = Catenary(mock_EnergyCompany, 2000)

        self.assertEqual(catenary.get_voltage(), 2000)

    @patch('src.train.electricity.EnergyCompany')
    def test_consume(self, MockEnergyCompany):
        mock_EnergyCompany = MockEnergyCompany()
        mock_EnergyCompany.consume.return_value = 150000
        catenary = Catenary(mock_EnergyCompany, 15000)

        result = catenary.consume(10, .1)
        self.assertEqual(result, 10)
        mock_EnergyCompany.consume.assert_called_once_with(150000, EnergyType.ELECTRICITY, .1)
