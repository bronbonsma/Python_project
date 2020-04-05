
def is_parsable(s):
    if s.isdigit():
        print("True")
        return True
    else:
        print("False")
        return False


is_parsable(input("Enter your age: "))
