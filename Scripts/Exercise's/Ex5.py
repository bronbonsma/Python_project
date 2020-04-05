def build_pyramid():

    try:
      rows = int(input("Enter the number of Rows: "))
      for i in range(rows):
        print(' '*(rows-i-1) + '*'*(2*i+1))
    except ValueError:
        print("That is not a number ")


build_pyramid()
