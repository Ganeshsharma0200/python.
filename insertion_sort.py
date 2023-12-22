import numpy as np
# length = int(input("Enter the length of arrary\n"))
list = []
n= int(input("Enter the no. Elements of array\n"))
for i in range(n):
    print("Enter number",i+1,"Elements")
    e=input()
    list.insert(i,e)
arr = np.array(list)
print(arr)

for j in range(1,n):
    key = arr[j]
    i=j-1
    while(i>=0 and arr[i]>key):
        arr[i+1]=arr[i]
        i=i-1
    arr[i+1]=key

print(arr)