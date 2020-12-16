import datetime
a = datetime.datetime.now()
print(a)


n=15
for i in range(0, n):
    for j in range(0, i+1):
        print("* ",end="")
    print("\r")
