__author__ = 'Focker'


d = { "Name": "Guido",
    "Age": 56,
    "BDFL": True
    }


# Usually print
print(d.items())

print(d.keys())
print(d.values())

for i,j in d.items():
    print(i, "--", j)

for k in d:
    print(k,d[k])

MyList1 = [i for i in range(1,30,2)]
print(MyList1[::-1])

MyList2 = MyList1[::-2]
print(MyList2)

CubesList = [f**3 for f in range(1,11) if f**3%4==0]
print(CubesList)

##############   LAMBDA ###########

rem = lambda k: k+22

print(rem(2))

my_list = list(range(16))
print(my_list)
print(list(filter(lambda p: p % 3 == 0, my_list)))

squares = [i**2 for i in range(1,11)]

print(filter(lambda x: x >=30 and x <=70, squares))


threes_and_fives = [h for h in range(1,16) if (h%3 == 0 or h%5 == 0)]
print(threes_and_fives)

###################   SLICE

garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"

message = garbled[::-1]
message = message[::2]
print(message)

message2 = garbled
print(message2)
m3 = list(filter(lambda x: x!= 'X' , message2))

print(''.join(m3))

print(9 | 4)   # Bitwise OR
print(0b1 + 0b11)

print("-----")
print(bin(0b1 << 2))
