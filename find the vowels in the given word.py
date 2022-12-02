vowels=["a","e","i","o","u"]
word=input("enter the word")
vowelist=[]
for alphabet in word:
        if alphabet in vowels:
            vowelist.append((alphabet))
print(vowelist)