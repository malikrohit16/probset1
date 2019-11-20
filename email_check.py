l = []
n = int(input("Enter number of emails: "))
for i in range(n):
    e = input()
    if '@' in e:
        a = e.split('@')[1]
        if '.'  in a:
            if a.split('.')[0].isalpha() and a.split('.')[1].isalpha():
                l.append(e)
print(l)
