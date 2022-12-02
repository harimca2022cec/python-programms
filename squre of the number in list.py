numlist=[]
sqrlist=[]
r=int(input("enther the numbers to calculate square of"))
for num in range(0,r):
    inp=int(input("enter a number"))
    numlist.append(inp)
    for num in numlist:
        sqrlist.append(num**2)
print(sqrlist)
