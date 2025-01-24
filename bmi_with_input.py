#define the function to convert feet to inches
def height_conversion(feet, inches):
    total_inches = (feet * 12) + inches    
    return total_inches

#define feet and inches variables, using input
feet = int(input("Enter feet: "))
inches = int(input("Enter inches: "))

#define height variable
current_height = height_conversion(feet, inches)

#print the result
print(f"Height in inches = {current_height} inches.")

#define weight variable, using input
current_weight = float(input("Enter current weight: "))
print(f"Current weight  = {current_weight}")

#define bmi calculator function
def bmi_calculation():
    #BMI Calculation Formula
    bmi = (current_weight * 703)/(current_height**2)

    #define BMI Criteria Categories
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 24.9:
        category = "Normal Weight"
    elif 25 <= bmi < 29.9:
        category = "Overweight"
    else:
        category = "Obese"

    #print the result
    print(f"\nBMI is {bmi:.2f}")
    print(f"You are in the {category} category.")

#run the program
if __name__ == "__main__":
    bmi_calculation()
