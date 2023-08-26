class Employee:
    edict={"ID":"" ,"Name":"" ,"Salary":0 }
    def Create(self):
        self.edict["ID"]=input("Enter Employee ID : ")
        self.edict["Name"]=input("Enter Employee Name : ")
        self.edict["Salary"]=int(input("Enter Salary : "))

    def Display(self):
        print("ID : ",self.edict["ID"])
        print("Name : ",self.edict["Name"])
        print("Salary : ",self.edict["Salary"])

    def Modify(self):
        ch=int(input("Choose to Modify : \n 1.ID \n 2.Name \n 3.Salary \n Choice :"))

        if(ch==1):
            x=(input("Enter new ID : "))
            self.edict["ID"]=x
        
        elif(ch==2):
            x=(input("Enter new Name : "))
            self.edict["Name"]=x

        elif(ch==3):
            x=int(input("Enter new Salary : "))
            self.edict["Salary"]=x

        else:
            print("INVALID INPUT!")


n=int(input("Enter Number of Employees :"))
emp=Employee()
elist=[]
for i in range (n):
    emp.Create()
    elist.append(emp)

print("--------------------- Employee Details : ---------------------")
for e in elist:
    e.Display()
    
elist[1].Modify()
elist[1].Display()
    
a=int(input("Enter Employee Index to Delete : "))
elist.remove(elist[a])