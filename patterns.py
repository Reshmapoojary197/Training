n=5
for i in range(1,n+1):
    for j in range(1,n+1):
         print('*',end='')
    print(" \r")
#
n=5
for i in range(1,n+1):
    for j in range(1,i+1):
         print(j,end='')
    print(" \r")


n=5
for i in range(n+1):
    for j in range(i):
         print(i,end='')
    print(" \r")

n=5
for i in range(n,0,-1):
    for j in range(1,i+1):
         print(j,end='')
    print(" \r")

n=5
for i in range(n+1):
    for j in range(i+1):
         print(n,end='')
    print(" \r")

n=5
for i in range(n,0,-1):
    for j in range(1,i+1):
         print(n,end='')
    print(" \r")

n=5
for i in range(n,0,-1):
    for j in range(1,i+1):
         print(j,end='')
    print(" \r")

n=5
for i in range(1,n+1):
    for j in range(i,0,-1):
         print(j,end='')
    print(" \r")
#
n=5
for i in range(n, 0, -1):
        for j in range(n - i):
            print(" ", end="")
        for j in range(i, 0, -1):
            print(j, end="")
        print()
