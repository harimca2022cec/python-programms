def afibnocci(n):
    first = 0
    second = 1
    if n == 1:
        print(first)
    else:
        for i in range(n):
            third = first + second
            first = second
            second = third
        print(first)
num = int(input("enter the limit:"))
afibnocci(num)
