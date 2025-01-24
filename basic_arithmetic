### Create a basic arithmetic calculator 

#Define function
def basic_calculator():
    while True:
        try: 
            equation = input("Enter arithmetic equation: ")
            result = eval(equation)

            #print result
            print(f"{equation} = {result:.2f}")

        #handle exceptions and errors
        except ZeroDivisionError:
            print("ERROR: Cannot divide by zero")
        except (SyntaxError, NameError):
            print("ERROR: invalid input")
        except Exception as e:
            print(f"ERROR: {e}")
        break

#run program
basic_calculator()
