import math

def list_square_even_power_odd(list_range):
    power_odd = [x**2 for x in range(list_range) if x % 2 != 0]
    square_even = [math.sqrt(x) for x in range(list_range) if x % 2 == 0]
    print('The Power of the  Odd numbers' + str(power_odd))
    print('The square root of the even numbers' + str(square_even))


list_square_even_power_odd(5)




