# Phantom Year

The Phantom Year describes the mathematical discovery of a hidden year, each century, in which the Day = Year.

## Concept

In each century, there exists a special year where the **day of the year** (ordinal day 1-365/366) numerically matches the **last two digits of the year** itself. This is the "Phantom Year" - a hidden pattern where the day number and year digits align.

### Examples

- **Century 1900s**: Year **1901** → Day **1** (January 1)
- **Century 2000s**: Year **2001** → Day **1** (January 1) 
- **Year 1965**: Day **65** (March 6)
- **Year 2023**: Day **23** (January 23)

## Usage

### Running the Calculator

```bash
python phantomyear.py
```

### Using in Code

```python
from phantomyear import find_phantom_year, get_phantom_year_info

# Find the phantom year in a specific century
year, day, date = find_phantom_year(1900)
print(f"Phantom Year: {year}, Day: {day}, Date: {date}")

# Get detailed information about a specific year
info = get_phantom_year_info(1965)
print(f"Year {info['year']} - Day {info['day']}: {info['formatted']}")
```

## Running Tests

```bash
python -m unittest test_phantomyear.py -v
```

## Mathematical Discovery

The Phantom Year represents an elegant mathematical coincidence where temporal measurement aligns with numerical representation. Each century contains at least one such year where this alignment occurs, creating a hidden pattern in our calendar system.
