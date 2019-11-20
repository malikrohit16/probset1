n = int(input("Enter n: "))
x = 0
y = 0
for i in range(n+1):
    x = x + i
    y = y + (i*i)
print((x*x)-y)
