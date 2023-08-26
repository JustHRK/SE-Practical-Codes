class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def construct_tree(prefix):
    st=[]
    for i in range(len(prefix)):
        ch=str(prefix[i])
        if(ch.isalnum()):
            st.append(Node(ch))
        else:
            n=Node(ch)
            n.left=st[-1]
            st.pop()
            n.right=st[-1]
            st.pop()
            st.append(n)
        
    return st[-1]

def post_order(root):
    if(root==None):
        return
    
    st=[]
    curr=root

    while(not st or curr!= None):
        if(curr!=None):
            st.append(curr)
            curr=curr.left
        else:
            temp=st[-1].right
            if(temp==None):
                temp=st[-1]
                st.pop()
                print(temp.data ,end=" ")
                while( not st and temp==st[-1].right):
                    temp=st[-1]
                    st.pop()
                    print(temp.data ,end = " ")   
            else:
                curr=temp

def delete_tree(root):
    if(root==None):
        return
    else:
        delete_tree(root.left)
        delete_tree(root.right)
        del root

# MAIN Body

prefix="=+--a*bc/def"
root=construct_tree(prefix)
print("Post Order Traversal : ")
post_order(root)
delete_tree(root)