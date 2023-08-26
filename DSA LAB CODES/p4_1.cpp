#include<iostream>
#include<stack>     
using namespace std;

struct Node
{
    char data;
    Node* right;
    Node* left;
};

Node* NewNode(char d)
{
    Node* node=new Node;
    node->data=d;
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
    if (root==NULL)
        return;
        
    stack<Node*> st;
    Node* curr=root;
    
    while(!st.empty() || curr!=NULL)
    {
        if(curr!=NULL)
        {
            st.push(curr);
            curr=curr->left;
        }
        else
        {
            Node* temp=st.top()->right;
            if(temp==NULL)
            {
                temp=st.top();
                st.pop();
                cout<<temp->data<<"  ";
                while(!st.empty() && temp==st.top()->right )
                {
                    temp=st.top();
                    st.pop();
                    cout<<temp->data<<"  ";
                }
            }
            else
            {
                curr=temp;
            }
        }
    }
}

void DeleteTree(Node* root)
{
    if(root==NULL)
    {
        return;
    }
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
    Node* root =ConstructTree(prefix);
    
    cout<<"Post Order Traversal : ";
    PostOrder(root);
    cout<<endl;
    DeleteTree(root);
    return 0;
}
