def prime(n):
    flag=0
    n=int(input("enter a number:"))
    for i in range(2,n):
            if n%i==0:
                flag=1
                break
    if flag==1:
        print("not")
    else:
          print("number is prime")
prime(7)





