# Aim :To create ADT that implement the "set" concept. a. Add (new Element) -Place a value into the set , b. Remove (element) Remove the value c. Contains (element) Return true if element is in collection, d. Size () Return number of values in collection Iterator () Return an iterator used to loop over collection, e. Intersection of two sets , f. Union of two sets, g. Difference between two sets, h. Subset

class Set:
    def __init__(self,lst):
        lst1=[]
        for i in lst:
            if(i not in lst1):
                lst1.append(i)
        self.values=lst1
        print("Set : ",self.values)

    def Add(self,x):
        if(x not in self.values):
            self.values.append(x)
        print(f"{x} added to the set")
        print("Updated Set : ",self.values)

    def Remove(self,x):
        if(x in self.values):
            self.values.remove(x)
            print(f"{x} is Removed from the Set")
            print("Updated Set : ",self.values)
        else:
            print(f"{x} is not in the set")

    def Contains(self,x):
        return (x in self.values)    
    
    def Size(self):
        return (len(self.values))
    
    def Iterator(self):   
        return iter(self.values)
        
    def Intersection(self,set2):
        lst=[]
        lst1=self.values
        lst2=set2.values
        for i in lst1:
            if(i in lst2):
                lst.append(i)
        return lst
    
    def Union(self,set2):
        lst=self.values
        lst2=set2.values
        for i in lst2:
            if(i not in lst):
                lst.append(i)
        return lst
    
    def Difference(self,set2):
        lst=[]
        lst1=self.values
        lst2=set2.values
        for i in lst1:
            if(i not in lst2):
                lst.append(i)
        return lst
    
    def Subset(self,set2):
        lst=self.values
        lst2=set2.values
        for i in lst2:
            if(i not in lst):
                return False
        return True

my_set=Set([15,11,27,8,4,3,45,22,15])
my_set.Add(6)
my_set.Remove(27)
print(my_set.Contains(6))
print(my_set.Size())
print(my_set.Iterator())