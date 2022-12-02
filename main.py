# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


def factors(n):
    l=[]
    for i in range(1,n+1):
        if n%i==0:
            l.append(i)
    return l
def prime(n):
    f=0
    for i in range(2,n):
        if n%i==0:
            f=1
            break

    if f==0:
        print("{} is a Prime number".format(n))
    else:
        print("{} is Not a Prime number".format(n))

def amstrong(n,t):
    s=0
    if t==0:
        for l in n:
            s = s + (int(l) ** 3)

        if s == int(n):
            print("{} is a Amstrong No".format(n))
        else:
            print("{} Not an Amstrong No".format(n))
    else:
        m = int(n)
        s = 0
        while m > 0:
            r = m % 10
            m = m // 10
            s = s + r ** 3
        if s == int(n):
            print("{} is a Amstrong No".format(n))
        else:
            print("{} is Not an Amstrong No".format(n))
