# Build a program that converts decimal to binary, octal, and hexadecimal.


def to_binary(decimal):
    binary = bin(decimal)
    print(f"\nThe decimal value '{decimal}' is converted to binary value '{binary[2:]}'\n")

def to_octal(decimal):
    octal = oct(decimal)
    print(f"\nThe decimal value '{decimal}' is converted to octal value '{octal[2:]}'\n")

def to_hexadecimal(decimal):
    hexadecimal = hex(decimal)
    print(f"\nThe decimal value '{decimal}' is converted to hexadecimal value '{hexadecimal[2:]}'\n")

def main():

    print("\n-------Welcome to Number converter--------\n")

    while True:
        try:
            decimal = int(input("Enter a decimal number: "))

            convert_to = input("Enter type of conversion you want (binary, octal or hexadecimal) or enter 'q' to exit: ").lower().strip()

            if convert_to == "binary":
                to_binary(decimal)
            elif convert_to == "octal":
                to_octal(decimal)
            elif convert_to == "hexadecimal":
                to_hexadecimal(decimal)
            elif convert_to == "q":
                print("\nGoodbye! Have a good day.\n")
                print("-----------------------------")
                break
            else:
                print("Invalid input. Try again")
        except ValueError:
            print("Invalid input! Enter correct input.")

# Call main function
if __name__ == "__main__":
    main()

