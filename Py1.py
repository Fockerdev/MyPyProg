__author__ = 'Focker'
import sys;


print('welcome');

my_int = 7
'''my_float = 1.23
my_bool = True
'''

print(my_int);


def f1():
    toy = 12;
    return toy;


print(f1());
# return my_int;

webster = {
    "Aardvark": "A star of a popular children's cartoon show.",
    "Baa": "The sound a goat makes.",
    "Carpet": "Goes on the floor.",
    "Dab": "A small amount."
}

# Add your code below!

for z in webster:
    print(webster[z])

from datetime import datetime;

print(datetime.now())

import math
# everything = dir(math)
print(dir(datetime))

meal = 44.50
tax = 0.0675
tip = 0.15
meal *= 1.2


def distance_from_zero(s, a):
    if (type(s) and type(a)) == int or (type(s) and type(a)) == float:
        return max(s, a)
    else:
        return "Nope"


print(distance_from_zero(8, 7))

print(type(meal))

word = "text";
word1 = 34;

print(word.upper() + ' ' + str(word1));
print("w1 %s, %s" % (word, word1));
#color = input("erer");
#print("eee",color);

def MY():
    print("make the design")
    answer = input("1 or 2")
    if answer == "1":
        print("good")
    elif answer == "2":
        print("no good")
    else:
        print("bad")


number = 3

'''MyList = ["1tete", "2tyty", "3rt", "4r4r", "\'5ttt"]

print(MyList[0:2])
print(MyList.index("3rt"))
MyList.insert(2,1)
print(MyList)
'''
start_list = [5, 3, 1, 2, 4]
square_list = []

# Your code here!
square_list = [a ** 2 for a in start_list]

print(start_list)
print(square_list)

residents = {'Puffin': 104, 'Sloth': 105, 'Burmese Python': 106}

for d, f in residents.items():
    print(d, "=>", f)
    print(residents)

inventory = {
    'gold': 500,
    'pouch': ['flint', 'twine', 'gemstone'],  # Assigned a new list to 'pouch' key
    'backpack': ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}

# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

# Sorting the list found under the key 'pouch'
inventory['pouch'].sort()

# Your code here
inventory['pocket'] = ['seashell', 'strange berry', 'lint']

inventory['backpack'].sort()

inventory['backpack'].remove('dagger')

inventory['gold'] += 50

for t, k in inventory.items():
    print(t, "--", k)


def cube(number):
    # ererer
    number = number ** 3
    return number


def by_three(number):
    if (number % 3) == 0:
        return cube(number)
    else:
        return False


print(by_three(3))

'''

pyg = 'ay'

original = input('Enter a word:')
word = original.lower()
first = word[0]
new_word = word[1:] + first + pyg

if len(original) > 0 and original.isalpha():
    print(new_word)
else:
    print('empty')
'''
meal = meal + meal * tax
total = meal + meal * tip

print("%.4f" % total + ' tes\'t')

####

board=[]
for g in range(5):
    board.append(["O"]*5)

from random import randint

# for i in range(5):
 #   board.append(range(0,5))

def print_board(board):
    for i in board:
        print(" ".join(i))
      #  print(i)

print(board)
print(print_board(board))

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

print(ship_row)
print(ship_col)

for turn in range(4):

    guess_row = int(input("Guess Row:"))
    guess_col = int(input("Guess Col:"))

    if guess_row == ship_row and guess_col == ship_col:
            print("Congratulations! You sunk my battleship!")
            break
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print("Oops, that's not even in the ocean.")
        elif(board[guess_row][guess_col] == "X"):
            print("You guessed that one already.")
        else:
            print("You missed my battleship!")
            board[guess_row][guess_col] = "X"
    # Print (turn + 1) here!
    print("Turn", turn + 1)
if turn == int("3"):
    print("Game Over")
print_board(board)