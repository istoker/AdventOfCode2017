from math import ceil, sqrt
from math import pow as power

def solve_for_lower_right(number, base):
    corner = power(base, 2)
    opposing_corner = power(base-1, 2)+1
    middle_corner = corner - ((corner - opposing_corner)/2)
    if number < middle_corner:
        if number <= opposing_corner + ((middle_corner - opposing_corner)/2):
            return base - 1 - (number - opposing_corner)
        else:
            return base - 1 - (middle_corner - number)
    else:
        if number <= middle_corner + ((corner - middle_corner)/2):
            return base - 1 - (number - middle_corner)
        else:
            return base - 1 - (corner - number)

def solve_for_upper_left(number, base):
    corner = power(base, 2)
    opposing_corner = power(base-1, 2) + 1
    middle_corner = corner - ((corner - opposing_corner)/2)
    if number < middle_corner:
        if number < opposing_corner + ceil((middle_corner - opposing_corner)/2):
            return base - 1 - (number - opposing_corner)
        else:
            return base - (middle_corner - number)
    else:
        if number < middle_corner + ceil((corner - middle_corner)/2):
            return base - (number - middle_corner)
        else:
            return base - 1 - (corner - number)


def is_even(number):
    return number % 2 == 0

def main():
    number = 325489
    base = ceil(sqrt(number))
    if is_even(power(base, 2)):
        print(int(solve_for_upper_left(number, base)))
    else:
        print(int(solve_for_lower_right(number, base)))

if __name__ == '__main__':
    main()