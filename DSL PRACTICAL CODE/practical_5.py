# PRACTICAL 5:

# Write a Python program to compute following operations on String:
# a) To display word with the longest length
# b) To determines the frequency of occurrence of particular character in the string
# c) To check whether given string is palindrome or not
# d) To display index of first appearance of the substring
# e) To count the occurrences of each word in a given string

def longest(line):
    lst=line.split()
    long=lst[0]
    for i in range (len(lst)):
        if(len(long)<len(lst[i])):
            long=lst[i]
    print(long)

def occurence(line):
    x=input("Enter the Character to be searched:")
    print("Occurence:",line.count(x))

def palindrome(line):
    x=line[::-1]
    if(line==x):
        print("PALINDROME")
    else:
        print("NOT PALINDROME")

def findl(line):
    x=input("Enter Substring:")
    print("Found at:",line.find(x))

def eachOccurence(line):
    lst=(line.split())
    for i in range (len(lst)):
        print(lst[i]," : ",line.count(lst[i]))
flag="yes"
line=input("Enter the String:\n")
while(flag=="yes"):    
    print("""Choose Operation:
    1. To display word with the longest length
    2. To determines the frequency of occurrence of particular character in the string
    3. To check whether given string is palindrome or not
    4. To display index of first appearance of the substring
    5. To count the occurrences of each word in a given string""")
    ch=int(input("Option:"))
    if(ch==1):
        longest(line)
    if(ch==2):
        occurence(line)
    if(ch==3):
        palindrome(line)
    if(ch==4):
        findl(line)
    if(ch==5):
        eachOccurence(line)
    flag=input("Do You wish to Continue ? (yes/no) : ") 
