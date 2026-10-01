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
        

# ---------------------------------------------------------------------------------------------------------------------------------------

# From Octal
def OrigOctal():

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

# ---------------------------------------------------------------------------------------------------------------------------------------

# From Decimal
# From Octal
def OrigDecimal():

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

# ---------------------------------------------------------------------------------------------------------------------------------------

# From Hexadecimal
def OrigHexadecimal():

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

# ---------------------------------------------------------------------------------------------------------------------------------------


# Number Input
OriBase = str(input("Input Original Base Number: "))
validOriBase = ["2", "8", "10", "16"]

if OriBase.strip() not in validOriBase:
    print("Wrong Base, please enter a valid Base")

OriValue = input("Input number to be converted: ")

if OriBase == "2":
    OrigBinary()
elif OriBase == "8":
    OrigOctal()
elif OriBase == "10":
    OrigDecimal()
elif OriBase == "16":
    OrigHexadecimal()