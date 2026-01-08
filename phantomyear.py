"""
Phantom Year Calculator

The Phantom Year describes the mathematical discovery of a hidden year, 
each century, in which the Day = Year.

In each century, there exists a special year where the day of the year 
(ordinal day 1-365/366) numerically matches the last digits of the year itself.
"""

from datetime import datetime, timedelta


def find_phantom_year(century_start):
    """
    Find the phantom year in a given century.
    
    The phantom year is the year where the day of the year equals
    the last two digits of the year (or the year modulo 100).
    
    Args:
        century_start: The starting year of the century (e.g., 1900, 2000)
        
    Returns:
        tuple: (year, day, date) - The phantom year, the day number, and the actual date
        
    Example:
        >>> find_phantom_year(1900)
        (1965, 65, datetime.datetime(1965, 3, 6, 0, 0))
    """
    for year in range(century_start, century_start + 100):
        # Get the last two digits of the year
        day_to_match = year % 100
        
        # Skip if day_to_match is 0 (would be invalid day)
        if day_to_match == 0:
            continue
            
        # Check if this day exists in the year (accounting for leap years)
        try:
            # Calculate the date for this day of the year
            jan_first = datetime(year, 1, 1)
            target_date = jan_first + timedelta(days=day_to_match - 1)
            
            # Verify this is still in the same year
            if target_date.year == year:
                return (year, day_to_match, target_date)
        except (ValueError, OverflowError):
            continue
    
    return None


def get_phantom_year_info(year):
    """
    Get information about a specific phantom year.
    
    Args:
        year: The year to check
        
    Returns:
        dict: Information about the phantom year including the day number and date
    """
    day_num = year % 100
    
    if day_num == 0:
        return None
        
    try:
        jan_first = datetime(year, 1, 1)
        target_date = jan_first + timedelta(days=day_num - 1)
        
        if target_date.year == year:
            return {
                'year': year,
                'day': day_num,
                'date': target_date,
                'formatted': target_date.strftime('%B %d, %Y'),
                'is_leap_year': year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
            }
    except (ValueError, OverflowError):
        pass
    
    return None


def list_phantom_years(start_century, end_century):
    """
    List all phantom years across multiple centuries.
    
    Args:
        start_century: Starting century (e.g., 1900)
        end_century: Ending century (e.g., 2100)
        
    Returns:
        list: List of tuples (year, day, date) for each phantom year found
    """
    phantom_years = []
    
    for century in range(start_century, end_century, 100):
        result = find_phantom_year(century)
        if result:
            phantom_years.append(result)
    
    return phantom_years


if __name__ == "__main__":
    # Example usage
    print("Phantom Year Calculator")
    print("=" * 50)
    print("\nThe Phantom Year is when the day of the year")
    print("equals the last two digits of the year itself.\n")
    
    # Find phantom years for several centuries
    centuries = [1900, 2000, 2100, 2200]
    
    for century in centuries:
        result = find_phantom_year(century)
        if result:
            year, day, date = result
            print(f"Century {century}s:")
            print(f"  Phantom Year: {year}")
            print(f"  Day of Year: {day}")
            print(f"  Date: {date.strftime('%B %d, %Y')}")
            print()
