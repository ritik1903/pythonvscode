def linearSearch(list,length,element):
    for i in range(0,length):
        if list[i] == element:
            return i
list=[10,20,30,40,50,60]
element=int(input("Enter the value which you have to get in the list:"))
length=len(list)
result=linearSearch(list,length,element)
if result == -1:
    print("The element {} is not found".format(element))
else:
    print("The element {} is found at {}".format(element,result))