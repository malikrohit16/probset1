n = int(input("Enter n: "))
for i in range(n):
    for j in range(n):
        if j<=i:
            print(j+1,end="")
        if j == i:
            for k in range(j,0,-1):
                print(k,end="")
    print()
