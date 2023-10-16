import unittest
import numpy as np
from tires.carrigan_tires import CarriganTires


class TestCarriganTires(unittest.TestCase):
    def test_needs_service_true(self):
        worn = np.array([0.1, 0.1, 0.5, 0.9])
        tires = CarriganTires(worn)
        self.assertTrue(tires.needs_service())

    def test_needs_service_false(self):
        tire_wear = np.array([0.1, 0.2, 0.2, 0.1])
        tires = CarriganTires(tire_wear)
        self.assertFalse(tires.needs_service())
