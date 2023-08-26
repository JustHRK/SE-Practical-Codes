/*
PRACTICAL 26:

In any language program mostly syntax error occurs due to unbalancing delimiter such as
(),{},[]. Write C++ program using stack to check whether given expression is well
parenthesized or not.
*/

#include <iostream>
#include <stack>
using namespace std;
int main() {
    stack<char> brackets;
    string exp;
    cout<<"Enter the Expression : ";cin>>exp;
    for(char ch: exp)
    {
        switch(ch)
            {
            case '(':brackets.push(ch);break;
            case '[':brackets.push(ch);break;
            case '{':brackets.push(ch);break;
            case ')':brackets.pop();break;
            case ']':brackets.pop();break;
            case '}':brackets.pop();break;
            }
    }
    
    if(brackets.empty())
    {
        cout<<"\n The Expression is Well Paranthesized! \n";
    }
    else
    {
        cout<<"\n The Expression is not Well Paranthesized! \n";
    }
    return 0;
}