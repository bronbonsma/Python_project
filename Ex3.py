def is_even(number):
    if number % 2 == 0:
       return True


while True:
    try:
        number = int(input("Enter a number: "))
        is_even(number)
    except ValueError:
        print("Sorry, that's not a number!!")

        continue
    else:
        break
if number % 2 == 0:
    print("True")
else:
    print("False")

