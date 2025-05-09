oddOrEven = int(input("Please enter a number: "))
resultOddOrEven = ""

if oddOrEven % 2 == 0:
    resultOddOrEven = "EVEN"
else:
    resultOddOrEven = "ODD"

print(f"The Number is {resultOddOrEven}")