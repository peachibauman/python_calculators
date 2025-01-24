def height_conversion(feet, inches):
    total_inches = (feet * 12) + inches
    return total_inches

feet = int(input("Enter feet: "))
inches = int(input("Enter inches: "))

current_height = height_conversion(feet, inches)

print(f"Height in inches = {current_height} inches.")

current_weight = float(input("Enter current weight: "))
print(f"Current weight  = {current_weight}")

def bmi_calculation():
    #BMI Calculation Formula
    bmi = (current_weight * 703)/(current_height**2)

    #Define BMI Criteria Categories
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 24.9:
        category = "Normal Weight"
    elif 25 <= bmi < 29.9:
        category = "Overweight"
    else:
        category = "Obese"
    
    print(f"\nBMI is {bmi:.2f}")
    print(f"You are in the {category} category.")

if __name__ == "__main__":
    bmi_calculation()