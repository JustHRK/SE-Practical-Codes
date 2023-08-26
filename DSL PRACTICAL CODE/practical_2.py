# PRACTICAL 2:

# Write a Python program to store marks scored in subject “Fundamental of Data Structure” by
# N students in the class. Write functions to compute following:
# a) The average score of class
# b) Highest score and lowest score of class
# c) Count of students who were absent for the test
# d) Display mark with highest frequency

def avg(arr,n):
    avg=0
    for i in arr:
        avg+=i
    print(f"Average Marks of Class : {(avg//n)}")

def  highestAndLowest(arr):
    print("Highest Score : ",max(arr))
    print("Lowest Score : ",min(arr))

def absent(n):
    u=int(input("Total Students in Class : "))
    if(u>=n):
        print("Absent Students : ",(u-n))
    else:
        print("Invalid Input")

def highestFreq(arr):
    f=0
    y=0
    for i in arr:
        x=arr.count(i)
        if(x>y):
            y=x
            f=i
    print(f"Marks with Highest Frequency : {f}")
    

marks=[]
n=int(input("Enter Number of Students : "))
for i in range(n):
    x=int(input(f"Enter Marks of Student {i+1} : "))
    marks.append(x)

avg(marks,n)
highestAndLowest(marks)
absent(n)
highestFreq(marks)