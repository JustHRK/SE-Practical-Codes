# # PRACTICAL 11:

# a) Write a Python program to store roll numbers of student in array who attended training
# program in random order. Write function for searching whether particular student
# attended training program or not, using Linear search and Sentinel search.

# b) Write a Python program to store roll numbers of student array who attended training
# program in sorted order. Write function for searching whether particular student attended
# training program or not, using Binary search and Fibonacci search

list=[]
def accept(A):
    size=int(input("enter the length of an array:"))
    for i in range(size):
        x=int(input("enter the element of an array:"))
        A.append(x)


def display(A):
    for i in range(len(A)):
        print(A[i])


def linear_search(A):
    key=int(input("enter the key to search:"))
    flag=0
    for i in range(len(A)):
        if (A[i]==key):
            flag=1
    if (flag==1):
        print("key is present.******")
    else:
        print("key is not present.*****")


def binary_search(A):

    print(" enter the  elements ")
    flag=0
    key=int(input("enter the key to search:"))
    start=0
    end=len(A)-1
    mid=int((start+end)/2)
    for i in range(len(A)):
        if (key==A[mid]):
            flag=1
        else:
           
                  if (key>A[mid]):
                      start=mid+1
                      end=len(A)-1
                      mid=int((start+end)/2)
                      if (A[mid]==key):
                          flag=1
                  else:
                      if (key<A[mid]):
                          start=0
                          end=mid-1
                          mid=int((start+end)/2)
                          if (key==A[mid]):
                              flag=1
    if (flag==1):
        print("key is present.*****")
    else:
        print("key is not present.*****")

def sentinal(A):
    n=len(A)
    key=int(input("enter your key:"))
    i=0
    last=A[n-1]
    A[n-1]=key
    while(A[i]!=key):
        i+=1

    A[n-1]=last

    if ((i < n - 1) or (A[n - 1] == key)):
        print(key, "is present at index*****", i)
    else:
        print("Element Not found*******")

def fibogenerator(n):

    if (n<1):
        return 0
    elif (n==1):
        return 1
    else:
        return fibogenerator(n-1)+fibogenerator(n-2)

def fibo_search(arr):
    x=int(input("what you want to search:"))
    m=0
    y="prsent"
    n="not present"
    while(fibogenerator(m)<len(arr)):
        m=m+1
        offset=-1

    while(fibogenerator(m)>1):
        i=min(offset+fibogenerator(m-2),len(arr)-1)

        if (x >arr[i]):
            m=m-1
            offset=i

        elif(x <arr[i]):
            m=m-2

        else:
            return y

    if (fibogenerator(m-1) and arr[offset+1]==x):
        return offset+1
    
    return n

while (True):
    print("")
    print("choice 1=linear search")
    print("choice 2=binray search")
    print("choice 3=sentinal search")
    print("choice 4=fibonacci search")
    print("choice 5=exit.")
    print("")

    ch=int(input("enter your choice: "))
    print(" ")

    if(ch==1):
        accept(list)
        print("")
        linear_search(list)
        print("")
        print("********")
    elif(ch==2):
        accept(list)
        print("")
        binary_search(list)
        print("")
        print("********") 
    elif(ch==3):
        accept(list)
        print("") 
        sentinal(list)
        print("")
        print("********") 
 
    elif(ch==4):
        accept(list)
        b=fibo_search(list)
        print("")
        print(b)
        print("********")
    elif(ch==5):
        print("thanks for using visit again!.")
        break