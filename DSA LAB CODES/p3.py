class Node:
	def __init__(self,n):
			self.name=n
			self.children=[]
	def add_child(self,x):
			self.children.append(x)
	def __repr__(self):
			return (self.name)

def print_tree(root,level=0):
		print("   "*level,root)
		for child in root.children:
				print_tree(child,level+1)

book=Node("Book")
ch1=Node("Chapter 1")
ch2=Node("Chapter 2")
s1=Node("Section 1")
s2=Node("Section 2")
ss11=Node("Subsection 1.1")
ss12=Node("Subsection 1.2")
ss21=Node("Subsection 2.1")
ss22=Node("Subsection 2.2")

book.add_child(ch1)
book.add_child(ch2)
ch1.add_child(s1)
ch2.add_child(s2)
s1.add_child(ss11)
s1.add_child(ss12)
s2.add_child(ss21)
s2.add_child(ss22)

print_tree(book)