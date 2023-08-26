#Problem Statement: A book consists of chapters, chapters consist of sections and sections consist of subsections. Construct a tree and print the nodes. Find the time and space requirements of your method in python.

class Node:
    def __init__(self,name):
        self.name=name
        self.children=[]
    
    def add_child(self,x):
        self.children.append(x)
    
    def __repr__(self):
        return self.name
        #If this function is not used, print(book) :-<__main__.Node object at 0x00000163DF2F5810>
        #With this Function, print(book) will print :- book
    
def printTree(root,level=0):
    print("   "*level,root.name)
    for child  in root.children:
        printTree(child,level+1)

book=Node("Book")
chapter_1=Node("Chapter 1")
chapter_2=Node("Chapter 2")
section_1_1=Node("Section 1.1")
section_1_2=Node("Section 1.2")
section_2_1=Node("Section 2.1")
section_2_2=Node("Section 2.2")
subsection_1_1_1=Node("Subsection 1.1.1")
subsection_1_2_1=Node("Subsection 1.2.1")
subsection_2_1_1=Node("Subsection 2.1.1")

book.add_child(chapter_1)
book.add_child(chapter_2)
chapter_1.add_child(section_1_1)
chapter_1.add_child(section_1_2)
section_1_1.add_child(subsection_1_1_1)
section_1_2.add_child(subsection_1_2_1)
chapter_2.add_child(section_2_1)
chapter_2.add_child(section_2_2)
section_2_1.add_child(subsection_2_1_1)

printTree(book)
# printTree(chapter_1) :- We can access subtrees like this 