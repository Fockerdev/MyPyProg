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

r = {"a": 1, "b": 2, "c": 3}

for a in r:
    print(a, r[a])

h = [2, 3, 4, 5, 6, 7, 10, 9, 8]


# List numeration

for t, y in enumerate(h):
    print(t + 1, y)

from random import sample

print(dir(sample))
print(dir(r))
print(dir(h))

'''
x = input()



def is_int(x):
    b = float(x) - int(float(x))
    if isinstance( x, int ) or (b == 0):
        return True
    else:
        return False

print(is_int(x))
print(x)

'''
'''
№ Поразрядная сумма
def digit_sum(n):
    if int(n) <=0:
        print("Negative")
    else:
        b=0
        for a in n:
            a=int(a)
            b+=a
        return b

print(digit_sum(x))
'''

'''
# Факториал
n = input("Факториал числа ")
n = int(n)
fac = 1
i = 0
while i < n:
    i+=1
    fac = fac*i
print("равен", fac)


input(x)

def is_prime(x):
  y = 2
  if x < 2:
      return False
  while y < x:
      if x % y == 0 :
          return False
      y += 1
  return True

print(is_prime(x))
'''

##############     revers STRING   ##############
list1 = "data1$$#@"


def reverse(text):
    if len(text) <= 1:
        return text

    return reverse(text[1:]) + text[0]


print(reverse(list1))

print(list1[0:2])

print(list1[-1])

print(reverse(list1[0:]))
print(list1[0:])


####     REMOVE VOWELS FROM STRING    ###########

string2 = "Hey My programmer developer"

vowels = ["a", "A", "i", "I", "o", "O", "u", "U", "e", "E"]


def anti_vowel(string2):
    vowels = ["a", "A", "i", "I", "o", "O", "u", "U", "e", "E"]
    new_text = ''
    for letter in string2:
        if letter not in vowels:
            new_text = new_text + letter
        else:
            new_text = new_text

    return new_text


print(anti_vowel(string2))


################       COUNT DICTIONARY ITEMS   ##############

score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}

# print(list(score))

data1 = "erereq"


def scrabble_score(word):
    score_end = 0
    for letter in word:
        score_end += score[letter]
    return score_end


print(scrabble_score(data1))
print(score["h"])
a = []

for key, value in score.items():
    # print(key)
    # print(type(a))
    a.append(key)

print(a)

###############   REPLACE WORD IN STRING  ##############3

text3 = "Hello my little brother, Hello"
word3 = "Hello"


def censor(text3, word3):
    b = ''
    # return text3.replace(word3, ("*"*len(word3)))
    # return ' '.join([('*' * len(word3)) if x == word3 else x for x in text3.split()])
    for x in text3.split():
        if x == word3:
            a = '*' * len(word3)
            b = b + " " + a
        else:
            m = x
            b = b + " " + m
    return b.strip()


print(censor(text3, word3))

h = 6
j = [h ** 2 + i for i in range(6)]
print(j)

#################     PRINT NUMBER OF SYMBOL IN LIST   ###############
sequence = ['a', 'c', 'c', 'a', 'v', 'b', 'b', 'b']
item = 'b'


def count(sequence, item):
    a = 0
    for i in sequence:
        if i == item:
            a += 1
        else:
            continue
    return a


print(count(sequence, item))

############  REMOVE ODD NUMBERS FROM LIST ########

s = 0
b = [s for s in range(1, 10)]


def purify(pureList):
    a = []
    for i in pureList:
        if i % 2 == 0:
            a.append(i)
        else:
            continue
    return a


print(purify(b))

####################  MULTIPLY ALL ELTVENTS IN LIST   ############

def product(ListProd):
    a = 1
    for i in ListProd:
        a = a * i
    return a


print(product(b))

#########################     REMOVE DUPLICATES ##################



def remove_duplicates(ListDub):
    return list(set(ListDub))


print(remove_duplicates(sequence))


def remove_duplicates1(ListDub1):
    r = []
    for a in ListDub1:
        if a not in r:
            r.append(a)
    return r


print(remove_duplicates1(sequence))


###################   COUNT MEDIAN   #############

medList = [1, 4, 3, 2, 7, 6, 9, 8, 12, 2]
med1 = [4,5,5,4]
med2 = [6, 8, 12, 2, 23]


def median(medList):
    medList.sort()
    if len(medList) == 1:
        return medList[0]
    elif len(medList) % 2 != 0:
        a = len(medList) / 2
        print(a)
        return medList[(len(medList) - int(len(medList) / 2 + 0.5))]
    else:
        return (medList[(int(len(medList) / 2))] + medList[(int(len(medList) / 2 - 1))]) / 2


print(median(med2))
print(7 % 2)



###############   LIST FUNCTION  #################

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades):
    i = 0
    while i < len(grades):
        print(grades[i])
        i+=1

print(print_grades(grades))

def sum(scores):
    i = 0
    scoreAll = 0
    while i < len(scores):
        print(scores[i])
        scoreAll += scores[i]
        i+=1
    return scoreAll

print(sum(grades))

def grades_average(grades):
    return sum(grades)/float(len(grades))

print(grades_average(grades))


def grades_variance(scores):
    average = grades_average(scores)
    variance=  0
    for score in scores:
        variance +=(average - score)**2
    return variance/len(scores)

print(grades_variance(grades))



def grades_std_deviation(variance):
    return variance ** 0.5


variance = grades_variance(grades)

print(grades_std_deviation(variance))
