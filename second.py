# number1=input("FIrst number:")
# number2=input("second number:")
# sum=float(number1)+float(number2)
# print("The sum of {0} and {1} is {2}" .format(number1,number2,sum))

#write a python program for print the sum of two number
# number1=input("Enter the first number:")
# number2=input("Enter the second number:")
# sum=int(number1)+int(number2)
# print(sum)

#writ a python program for print the greatest number among twwo number
# def maximum(a,b):
#     if a>=b:
#         return a
#     else:
#         return b
#     a=2
#     b=4
#     print(maximum (a,b))


#write a python program for find the factorial of the fiven number
# def factorial(n):
#     return 1 if (n==1 or n==0) else n* factorial(n-1);
# num=input("Enter the number to print the facotorial")
# print("Factorial of",int(num),"is",factorial(int(num)))

#Write a python program for append the string in the list
# ritik=[]
# ritik.append(21)
# ritik.append(45.5)
# ritik.append("RITIK")
# print("ritik",ritik)

# def getInteger():
#     result = int(input("Enter integer: "))
#     return result

# def Main():
#     print("Started")

#     # calling the getInteger function and 
#     # storing its returned value in the output variable
#     output = getInteger()     
#     print(output)

# # now we are required to tell Python 
# # for 'Main' function existence
# if __name__=="__main__":
#     Main()

# john=3
# mary=21
# adam=12
# totalapples=john+mary+adam
# print("Total number of apples",totalapples)

#write a python program for print the average of three number 
# a=2
# b=2
# c=2
# averagenumber=(a+b+c)/3
# print(int(averagenumber))


#write a python program to find the greatest mong three number
# a=12
# b=1
# c=21
# if a>b and a>c:
#     print("A is greater")
# elif b>a and b>c:
#     print("B is greater")    
# else:
#     print("null")

#Wite a python program to find the number is positive negative or zero 
# num =int(input("Enter the number:"))
# if num>0:
#     print("The number is positive")
# elif num==0:
#     print("The number is zero")
# else:
#     print("The number is negative")

#write a python progam to find the valid triangle or not 
# num=int(input("Enter the number:"))
# for i in range(num,num+1)
# print(num)

# #wrote a python program for print the factorial of the given number
# def  factorial(n):
#     if n==0:
#         return 1
#     else:
#         return n*factorial(n-1)
#     n=int(input("Enter the number :"))
#     print(factorial(n))

# import mimetypes


# num=int(input("Enter the number:"))
# factorial=1
# if num<0:
#         print("This is the wrong solution to print the factorial")
# elif num==0:
#         print("The factorial of 0 is 1")
# else:
#     for i in range(1,num+1):
#         factorial=factorial*i
# print("The factorial of",num,"is",factorial)

#write a python program to find the even number 
# start,end=0,20
# for num in range(start,end+1):
#     if num%2!=0:
#         print(num,end=" ")       

# start=int(input("Enter the starting range:"))
# end=int(input("Enter the ending range:"))
# for num in range(start,end+1):
#     if num%2==0:
        # print(num,end=" ")

# start=int(input("Enter the number:"))
# end=int(input("Enter the number:"))
# for num in range(start,end+1):
#     if num%2!=0:
#         print(num,end=" ")

# num=11
# if num>1:
#     for i in range(2,int(num/2)+1):
#         if(num%i)==0:
#             print(num,"is not a prime number")
#             break
#         else:
#             print(num,"is a prime number")
  
# number=int(input("Enter the number:"))
# if number>1:
#     for i in range(2,number):
#         if(number%i==0):
#             print(number,"is not a prime number")
#             break
#     else:
#             print(number,"is a prime number")
# else:
#         print(number,"is not a prime number")

# num1=int(input("enter the first number:"))
# num2=int(input("enter the second number:"))
# num3=int(input("Enter the third number:"))
# if num1>num2 and num1>num3:
#     print("number one is greater than the number two and number three")
# elif num2>num1 and num2>num3:
#     print("number two is greater than the number one and and number three")
# else:
#     print("number three is greater than the other two number")
      
        
# list1=[]
# num=int(input("ENter the number:"))
# for i in range(1,num+1):
#     greater=int(input("Enter the elements:"))
#     list1.append(greater)
# print("Largest element is:",max(list1))

# start=int(input("Enter the starting range:"))
# end=int(input("ENter the ending range:"))
# for num in range(start,end+1):
#     if num%2!=0:
#         print(num,end=" ")


#write a python program for print the factorial of the given number.
# num=int(input("Enter the number to print the factorial:"))
# factorial=1
# if factorial<0:
#     print("It is not the right way to print the factorial number")
# elif num==0:
#     print("The factorial of zero is one")
# else:
#     for i in range(1,num+1):
#         factorial=factorial*i
#         print("The factorial of",num,"is",factorial)

# minimum=int(input("Enter the minimum number:"))
# maximum=int(input("Enter the maximum number:"))
# total=0
# for number in range(minimum,maximum+1):
#     if number%2==0:
#         print("{0}".format(number))
#         total=total+number
# print("total sum of even number{0} to {1}={2}".format(minimum,number,total))

#write a python program to find the GCD of two number
# num1=int(input("ENter the first number:"))
# num2=int(input("Enter the second number:"))
# i=1
# while(i<=num1 and i<=num2):
#         if(num1%i==0 and num2%i==0):
#                 gcd=i
#         i=i+1
# print("THe GCD of {0} and {1}={2}".format(num1,num2,gcd))
        
# Take input from user
# upto = int(input("Find prime numbers upto : "))

# print("\nAll prime numbers upto", upto, "are : ")

# for num in range(2, upto + 1):

#     i = 2

#     for i in range(2, num):
#         if(num % i == 0):
#             i = num
#             break;

#     # If the number is prime then print it.
#     if(i != num):
#         print(num, end=" ")

#wirte a python prgram to find the factorial of the given number
# from re import I


# num=int(input("enter the number to find the number:"))
# fac=1
# if int(num)>1:
#         for i in range(1,int(num)+1):
#                 fac=fac*i
#         print("Factorial of",num,"is:",fac)

#write a c program to find the even numberodd number

# a=int(input())
# b=int(input())
# c=a+b
# print(c)        

# mark1=int(input())
# mark2=int(input())
# mark3=int(input())
# avg=(mark1+mark2+mark3)/3
# print(avg)
# X=int(input())
# N=int(input())
# power=X**N
# print(power)

  
# num1=int(input("Enter first number:"))
# num2=int(input("Enter second number:"))
# num3=int(input("Enter third number:"))
# number=num2-num1 and num3-num2
# print(number)
# int a=1
# int b=3
# int c=5
# number=b-a and c-b
# print(number)

# a=int(input("Enter the number :"))
# if a%2!=0:
#         print("It is even number")
# else:
#         print("It is odd number")
# var1 = 1
# var2 = 2
# var3 = "3"

# print(var1 + var2 + var3)

# for i in range(10, 15, 1):
#   print( i, end=', ')
# x = 36 / 4 * (3 +  2) * 4 + 2
# print(x)
# 
# # f calculate (num1, num2=4):
#       res = num1 * num2
# print(res)
# de

# calculate(5, 6)
# 
# 
# 
# 
# 
# 
# 
# salary = 8000

# def printSalary():
#   salary = 12000
#   print("Salary:", salary)
  
# printSalary()
# # print("Salary:", salary)
# x = 50
# def fun1():
#     x = 25
#     print(x)
    
# fun1()
# print(x)
# x = 75
# def myfunc():
#     x = x + 1
#     print(x)

# myfunc()
# print(x)
# def func1():
#     x = 50
#     return x
# func1()
# print(x)
# num=int(input())
# if num<0:
#     print("Negative")
# elif num>0:
#     print("Positive")
# elif num==0:
#     print("Zero")
# else:
# if (10 < 0) and (0 < -10):
#      print("A")
# elif (10 > 0) or False:
#      print("B")
# else:
#     print("C")
# if True or True:
#     if False and True or False:
#         print('A')
#     elif False and False or True and True:
#        print('B')
#     else:
#       print('C')
# else:
#      print('D')
# num=int(input())
# sum=0
# while num>0:
#     sum=sum+num
#     num=num-1
# print(sum)
# num=int(input())
# total=0
# number=1
# while number<=num:
#     if(number%2==0):
#         total=total+number
#     number=number+1
# print(total)
# i=0
# while i<10:
# print(i)
# i=i+
# i=0
# while i<10:
#     print(i)
# # i = i+1
# def printTable(s,e,w):
#     while True:
#         c=0
#         if s<=e:
#             c=(s-32)*5/9
#             print(s,int(c))
#             s=s+w
#         else:
#             break
# s=int(input())
# e=int(input())
# step=int(input())
# printTable(s,e,step)
# list=[10,20,30]
# i=list[1]
# for i not in list:
#     i += 1
#     print(i,end=" ")num1=int(input())
# num=int(input())
# while num!=6:
#     if num<=5 and num>=1:
#         a=int(input())
#         b=int(input())
#     if num==1:
#         print(a+b)
#     if num==2:
#         print(a-b)
#     if num==3:
#         print(a*b)
#     if num==4:
#         print(a//b)
#     if num==5:
#         print(a%b)
#     elif num<1 or num>6:
#         print("Invalid operator")
#     num=int(input())
# num=int(input())
# rev=0
# while num>0:
#     rem=num%10
#     rev=rev*10+rem
#     num=num//10
# print(rev)
# number=int(input())
# rev=0
# temp=number
# while temp>0:
#     rem=temp%10
#     rev=(rev*10)+rem
#     temp=temp//10
# if(number==rev):
#     print("True")
# else:
#     print("False")
# number=int(input())
# even=0
# odd=0
# while number>0:
#     rem=number%10
#     if(rem%2==0):
#         even=even+rem
#     else:
#         odd=odd+rem
#     number=number//10
# print(even," ",odd)
# num=int(input())
# while num!=6:
#     if num<=5 and num>=1:
#         a=int(input())
#         b=int(input())
#     if num==1:
#         print(a+b)
#     elif num==2:
#         print(a-b)
#     elif num==3:
#         print(a*b)
#     elif num==4:
#         print(a//b)
#     elif num==5:
#         print(a%b)
#     elif num<1 or num>6:
#         print("Invalid operator")
#     num=int(input())
# def fibonacci(n):
#     if n<0:
#         print("Incorrect input")
#     elif n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fibonacci(n-1)+fibonacci(n-2)
# n=int(input())
# print(fibonacci(n))
# n=int(input())
# i=1
# while i<=n:
#     j=1
#     while j<=n:
#         print(j,end=" ")
#         j=j+1
#     print()
#     i=i+1
# from pickletools import int4


# num=int(input())
# i=1
# while i<=num:
#     j=1
#     p=1
#     while j<=i:
#         print(p,end="")
#         j=j+1
#     print()
#     i=i+1
# num=int(input())
# i=1
# while i<=num:
#     j=1
#     starting_point=ord("A")+i-1
#     while j<=i:
#         print(chr(starting_point+j-1),end="")
#         j=j+1
#     print()
#     i=i+1
# n=int(input())
# for i in range(n,0,-1):
#     for j in range(j,n+1):
#         print(chr(j+64),end="")
#     print()
# num=int(input())
# i=1
# while i<=num:
#     j=1
#     while j<i+1:
#         if(j==1 or j==i):
#             print(1,end="")
#         else:
#             print(2,end="")
#         j=j+1
#     i=i+1
#     print()


#       *
#      **
#     ***
#    ****
# num=int(input())
# i=1
# while num<=i:
#     space=1
#     while space<=num-i:
#         print(" ",end="")
#         space=space+1
#     star=1
#     while star<=i:
#         print("*",end="")
#         star=star+1
#     print()
#     i=i+1


# def lastIndex (a,x,si):
#     l=len(a)
#     if si==l:
#         return -1
#     smallerlistoutput=lastIndex(a,x,si + 1)
#     if smallerlistoutput != -1:
#         return smallerlistoutput
#     else:
#         if a[si]==x:
#             return si
#         else:
#             return -1
# a=[1,3,4,5,6]
# x=5
# print(lastIndex(a,x,0))

# def replacePi(string):
#         if len(string)==0 or len(string)==1:
#                 return string
#         if string[0]=="p" and string[1]=="i":
#                 smallerOutput=replacePi(string[2:])
#                 return "3.14" + smallerOutput
#         else:
#                 smallerOutput=replacePi(string[1:])
#                 return "3.14" + smallerOutput
# print(replacePi("pippi"))

# def removeX(string): 
#     if len(string) == 0:
#         return string
#     smallOutput = removeX(string[1:])
#     if string[0] == 'x':
#         return smallOutput
#     else:
#         return string[0] + smallOutput

# # Main
# string = input()
# print(removeX(string))


# vals=[0,1,2]
# vals.insert(0,1)
# del vals[1]

# def reverseArray(a,start,end):
#         while start<end:
#                 a[start],a[end]=a[end],a[start]
#                 start=start+1
#                 end=end-1
# a=[1,2,3,4,5,6]
# print(a)
# reverseArray(a,0,5)
# print("the reverse array is :")
# print(a)

# def reverseList(A):
#         print(A[::-1])
# A="RItikmdfd"
# print(A)
# print("The reverse list is:")
# reverseList(A)


# import array
# arr=array.array('i',[1,2,3,4,5])
# print("The original array is:",end=" ")
# for i in range(0,5):
#         print(arr[i],end=" ")
# print("\r")
# arr.append(6);
# print("The newest appended array is :",end=" ")
# for i in range(0,6):
#         print(arr[i],end=" ")
# print("\r")
# arr.insert(2,7);
# print("The inserted array of program is :",end=" ")
# for i in range(0,7):
#         print(arr[i],end=" ")
# print("\r")
# arr.pop(2);
# print("The popped list in the array :",end=" ")
# for i in range(0,6):
#         print(arr[i],end=" ")
# print("\r")
# arr2=array.array('i',[1,2,1,3,4,2])
# arr2.remove(1);
# print("Here is the removing array: ",end=" ")
# for i in range(0,5):
#         print(arr2[i],end=" ")
# print("\r")
# print("the index array is : ",end=" ")
# print(arr2.index(3))
# arr2.reverse();
# print("THe reverse array of the element: ")
# for i in range(0,5):
#         print(arr2[i],end=" ")
        

        




# m=int(input("Enter the number to print the rows:"))
# n=int(input("Enter the pattern to print the column:"))
# print("Hollow rectangle star pattern")
# for i in range(m):
#         for j in range(n):
#                 if(i==0 or i==m-1 or j==0 or j==n-1):
#                         print("*",end=" ")
#                 else:
#                         print(" ",end=" ")
#         print()
                        
# def arrayRotate(arr,d,n):
#         for i in range(d):
#                 leftRotateByOne(arr,n)
# def leftRotateByOne(arr,n):
#         temp=arr[0]
#         for i in range(n-1):
#                 arr[i]=arr[i+1]
#         arr[n-1]=temp
# def printArray(arr,size):
#         for i in range(size):
#                 print("% d"% arr[i],end=" ")
# arr=[1,2,3,4,5,6,7]
# arrayRotate(arr,3,7)
# printArray(arr,7)