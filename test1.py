import unittest
from bmi_calculator import calculate_bmi

class TestBMICalculator(unittest.TestCase):
    def test_bmi_calculation(self):
        # Test cases with known results
        test_cases = [
            (160, 50, 19.53),
            (170, 75, 25.95),
            (180, 90, 27.78),
        ]
        
        for height, weight, expected_bmi in test_cases:
            calculated_bmi = calculate_bmi(height, weight)
            self.assertAlmostEqual(calculated_bmi, expected_bmi, delta=0.01)

if __name__ == "__main__":
    unittest.main()
