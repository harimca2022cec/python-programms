limit =int(input("enter a limit:"))
num=[]
for i in range (limit):
    num.append(int(input(f"enter the {i}th element:")))
print(num)
squre_num = [i*i for i in num]
print("square of the above list is :")

print(squre_num)    
                 
