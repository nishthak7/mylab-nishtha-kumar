# Import the constants file and math module
import math
from constants import earth_g, mars_g

height = float(input('Height in meters: '))  # Meters from planet (now allows decimals)

# Calculate and print out time values for Earth and Mars, rounded to two decimal places
if __name__ == '__main__':
    print(f'Earth: {math.sqrt(2 * height / earth_g):.2f} seconds')
    print(f'Mars: {math.sqrt(2 * height / mars_g):.2f} seconds')