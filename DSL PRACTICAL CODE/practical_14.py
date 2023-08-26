# PRACTICAL 14:

# Write a Python program to store first year percentage of students in array. Write function for
# sorting array of floating point numbers in ascending order using
# a) Selection Sort
# b) Bubble sort and display top five scores.

def bubbleSort(arr, n):
    for i in range(n-1):
        for j in range (n-1):
            if(arr[j]>arr[j+1]):
                temp=arr[j+1]
                arr[j+1]=arr[j]
                arr[j]=temp
    return arr

def selectionSort(arr,n):
    for i in range (n):
        min_ind=i
        for j in range(i,n):
            if(arr[min_ind]>arr[j]):
                temp=arr[min_ind]
                arr[min_ind]=arr[j]
                arr[j]=temp
    return arr 

marks=[]
n=int(input("Enter No. of students: "))
for i in range (n):
    x=float(input(f"Enter Percentage of Student {i+1} : "))
    marks.append(x)

print(f"Unsorted Array : {marks}")
print(f"Selection Sorted Array : {selectionSort(marks,n)}")
print(f"Bubble Sorted Array : {bubbleSort(marks,n)}")

print("Top Five Scores:")
arr=bubbleSort(marks,n)
print(arr[-1:-6:-1])