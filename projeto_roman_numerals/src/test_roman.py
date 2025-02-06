import unittest
from main import int_to_roman

class TestRomanNumerals(unittest.TestCase):
    def test_single_digits(self):
        test_cases = {1: "I", 2: "II", 3: "III", 4: "IV", 5: "V"}
        for num, expected in test_cases.items():
            with self.subTest(num=num):
                self.assertEqual(int_to_roman(num), expected)
    
    def test_double_digits(self):
        test_cases = {9: "IX", 10: "X", 14: "XIV", 19: "XIX", 20: "XX"}
        for num, expected in test_cases.items():
            with self.subTest(num=num):
                self.assertEqual(int_to_roman(num), expected)
    
    def test_higher_numbers(self):
        test_cases = {
            40: "XL", 50: "L", 90: "XC", 100: "C", 400: "CD", 500: "D",
            900: "CM", 1000: "M", 1987: "MCMLXXXVII", 3999: "MMMCMXCIX"
        }
        for num, expected in test_cases.items():
            with self.subTest(num=num):
                self.assertEqual(int_to_roman(num), expected)

    def test_edge_cases(self):
        test_cases = {3998: "MMMCMXCVIII", 44: "XLIV", 99: "XCIX", 2024: "MMXXIV"}
        for num, expected in test_cases.items():
            with self.subTest(num=num):
                self.assertEqual(int_to_roman(num), expected)

if __name__ == "__main__":
    unittest.main()
