# This code is also available at https://github.com/2601953/LAB-1

# Returns bools
def isOdd(number):
    return number % 2 != 0

def isEven(number):
    return not isOdd(number)

# Entry
print("Odd even checker:\ntype 'exit' to quit")

while True:
    # Standardise input
    user_in = input("Enter a number: ").lower()

    # Check exit condition before casting
    if user_in == 'exit':
        print("Exiting...")
        break

    # Use a try catch block to handle invalid inputs throwing an exception
    try:
        number = int(user_in)

        if isEven(number):
            print(f"{number} is even.")
        else:
            print(f"{number} is odd.")
            
    except:
        print("Invalid input. Please enter a valid integer.")

        # Wait for key press to continue
        input("Press Enter to continue...") 