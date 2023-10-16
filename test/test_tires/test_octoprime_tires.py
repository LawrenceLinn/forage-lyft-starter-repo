import unittest
import numpy as np
from tires.octoprime_tires import OctoprimeTires


class TestOctoprimeTires(unittest.TestCase):
    def test_needs_service_true(self):
        tire_wear = np.array([0.9, 0.9, 0.9, 0.9])
        tires = OctoprimeTires(tire_wear)
        self.assertTrue(tires.needs_service())

    def test_needs_service_false(self):
        tire_wear = np.array([0.1, 0.1, 0.1, 0.1])
        tires = OctoprimeTires(tire_wear)
        self.assertFalse(tires.needs_service())


if __name__ == "__main__":
    unittest.main()
