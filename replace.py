a=("hello")
b=("good")
c=("better")
vowels="aeiouAEIOU"
for i in a:
    if i in vowels:
        a=a.replace(i,"@")
        print(a)
for i in b:
    if i not in vowels:
        b=b.replace(i,"*")
        print(b)
c=c.upper(c)
print(c)