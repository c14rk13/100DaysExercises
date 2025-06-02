# Can declare variables with data types specified explicitly
# Ex:
#   age: int
#   name: str
#   height: float
#   is_human: bool


# Can also explicitly declare the data type returned by a function using arrow notation:
def police_check(age: int) -> bool:
    if age > 18:
        can_drive = True
    else:
        can_drive = False

    return can_drive

