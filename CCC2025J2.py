d = int(input())
e = int(input())

for i in range(e):
    plusOrMinus = input()
    q = int(input())
    if (plusOrMinus == "+"):
        d += q
    else:
        d -= q
if (d < 0):
    print(0)
else:
    print(d)
