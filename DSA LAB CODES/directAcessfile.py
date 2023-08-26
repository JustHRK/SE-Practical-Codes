file={}

def InsertData():
    roll_num=input("Enter Student Roll Number : ")
    name=input("Enter Student Name : ")
    div=input("Enter Student Division : ")
    addr=input("Enter Student Address : ")

    record ={"roll_num":roll_num,"name":name,"division":div, "address":addr}

    file[roll_num]=record
    print("Record Added Successfully!\n")

def DeleteData():
    roll_num=input("Enter Roll Number to delete Data : ")

    if(roll_num in file):
        del file[roll_num]
        print("Record Deleted Succesfully!\n")
    else:
        print("Record Not Found!\n")

def PrintData():
    roll_num=input("Enter Roll number to Display Data : ")

    if(roll_num in file):
        r=file[roll_num]
        print(f"Roll Numer : {roll_num}")
        print(f"Name : {r['name']}")
        print(f"Division : {r['division']}")
        print(f"Address : {r['address']}\n")
    else:
        print("Record Not Found!\n")

#MAIN BODY
while(True):
    print("""Direct File Access
1. Insert Data
2. Delete Data
3. Display Data
4. Exit 
""")
    ch=int(input("Enter Your Choice : "))
    if(ch==1):
        InsertData()
    elif(ch==2):
        DeleteData()
    elif(ch==3):
        PrintData()
    elif(ch==4):
        break
    else:
        print("Invalid Input !\n")