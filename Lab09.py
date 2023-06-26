#arr=Array
#low = start index
#high= End index
#x=search value
#mid=mid index


arr=[]
for v in range(4):
    arr.append(int(input('Enter a number:')))
print (arr)

x=int(input('Enter a  search number:'))

def binary_search(arr,low,high,x):
    #check base case
    if high>=low:

        mid=(high+low)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]>x:
            return binary_search(arr,low,mid-1,x)
        else:
             return binary_search(arr,high,mid+1,x)
    else:
        return -1
#function call
result = binary_search(arr,0,len(arr)-1,x)

if result !=-1:
    print('Element is present at index',str(result))
else:
    print('Element is not present at array')
            
