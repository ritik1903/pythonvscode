# print("Hello world")
num=int(input())
i=1
while num<=i:
    space=1
    while space<=num-i:
        print(" ",end="")
        space=space+1
    star=1
    while star<=i:
        print("*",end="")
        star=star+1
    print()
    i=i+1