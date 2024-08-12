
# Function to convert pounds to kilograms
def pounds_to_kg(pounds):
    return pounds * 0.453592

# Function to convert feet to centimeters
def feet_to_cm(feet):
    return feet * 30.48

# Main function to get user input and display the conversion
def main():
    # Input: weight in pounds and height in feet
    weight_lbs = float(input("Enter weight in pounds: "))
    height_ft = float(input("Enter height in feet: "))
    
    # Convert to kilograms and centimeters
    weight_kg = pounds_to_kg(weight_lbs)
    height_cm = feet_to_cm(height_ft)
    
    # Output: weight and height in the new units
    print(f"Weight in kilograms: {weight_kg:.2f} kg")
    print(f"Height in centimeters: {height_cm:.2f} cm")

# Run the main function
if __name__ == "__main__":
    main()
