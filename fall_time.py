import math
import constants.py


# This script finds the time in seconds to drop from a height on some planets.
# You have to complete/fix the code given below.

# How would you import the constants file here?
# How would you import the math module here?
height = int(input('Height in meters: '))  # Meters from planet

# How would you use the constants for Mars and Earth to print out time values?
if __name__ == '__main__':
    print('Earth:', math.sqrt(2 * height / earth_g), 'seconds')
    print('Mars:', math.sqrt(2 * height / mars_g), 'seconds')
