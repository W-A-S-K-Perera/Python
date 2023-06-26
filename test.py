#A=[]
#for v in range(1,8):
 #   A.append(int(input('Enter number:')))
  #  print(A)
#def bubbleSort(A):
 #   n=len(A)
  #  for i in range(1,n):
   #     for j in range (1,n-i+1):
    #        if A[j]<A[j-1]:
     #           A[j],A[j-1]=A[j-1],A[j]
#bubbleSort(A)
#print('Sorted Array',A)

A=[]
n=9
for i in range(0,n):
    number=int(input('Enter number:'))
    A.append(number)
def insertionSort(A):
    for j in range(1,n):
        key=A[j]
        i=j-1
        while i>0 and key<A[i]:
            A[i+1]=A[i]
            i=i-1
        A[i+1]=key
insertionSort(A)

A=[]
for v in range(8):
    A.append(int(input('Enter number:')))
    print(A)

def selectionSort(A):
    n=len(A)
    for j in range(0,n-1):
        small=j
        for i in range(j+1,n):
            if A[i]<A[small]:
                small=i
                A[j],A[small]=A[small],A[j]




A=[]
for v in range(7):
    A.append(input('Enter number:'))
    print(A)
def partition(A,low,high):
    pivot=A[high]
    i=(low-1)
    for j in range(low,high):
        if A[j]<=pivot:
            i=i+1
            A[i],A[j]=A[j],A[i]
            A[i+1],A[high]=A[high],A[i+1]
            return (i+1)


def quickSort(A,low,high):
    if low<high:
        q=partition(A,low,high)
        quickSort(A,low,q-1)
        quickSort(A,q+1,high)
    quickSort(A,0,len(A)-1)
    print('Sorted Array:')
    for i in range(len(A)):
        print(A[i])



A=[]
for v in range(4):
    A.append(int(input('Enter nuber:')))
    print(A)

    x=int((input('Enter serch value:')))
def binary_search(A,low,high,x):
    if high>=low:
        mid=(high+low)//2
        if A[mid]==x:
            return mid
        elif A[mid]>x:
            return binary_search(A,low,mid-1,x)
        else :
            return binary_search(A,high<mid+1,x)
    else:
        return -1

    result=binary_search(A,0,len(A)-1,x)

    if result!=-1
        























        


















                

        
