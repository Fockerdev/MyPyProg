__author__ = 'Focker'


d = { "Name": "Guido",
    "Age": 56,
    "BDFL": True
    }

print(d.items())

print(d.keys())
print(d.values())

for i,j in d.items():
    print(i, "--", j)

for k in d:
    print(k,d[k])

MyList1 = [i for i in range(1,30,2)]
print(MyList1[2])

CubesList = [f**3 for f in range(1,11) if f**3%4==0]
print(CubesList)