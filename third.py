#pattern
# n=int(input())
# i=1
# while i<=n:
#     space=1
#     while space<=n-i:
#         print(" ",end="")
#         space=space+1
#     num=1
#     while num<=i:
#         print(num,end="")
#         num=num+1
#     rev=i-1
#     while rev>=1:
#         print(rev,end="")
#         rev=rev-1
#     print()
#     i=i+1

# n=int(input())
# i=1
# while i<=n:
#     spaces=1
#     while spaces<=(n-i):
#         print(" ",end="")
#         spaces=spaces+1
#     j=1
#     num=i
#     while j<=i:
#         print(num,end="")
#         num=num+1
#         j=j+1
#     j=1
#     num=2*i-2
#     while j<=i-1:
#         print(num,end="")
#         num=num-1
#         j=j+1
#     print()
#     i=i+1
    
# n=int(input())
# currRow=1
# while currRow<=n:
#     spaces=1
#     while spaces<=(n-currRow):
#         print(" ",end="")
#         spaces+=1
#     currCol=1
#     valToPrint=currRow
#     while currCol<=currRow:
#         print(valToPrint,end="")
#         valToPrint+=1
#         currCol+=1
#     currCol=1
#     valToPrint=2*currRow-2
#     while currCol<=currRow-1:
#         print(valToPrint,end="")
#         valToPrint-=1
#         currCol+=1
#     print()
#     currRow+=1


# n = int(input())
# firstHalf = (n + 1) // 2
# secondHalf = n // 2
# i = 1 
# while i <= firstHalf:
#     spaces = 1 
#     while spaces <= (firstHalf - i) :
#         print(" ", end = "")
#         spaces += 1
#     j = 1
#     while j <= (2 * i) - 1 :
#         print("*", end = "")
#         j += 1    
#     print()
#     i += 1
# i = secondHalf 
# while i >= 1 :
#     spaces = 1
#     while spaces <= (secondHalf - i + 1) :
#         print(" ", end = "") 
#         spaces += 1
#     j = 1 
#     while j <= (2 * i) - 1 :
#         print("*", end = "") 
#         j += 1
#     print()
#     i -= 1

# N=int(input()) #Take user input, N= Number of Rows
# row=1; #The loop starts with the 1st row
# while row<=N:#Loop will on for N rows
#     col=1; #The loop starts with the first column in the current row
#     while col<=N-row:#The loop will go on for N columns
#         print(" ",end="")
#         col=col+1#Printing a (" ")
#     num=1
#     while num<=row:
#         print("*",end="")
#         num=num+1  
#     row=row+1 #Increment the current row (Outer Loop)
#     print() 

# num=int(input())
# for i in range(1,num+1,1):
#     print(i)for i in range(1,5,2):
    # print(i,end=' '
    
    
# for i in range(1,6,2):
#     print(i,end=' ')
# for i in range(5):
#     print(i,end= ' ')

# n=int(input())
# for i in range(3,33,3):
#     print(i,end=" ")
#     print()

# from enum import Flag


# num=int(input())
# Flag=False
# for d in range(2,num,1):
#     if num%d==0:
#         Flag=True
# if Flag:
#     print("It is not prime")
# else:
# #     print("The number is prime number")
# n=int(input())
# for i in range(1,n+1,1):
#     for s in range(n-i):
#         print(" ",end="")
#     for num in range(i,2*i,1):
#         print(num,end="")
#     for rev in range(2*i-2,i-1,-1):
#         print(rev,end="")
#     print()
# i=1
# while i<3:
#     j=1
#     while j<5:
#         if j==3:
#             break
#         print(j,end='')
#         j = j + 1
#     i = i + 1

# i=1
# while i<5:
#     if i == 6:
#         break
#     print(i,end=" ")
#     i = i + 1
# else:
#     print('Else is also printed')

# i=1
# while i<5:
#     if i == 3:
#         break
#     print(i,end='')
#     i = i + 1
# else:
# #     print('Else is also printed')

# for i in range(5):
#     for j in range(i+1):
#         print("*",end="")
#     print()

# n=int(input())
# i=1
# while i<=n:
#     j=1
#     while j<i:
#         print("*",end="")
#         j=j+1
#     print()
#     i=i+1

# n=int(input("Enter the range of the pattern:"))
# for i in range(n):
#     for j in range(n-i):
#         print(end=' ')
#     for j in range(i+1):
#         print("*",end=" ")
#     print()

# i=11
# while i<5:
#     if i==3:
#         continue
#     print(i,end=" ")
#     i = i + 
    
# i=1
# while i<3:
#     j=0
#     while j<5:
#         j = j +1
#         if j==3:
#             continue
#         print(j,end=" ")
#     i = i +1

# i=3
# if i<7:
#     print("Pass")
# n=int(input())
# flag=True
# if n>1:
#     for i in range(2,n):
#         if n%2==0:
#             flag=False
#             break
# if n<=1:
#     print("The number is not prime number")
# elif flag:
#     print("The number is prime number")
# else:
#     print("THis is not the prime number")

# n = int(input())
# for i in range(1,n+1):
#     count = 1
#     for j in range(1,i):
#         print(" ",end="")
#         count = count + 1
#     num = i 
#     for j in range(count,n+1):
#         print(num,end="") 
#         num = num + 1
#     print()
# for i in range(n-1,0,-1):
#     count=1
#     for j in range(1,i):
#         print(" ",end="")
#         count=count+1
#     num=i
#     for j in range(count,n+1):
#         print(num,end="")
#         num=num+1
#     print()
# def isPrime(n):
#     for i in range(2,n):
#         if (n%i==0):
#             break
#     else:
#         return True
#     return False
# isPrime(3)
# a = 5
# def func(a):
#     a = a + 10
#     return a
# def square(a):
#     ans  = a*a
#     return  ans

# a = 4
# a = square(a)
# # print(a)
# def foo():
#     y = "local"
#     print(y)
# # foo()
# def printTable(start,end,step):
#     curr_temp = start

#     while curr_temp <= end:
#         c = 5/9 * (curr_temp-32)
#         print(curr_temp, " ", int(c))
#         curr_temp = curr_temp+step
# pass 
# s = int(input())
# e = int(input())
# step = int(input())
# printTable(s,e,step)


# import math
# def isPerfectSquare(x): 
#     s = int(math.sqrt(x)) 
#     return s*s == x 

# def checkMember(n):
#     return isPerfectSquare(5*n*n + 4) or isPerfectSquare(5*n*n - 4) 
# pass



# n=int(input())
# if(checkMember(n)):
#     print("true")
# else:
#     print("false")


# num = int(input())
# sum = 0
# temp = num
# while temp > 0:
#    digit = temp % 10
#    sum += digit ** 3
#    temp //= 10
# if num == sum:
#     print("true")
# else:
# # print(('%d %d %.2f') (11, '22', 11.22))

# print(sep='--', 'Ben', 25, 'California')

# x = float('NaN')
# print('%f, %e, %F, %E' % (x, x, x, x))

# print('%x, %X' % (15, 15))
# x = 0
# while (x < 100):
#   x+=2
# print(x)

# var = 10
# for i in range(10):
#     for j in range(2, 10, 1):
#         if var % 2 == 0:
#             continue
#             var += 1
#     var+=1
# else:
#     var+=1
# print(var)