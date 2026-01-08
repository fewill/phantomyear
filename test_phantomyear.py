"""
Tests for Phantom Year Calculator
"""

import unittest
from datetime import datetime
from phantomyear import find_phantom_year, get_phantom_year_info, list_phantom_years


class TestPhantomYear(unittest.TestCase):
    
    def test_find_phantom_year_1900s(self):
        """Test finding phantom year in the 1900s century."""
        result = find_phantom_year(1900)
        self.assertIsNotNone(result)
        year, day, date = result
        
        # The phantom year should be 19XX where XX is a valid day number
        self.assertTrue(1900 <= year < 2000)
        self.assertEqual(day, year % 100)
        self.assertEqual(date.year, year)
    
    def test_find_phantom_year_2000s(self):
        """Test finding phantom year in the 2000s century."""
        result = find_phantom_year(2000)
        self.assertIsNotNone(result)
        year, day, date = result
        
        # The phantom year should be 20XX where XX is a valid day number
        self.assertTrue(2000 <= year < 2100)
        self.assertEqual(day, year % 100)
        self.assertEqual(date.year, year)
    
    def test_phantom_year_day_matches_year_digits(self):
        """Test that the day of year matches the last digits of the year."""
        result = find_phantom_year(1900)
        year, day, date = result
        
        # Day should equal last two digits of year
        self.assertEqual(day, year % 100)
        
        # Calculate day of year from date
        jan_first = datetime(year, 1, 1)
        day_of_year = (date - jan_first).days + 1
        self.assertEqual(day_of_year, day)
    
    def test_get_phantom_year_info(self):
        """Test getting information about a specific phantom year."""
        # Test with year 1965 (day 65)
        info = get_phantom_year_info(1965)
        self.assertIsNotNone(info)
        self.assertEqual(info['year'], 1965)
        self.assertEqual(info['day'], 65)
        self.assertEqual(info['date'].year, 1965)
        self.assertIn('formatted', info)
        self.assertIn('is_leap_year', info)
    
    def test_get_phantom_year_info_invalid(self):
        """Test with a year where last digits are 00."""
        info = get_phantom_year_info(1900)
        self.assertIsNone(info)
        
        info = get_phantom_year_info(2000)
        self.assertIsNone(info)
    
    def test_list_phantom_years(self):
        """Test listing phantom years across multiple centuries."""
        phantom_years = list_phantom_years(1900, 2200)
        
        # Should have phantom years for multiple centuries
        self.assertGreater(len(phantom_years), 0)
        
        # Each entry should be a valid tuple
        for year, day, date in phantom_years:
            self.assertEqual(day, year % 100)
            self.assertEqual(date.year, year)
    
    def test_phantom_year_consistency(self):
        """Test that the phantom year calculation is consistent."""
        result1 = find_phantom_year(1900)
        result2 = find_phantom_year(1900)
        
        self.assertEqual(result1, result2)
    
    def test_different_centuries_different_years(self):
        """Test that different centuries have different phantom years."""
        result_1900 = find_phantom_year(1900)
        result_2000 = find_phantom_year(2000)
        
        self.assertIsNotNone(result_1900)
        self.assertIsNotNone(result_2000)
        
        year_1900, _, _ = result_1900
        year_2000, _, _ = result_2000
        
        # Different centuries should give different years
        self.assertNotEqual(year_1900, year_2000)


if __name__ == '__main__':
    unittest.main()
