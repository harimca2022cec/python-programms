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
        return flag
def find_nth_prime(n):
    prime_count = 0
    number = 1
    while prime_count != n:
        number+=1
        if is_prime(number):
            prime_count+=1
            return number
print(prime(12))
print(find_nth_prime(5))
