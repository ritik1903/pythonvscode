# def reverseArray(arr,n):
#     i=0
#     j=n-1
#     while i!=j:
#         arr[i],arr[j]=arr[j],arr[i]
#         i=i+1
#         pass
# arr=[1,2,3,4,5,6]
# n=len(arr)
# print("The given array is : ")
# for i in range(0,n):
#     print(arr[i],end=" ")
# reverseArray(arr,n)
# print("\nRotate array is: \n")
# for i in range(0,n):
#     print(arr[i],end=" ")


#another approach
# def reverseArray(array):
#     array[:]=array[-1:] +  array[:-1]
# array=[1,2,3,4,5] 
# reverseArray(array)
# print(array) 

