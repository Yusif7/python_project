from random import *

start_area = 0
end_area = 100
n_rand = randint(start_area, end_area)

n = int(input("Enter a number between 0 and 100: "))

while n_rand != n:
    if int(n) > n_rand:
        if int(n) > end_area:
            end_area = end_area
        else:
            end_area = int(n)
        n = int(input(f"Too much, try again, enter a number between {start_area} and {end_area}: "))
    elif int(n) < n_rand:
        if int(n) < start_area:
            start_area = start_area
        else:
            start_area = int(n)
        n = int(input(f"Too little, try again, enter a number between {start_area} and {end_area}: "))
if int(n) == n_rand:
    print('You win')
