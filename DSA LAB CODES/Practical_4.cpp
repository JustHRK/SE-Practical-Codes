// Aim: Construct an expression tree from the given prefix expression eg. +--a*bc/def and traverse it using post order traversal (non recursive) and then delete the entire tree.

#include<iostream>
#include<stack>
using namespace std;

struct Node
{
    char data;
    Node* left;
    Node* right;
};

Node* NewNode(char data)
{
    Node* node=new Node;
    node->data=data;
    node->left=NULL;
    node->right=NULL;
    return node;
}

Node* ConstructTree(string prefix)
{
    int len=prefix.length();
    stack<Node*> st;

    for(int i=len-1;i>=0;i--)
    {
        char ch=prefix[i];
        if(isalnum(ch))
            st.push(NewNode(ch));
        else
        {
            Node* node=NewNode(ch);
            node->left=st.top();
            st.pop();
            node->right=st.top();
            st.pop();
            st.push(node);
        }
    }
    return st.top();
}

void PostOrder(Node* root)
{
    if(root==NULL)
        return;
    
    stack<Node*> st;
    Node* current=root;

    while(!st.empty() || current!=NULL)
    {
        if(current!=NULL)
        {
            st.push(current);
            current=current->left;
        }
        else
        {
            Node* temp=st.top()->right;
            if(temp==NULL)
            {
                temp=st.top();
                st.pop();
                cout<<temp->data<<" ";
                while(!st.empty() && temp==st.top()->right)
                {
                    temp=st.top();
                    st.pop();
                    cout<<temp->data<<" ";
                }
            }
            else{
                current=temp;
            }
        }
    }
}

void DeleteTree(Node* root)
{
    if(root==NULL)
        return;
    else
    {
        DeleteTree(root->left);
        DeleteTree(root->right);
        delete root;
    }
}

int main()
{
    string prefix="+--a*bc/def";
    Node* root=ConstructTree(prefix);
    
    cout<<"Postorder Traversal : ";
    PostOrder(root);
    cout<<endl;
    DeleteTree(root);
    return 0;
}