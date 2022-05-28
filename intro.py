# n=int(input())
# li=[int(x) for x in input().split()]
# print(li)
# ele=int(input())
# isfound=False
# for i in range(len(li)):
#     if li[i]==ele:
#         print(i)
#         isfound=True 
#         break
# if isfound is False:
#     print(-1)

# num=int(input())
# i=1
# while i<=num:
#     print()


# def change(li):
#     li[1] = li[1] + 2
#     li = [3,3,3,4,5]
#     return li
# li = [1,2,3,4,5]
# li=change(li)
# print(li)


# def swapAlternate (li):
#     length =len(li)
#     i = 0
#     for k in range(length//2):
#         li[i],li[i+1]=li[i+1],li[i]
#         i=i+2
#     print(*li,end=" ")
#     print()
# loop_cycle=int(input())
# for i in range(0, loop_cycle):
#     faltu = input()
#     li = [int(x) for x in input().split()]
#     swapAlternate(li)
# import sys
# def findUnique(arr, n) :
#     for i in range(n) :
#         j = 0
#         while j < n :
#             if i != j :
#                 if arr[i] == arr[j] :
#                     break
#             j += 1
#         if j == n : 
#             return arr[i]
# def takeInput() :
#     n = int(input())
#     if n == 0 :
#         return list(), 0
#     arr = list(map(int, input().rstrip().split(" "))) 
#     return arr, n
# t = int(input()) 
# while t > 0 : 
#     arr, n = takeInput()
#     print(findUnique(arr, n)) 
#     t -= 1

#     *
#    **
#   ***
#  ****
# n=int(input("Enter the number to print the pattern:"))
# i=1
# while i<=n:
#     j=1
#     while j<=n-i:
#         print(" ",end="")
#         j=j+1
#     num=1
#     while num<=i:
#         print("*",end="")
#         num=num+1
#     i=i+1
#     print()


#    *
#    **
#    ***
#    ****
#    *****

# n=int(input("Enter the number to print the pattern:"))
# i=1
# while i<=n:
#     j=1
#     while j<=i:
#         print("*",end="")
#         j=j+1
#     i=i+1
#     print()


# n = int(input())
# firstHalf = (n + 1) // 2
# secondHalf = n // 2
# i = 1 
# while i <= firstHalf:
#     spaces = 1 
#     while spaces <= (firstHalf - i) :
#         print(" ", end = "")
#         spaces=spaces+1
#     j = 1
#     while j <= (2 * i) - 1 :
#         print("*", end = "")
#         j=j+1  
#     print()
#     i=i+1
# i = secondHalf 
# while i >= 1 :
#     spaces = 1
#     while spaces <= (secondHalf - i + 1) :
#         print(" ", end = "") 
#         spaces=spaces+1
#     j = 1 
#     while j <= (2 * i) - 1 :
#         print("*", end = "") 
#         j =j+1
#     print()
#     i=i-1
    
    
    
    
# N = int(input())
# while N > 0:
#     x, y = map(int, input().split())
#     sum = x + y
#     print(sum)
#     N = N - 1
    
# T = int(input())
# for tc in range(T):
# 	# Read integers a and b.
# 	(a, b) = map(int, input().split(' '))
# 	ans = a + b
# 	print(ans)


# from sys import stdin
# def binarySearch(arr, n, x) : 
#     start = 0;
#     end = n - 1 
#     mid = start
#     while start <= end :
#         mid = start + (end - start) // 2
#         if arr[mid] > x :
#             end = mid - 1
#         elif arr[mid] < x :
#             start = mid + 1 
#         else : 
#             return mid 
#     return -1
# def takeInput() :
#     n = int(input())
#     if n == 0 :
#         return list(), 0
#     arr = list(map(int, input().strip().split(" "))) 
#     return arr, n
# arr, n = takeInput()
# t = int(input()) 
# while t > 0 : 
#     x = int(input().strip()) 
#     print(binarySearch(arr, n, x)) 
#     t -= 1



#      *
#     ***
#    *****
#     ***
#      * 
# n=int(input("Enter the number to print the pattern:"))
# firsthalf=(n+1)//2
# secondhalf=n//2
# i=1
# while i<=firsthalf:
#     spaces=1
#     while spaces<=(firsthalf-i):
#         print(" ",end="")
#         spaces=spaces+1
#     j=1
#     while j<=(2*i)-1:
#         print("*",end="")
#         j=j+1
#     print()
#     i=i+1
# i=secondhalf
# while i>=1:
#     spaces=1
#     while spaces<=(secondhalf-i+1):
#         print(" ",end="")
#         spaces=spaces+1
#     j=1
#     while j<=(2*i)-1:
#         print("*",end="")
#         j=j+1
#     print()
#     i=i-1


#write a python program for print the numbe pattern
# def numpat(n):
#     num=1
#     for i in range(0,n):
#         num=1
#         for j in range(0,i+1):
#             print(num,end="")
#             num=num+1
#         print()
# n=5
# numpat(n)            

# n=int(input("Enter the number to print the pattern:"))
# i=1
# while i<=n:
#     j=1
#     while j<=n-i+1:
#         print(j,end="")
#         j=j+1
#     print()
#     i=i+1



  #   1
    # 2 3
    # 4 5 6
    # 7 8 9 10
# n=int(input("Enter the number:"))
# k=1
# i=1
# while i<=n:
#     j=1
#     while j<=i:
#         print("{:3d}".format(k),end="")
#         j=j+1
#         k=k+1
#     print()
#     i=i+1        



# n=5
# i=1
# while i<=n:
#     j=n
#     while j>=i:
#         print("*",end="")
#         j=j-1
#     print()
#     i=i+1


# rows=6
# for i in range(1,rows+1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()



# def alphabet(n):
#   num=65
#   for i in range(0,n+1):
#     for j in range(0,i+1):
#       ch=chr(num)
#       print(ch,end="")
#     num=num+1
#     print()
# n=5
# alphabet(n)    


    

# num=65
# i=1
# while i<=num:
#   j=1
#   while j<=num:
#     ch=chr(num)
#     print(ch,end="")
#     num=num+1
#   j=j+1
# print()  
# i=i+1

# n=5
# li=[]
# for i in range(n):
#   curr=int(input("Enter the number to print the list:"))
#   li.append(curr)
# print(li)

# def swapalternate(li):
#   length=len(li)
#   i=0
#   for k in range(length//2):
#     li[i],li[i+1]=li[i+1],li[i]
#     i=i+2
#   print(*li,end="")
#   print()
# loop=int(input())
# for i in range(0,loop):
#   faltu=input()
#   li=[int(x) for x in input().split()]
#   swapalternate(li)


# n=5
# li=[]
# for i in range(n):
#       curr=int(input("ENter the number to print the list:"))
#       if curr==5:
#             continue
#       li.append(curr)
# print(li)


# from sys import stdin

# def bubbleSort(arr, n) :
#     #Your code goes here
#       for i in range(n - 1) :
#         for j in range(n - i - 1) :
#             if arr[j] > arr[j+1] :
#                 arr[j],arr[j+1]=arr[j+1],arr[j] 
# #Taking Input Using Fast I/O
# def takeInput() :
#     n = int(stdin.readline().strip())
#     if n == 0 :
#         return list(), 0

#     arr = list(map(int, stdin.readline().strip().split(" ")))
#     return arr, n
# #to print the array/list
# def printList(arr, n) : 
#     for i in range(n) :
#         print(arr[i], end = " ")
#     print()
# #main
# t = int(stdin.readline().strip())
# while t > 0 :
#     arr, n = takeInput()
#     bubbleSort(arr, n)
#     printList(arr, n)
#     t=t-1

# from sys import stdin

# def insertionSort(arr, n) :
    
#     #Your code goes here
#     for i in range(len(arr)):
#         for j in range(len(arr)-1):
#             if arr[j]>arr[j+1]:
#                 arr[j],arr[j+1]=arr[j+1],arr[j]		
#     return arr
# #Taking Input Using Fast I/O
# def takeInput() :
#     n = int(stdin.readline().strip())
#     if n == 0 :
#         return list(), 0
#     arr = list(map(int, stdin.readline().strip().split(" ")))
#     return arr, n
# #to print the array/list
# def printList(arr, n) : 
#     for i in range(n) :
#         print(arr[i], end = " ")
        
#     print()
# #main
# t = int(stdin.readline().strip())
# while t > 0 :
#     arr, n = takeInput()
#     insertionSort(arr, n)
#     printList(arr, n)

#     t-= 1

# s=input()
# p=s[::-1]
# if(s==p):
#     print("true")
# else:
#     print("false")

# a = "abce" >= "abcdef"
# print(a)
# def replace(str,char1,char2):
#     newstr=""
#     for char in str:
#         if (char==char1):
#             newstr+=char2
#         else:
#             newstr+=char
#     return newstr           
# str="abcdeabanao"
# str=replace(str,"a","z")
# print(str)


# from itertools import count
# def countInString(str):
#     v,c,d,s=0,0,0,0
#     for char in str:
#         if ((char>="a" and char<="z") or (char>="A" and char<="Z")):
#             char=char.lower()
#             if(char=="a" or char=="e" or char=="o" or char=="i" or char=="u"):
#                 v+=1
#             else:
#                 c+=1
#         elif(char>="0"or char<="9"):
#             d+=1
#         else:
#             s+=1
#     return v,c,d,s
# str="aksdjnasanjdsdjiuiooaido1213@#@#JW"
# type(str[0])
# v,c,d,s=countInString(str)
# print(v,c,d,s)

# def arePermutation(str1, str2):
    
#     n1 = len(str1) 
#     n2 = len(str2)
#     if (n1 != n2):
#         return False
  
#     # Sort both strings 
#     a = sorted(str1) 
#     str1 = "".join(a) 
#     b = sorted(str2) 
#     str2 = "".join(b) 
  
#     # Compare sorted strings 
#     for i in range(0, n1, 1): 
#         if (str1[i] != str2[i]): 
#             return False
  
#     return True
  
# str1 = input()
# str2 = input()
# if (arePermutation(str1, str2)):
#     print("true") 
# else: 
#     print("false")


#write a python program for delete the consecutive duplicate character in a given string
# import itertools        
# def censecutive(s1):
#     return(''.join(i for i, _ in itertools.groupby(s1)))
# s1=input()
# print(censecutive(s1))

#write a python program for print the reverse of the given string 
# s=input()
# nw=s[::-1]
# print(nw)

# def reverseword(s): 
   
#    w = s.split(" ")        
                           
#    nw= [i[::-1] for i in w]
                          
#    ns = " ".join(nw)
#    return ns
# # Driver's Code 

# s = input()
# w = s.split(" ")               
# nw= [i[::-1] for i in w]                      
# ns = " ".join(nw)
# print(ns)

#write a python program for search the selection sort in python lanaguage
# def selection_sort(Arr):
#       for i in range(len(Arr)):
#             min_index=i
#             for j in range(i+1,len(Arr)):
#                   if Arr[j] <Arr[min_index]:
#                         min_index=j
#             Arr[i],Arr[min_index]=Arr[min_index],Arr[i]
#       return Arr
# selection_sort([13,4,9,5,3])
# print(selection_sort)

# s=input()
# ch=input()
# print(s.replace(ch, ''))

# from hashlib import new


# li=[1,2,3,4,5]
# li_new_c=[ele**2 for ele in li if ele%2==0]
# print(li_new_c)


# li = [ele**2 for ele in range(5) if ele%3 ==0]
# print(li)

# li = [[ i*j for j in range(4)] for i in range(3)]
# print(li)

# from re import M


# str=input().split()
# n,m=int(str[0]),int(str[1])
# li=[[int(j)for j in input().split()]for i in range(n)]
# print(li)


  
#write a python program for print the divisible of two 
# li=[1,2,3,4,5,6]
# new_list=[ele**2 for ele in li if ele%2==0]
# print(new_list)

#write a python program for print the divisible of 5
# li=[ele**2 for ele in range(11) if ele%5==0]
# print(li)
# a = ("ab","abc","def")
# print(min(a))
# def sum_multiply(a,b,*more):
#     sum_value = a+b
#     m_value = a*b
#     for i in more:
#         sum_value += i
#         m_value*=i
#     return sum_value,m_value
# s_m = sum_multiply(2,3,4)
# print(s_m)
# d = {1:2, "abc":5, "def":7}
# print(d[0])

# a = {1:2,"list":[1,2],3:5}
# b = {4:5,3:7}
# a.update(b)
# print(a[3])

# my_list=[1,2,3,4,5]
# clone=my_list[:]
# print(clone)


# s = {1,2,3,5,4,2,3,1}
# print(len(s),end= "  ")
# s.add(4)
# s.add(3)
# print(len(s))
# s = {1,2,3,5,4,2,3,1}
# print(len(s))

# s=input().split()
# l=[]
# for i in s:
#     l.append(len(i))
# print(s[l.index(min(l))])
# n=int(input())
# def fact(n):
#   if n==0:
#     return 1
#   return n * fact(n-1)
# fact(n)
# n=input().split()
# def sumOrProduct(n, q):
#     if(q==1):
#         ans=(n*(n+1))//2 
#         return ans
#     else:
#         m=1
#         opt=1000000007 
#         while(n):
#             m=m*n
#             n=n-1
#         return m%opt
# print(sumOrProduct(4,1))
# print(sumOrProduct(4,2))

# def sumOrProduct(n, q):
    
#     answer = 0
#     mod = int(1e9) + 7

#     if q == 1:

#         # Sum of first 'N' numbers is given by
#         # 'N' * 'N + 1' / 2.
#         answer = (n * (n + 1)) // 2

#     else:
#         answer = 1
#         for i in range(1, n + 1):
#             # Modular Arithmatic.
#             i %= mod
#             answer %= mod
#             answer = (((answer * i) % mod) + mod) % mod

#     return answer
# def powerof(a, b):
#     results=1
#     for n in range(b):
#         results=results*a
#     return results
# a,b=input().split()
# a=int(a)
# b=int(b)
# print(powerof(a, b))


# def n_to_1(n):
#       if n==0:
#     return
#   print(n)
#   n_to_1(n)
#   return
# n=4
# # print(n_to_1)
# n=4
# def print_1_to_n(n):
#   if n==0:
#     return
#   print_1_to_n(n-1)
#   print(n)
#   return

# def fun(n):
#   if n==4:
#     return n
#   else:
#     return 2*fun(n+1)
# print(fun(2))


#python program for print the list is sorted or not by the help of recursion
# def issorted(a):
#       l=len(a)
#       if l==0 or l==1:
#             return True
#       if a[0] > a[1]:
#             return False
#       smaller_list=a[1:]
#       issmallerListSorted= issorted(smaller_list)
#       if issmallerListSorted:
#             return True
#       else:
#             return False
# a=[1,2,3,4,5,6,7]
# print(issorted(a))

#wrtie a pyton program for print the sum of all the number in aray
# def sumarray(a):
#       if len(a)==0:
#             return 0
#       else:
#             return a[0] + sumarray(a[1:])
            
# n=int(input())

# a=list(int(i) for i in input().strip().split(' '))
# print(sumarray(a))


#writea python program for check the lsit is sorted or not 

# def issortedbetter(a,si):
#       l=len(a)
#       if si==l-1 and si==l:
#             return True
#       if a[si]>a[si+1]:
#             return False
#       issmallersorted=issortedbetter(a,si+1)
#       return issmallersorted
# a=[1,2,3,4,5,6,7,8,9]
# print(issortedbetter(a,0))


#write a python program for find the first index of the number 
# def firstIndex(a,x):
#       l=len(a)
#       if l==0:
#             return -1
#       if a[0]==x:
#             return 0
#       smallerList= a[1:]
#       smallerListOutput=firstIndex(smallerList,x)
#       if smallerListOutput==-1:
#             return -1
#       else:
#             return smallerListOutput+1
# a=[1,2,3,4,5,6,7,8]
# print(firstIndex(a,7))

#another example of finding the frst index of the number 
# def firstIndex(a,x,si):
#       l=len(a)
#       if si==l:
#             return -1
#       if a[si]==x:
#             return si
#       smallerOutput=firstIndex(a,x,si+1)
#       return smallerOutput
# a=[1,3,5,7,8,4,3]
# print(firstIndex(a,8,0))

def lastIndex(a,x):
      l=len(a)
      if l==0:
            return -1
      if a[l-1]==x:
            return 0
      smallerList=a[:-1]
      smallerListOutput=lastIndex(smallerList,x)
      if smallerListOutput == -1:
            return -1
      else:
            return smallerListOutput +1
a=[1,2,3,4,3,1,5]
print(lastIndex(a,1))      
            
      
            
