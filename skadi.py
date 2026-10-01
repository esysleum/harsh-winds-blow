# Loop Iteration Counter 
LoopIteration = 0

while():
    print()


# ---------------------------------------------------------------------------------------------------------------------------------------

def InputAndRunBlock():
    # Number Input
    global OriBase # Makes the "OriValue" variable global
    OriBase = str(input("Input Original Base Number: "))
    validOriBase = ["2", "8", "10", "16"]

    if OriBase.strip() not in validOriBase:
        print("Wrong Base, please enter a valid Base")

    global OriValue # Makes the "OriValue" variable global
    OriValue = input("Input number to be converted: ")

    if OriBase == "2":
        OrigBinary()
    elif OriBase == "8":
        OrigOctal()
    elif OriBase == "10":
        OrigDecimal()
    elif OriBase == "16":
        OrigHexadecimal()

# ---------------------------------------------------------------------------------------------------------------------------------------

# Declaring def Functions 
# From Binary
def OrigBinary():
    try:

        # Convert Everything to Decimal
        ConValue = int(OriValue, 2)

        #Conversion & Printing Block
        # To Binary
        print(OriValue)

        # To Octal
        Octal = oct(ConValue) [2:]
        print(Octal)

        # To Decimal
        print(ConValue)

        # To Hexadecimal
        Hexadecimal = hex(ConValue) [2:]
        print(Hexadecimal)
    
    except ValueError:
        print("Number entered is Invalid")


# ---------------------------------------------------------------------------------------------------------------------------------------

# From Octal
def OrigOctal():
    try:

        # Convert Everything to Decimal
        ConValue = int(OriValue, 8)

        # Conversion & Printing Block
        # To Binary
        Binary = bin(ConValue) [2:]
        print(Binary)

        # To Octal
        print(OriValue)

        # To Decimal
        print(ConValue)

        # To Hexadecimal
        Hexadecimal = hex(ConValue) [2:]
        print(Hexadecimal)

    except ValueError:
        print("Number entered is Invalid")

# ---------------------------------------------------------------------------------------------------------------------------------------

# From Decimal
# From Octal
def OrigDecimal():
    try:

        # Convert Everything to Decimal
        ConValue = int(OriValue, 10)

        # Conversion & Printing Block
        # To Binary
        Binary = bin(ConValue) [2:]
        print(Binary)

        # To Octal
        Octal = oct(ConValue) [2:]
        print(Octal)

        # To Decimal
        print(ConValue)

        # To Hexadecimal
        Hexadecimal = hex(ConValue) [2:]
        print(Hexadecimal)

    except ValueError:
        print("Number entered is Invalid")

# ---------------------------------------------------------------------------------------------------------------------------------------

# From Hexadecimal
def OrigHexadecimal():
    try:

        # Convert Everything to Decimal
        ConValue = int(OriValue, 16)

        # Conversion & Printing Block
        # To Binary
        Binary = bin(ConValue) [2:]
        print(Binary)

        # To Octal
        Octal = oct(ConValue) [2:]
        print(Octal)

        # To Decimal
        print(ConValue)

        # To Hexadecimal
        print(OriValue)

    except ValueError:
        print("Number entered is Invalid")

# ---------------------------------------------------------------------------------------------------------------------------------------


InputAndRunBlock()
