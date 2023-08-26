#Aim: Implement all the functions of a dictionary (ADT) using hashing and handle collisions using chaining with / without replacement.

class Node:
    def __init__(self,val=None):
        self.value=val
        self.next=None

    def __repr__(self):
        return str(self.value)

def printTable(dct):
    lst=list(dct.values())
    for i in lst:
        while(i!=None):
            print(i.value,end=" ")
            i=i.next
        print()

def hash_func(x):
    return(x%n)

def insert(i):
    hk=hash_func(i)
    if hk not in hash_table.keys():
        hash_table.update({hk:Node(i)})
    else:
        while(hash_table[hk].next!=None):
            hash_table[hk]=hash_table[hk].next
        hash_table[hk].next=Node(i)

hash_table=dict()
n=10

keys=[15,11,27,8,4,3,45,22]

for i in keys:
    insert(i)

print(printTable(hash_table))
print(hash_table)
