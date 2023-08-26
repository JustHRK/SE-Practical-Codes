FileName="Student_data.txt"
RecordSize=100

def Add_student_data():
    roll_num=input("Enter Student Roll Number : ")
    name=input("Enter Student Name : ")
    div=input("Enter Student Div. : ")
    addr=input("Enter Student Address : ")
    record=f"{roll_num},{name},{div},{addr}\n"
    with open(FileName,"a") as f:
        f.writelines(record)
    print("Student Info Added Successfully!\n")

def Delete_Student_data():
    roll_num=input("Enter Roll Number to be Deleted : ")
    updated=[]

    with open (FileName,"r") as f:
        records=f.readlines()
    flag=False
    for r in records:
        if(r.startswith(roll_num+",")):
            flag=True
        else:
            updated.append(r)

    with open (FileName,"w") as f:
        f.writelines(updated)

    if(flag):
        print("Student Info Deleted!\n")
    else:
        print("Student Data Not Found!\n")

def Display_Student_data():
    roll_num=input("Enter Roll Number to be Displayed : ")
    flag=False
    with open (FileName,"r") as f:
        records = f.readlines()

    for r in records:
        if(r.startswith(roll_num+",")):
            flag=True
            r=r.strip().split(",")
            print("Roll Number : ",r[0])
            print("Name : ",r[1])
            print("Division : ",r[2])
            print("Address : ",r[3])
            break
    if(not flag):
        print("Student Info Not Found!\n")

#MAIN BODY
while(True):
    print("-----STUDENT RECORDS MANAGER-----")
    print("""Choose Your Operation :
    1. Add new Student Data
    2. Delete Student Data
    3. Display Student Data
    4. Exit""")
    ch=int(input("Enter Choice : "))
    if(ch==1):
        Add_student_data()
    elif(ch==2):
        Delete_Student_data()
    elif(ch==3):
        Display_Student_data()
    elif(ch==4):
        break
    else:
        print("Invalid Input")