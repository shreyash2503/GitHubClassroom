from bmi_calculator import calculate_bmi

def test_calculate_bmi():
    # Test cases with known results
    test_cases = [
        (160, 50, 19.53),
        (170, 75, 25.95),
        (180, 90, 27.78),
    ]
    
    for height, weight, expected_bmi in test_cases:
        calculated_bmi = calculate_bmi(height, weight)
        assert abs(calculated_bmi - expected_bmi) < 0.01  # Allow for a small difference due to floating-point precision

# Run the tests when the script is executed
if __name__ == "__main__":
    import pytest
    pytest.main()

