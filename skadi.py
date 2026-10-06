# ---------------------------------------------------------------------------------------------------------------------------------------

def InputAndRunBlock():
        
        global LoopIteration # Makes the LoopIteration variable 
        LoopIteration = 0
        LoopIteration += 1 # Adds 1 to LoopIteration

        # Number Input
        global OriBase # Makes the "OriValue" variable global
        OriBase = str(input("Input Original Base Number: "))
        validOriBase = ["2", "8", "10", "16"]

        if OriBase.strip() not in validOriBase:
            print("Error! Value or Base Invalid!")
            return

        global OriValue # Makes the "OriValue" variable global
        OriValue = input("Input the number to be converted: ")

        global ErrorMessage # Allows the variable ErrorMessage to be referenced by other defs
        ErrorMessage = "Number entered is Invalid"

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
        print(Hexadecimal.upper)
    
    except ValueError:
        print(ErrorMessage)


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
        print(Hexadecimal.upper)

    except ValueError:
        print(ErrorMessage)

# ---------------------------------------------------------------------------------------------------------------------------------------

# From Decimal
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
        print(Hexadecimal.upper)

    except ValueError:
        print(ErrorMessage)

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
        print(OriValue.upper)

    except ValueError:
        print(ErrorMessage)

# ---------------------------------------------------------------------------------------------------------------------------------------

while True: # The while loop
    InputAndRunBlock() # runs the InputAndRunBlock function

    if LoopIteration >= 1: # Checks if LoopIteration value is greater or equal to 1
        ChoiceInput  = str(input("Terminate Program? \nInput uppercase letter Y if you would like to terminate program, otherwise input anything: "))

        # If ChoiceInput is exactly Y
        if ChoiceInput == "Y":
            print("Shutting Down Program")
            break 

        # If ChoiceInput is anything but Y
        else:
            continue
    # If LoopIteration is below or equal to 0
    else:
        continue 
