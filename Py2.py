__author__ = 'Focker'


from random import randint

# Generates a number from 1 through 10 inclusive
random_number = randint(1, 10)

guesses_left = 3
# Start your game!
'''while guesses_left>0:
    guess = int(input("Your guess: "))
    if guess == random_number:
        print('You win!')
        break
    guesses_left-=1
else:
    print('You LOSE!')

'''

r = {"a":1, "b":2, "c":3}

for a in r:
    print(a, r[a])


h = [2,3,4,5,6,7]


# List numeration

for t,y in enumerate(h):
    print(t, y)

from random import sample
print(dir(sample))
print(dir(r))
print(dir(h))


x = input()

def is_int(x):
    b = float(x) - int(float(x))
    if isinstance( x, int ) or (b == 0):
        return True
    else:
        return False

print(is_int(x))
print(x)


