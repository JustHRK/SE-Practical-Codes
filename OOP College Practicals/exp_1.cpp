/*
EXPERIMENT 1:

Implement a class Complex which represents the Complex Number data type. Implement the
following
1. Constructor (including a default constructor which creates the complex number 0+0i).
2. Overload operator+ to add two complex numbers.
3. Overload operator* to multiply two complex numbers.
4. Overload operators << and >> to print and read Complex Numbers.
*/

#include<iostream>
using namespace std;

class complex{
int x,y;
public:
complex()
{
    x=0;
    y=0;
}

    friend void operator>>(complex &a ,complex &b)
    {
        cout<<"Enter Value of (x1):";
        cin>>a.x;
        cout<<"Enter Value of (y1):";
        cin>>a.y;
        cout<<"Enter Value of (x2):";
        cin>>b.x;
        cout<<"Enter Value of (y2):";
        cin>>b.y;
    }

    friend void operator<<(complex &a, complex &b)
    {
        cout<<"First Complex No. ("<<a.x<<" + "<<a.y<<"i )"<<endl;
        cout<<"Second Complex No. ("<<b.x<<" + "<<b.y<<"i )"<<endl;
    }

    friend void operator+(complex &a, complex &b)
    {
        complex add;
        add.x=a.x+b.x;
        add.y=a.y+b.y;
        if(add.y> 0)
            cout<<"Addition of Complex No. ="<<add.x<<" + "<<add.y<<"i"<<endl;
        else
            cout<<"Addition of Complex No. ="<<add.x<<" - "<<(-1)*add.y<<"i"<<endl;
    }

    friend void operator-(complex &a, complex &b)
    {
        complex sub;
        sub.x=a.x-b.x;
        sub.y=a.y-b.y;
        if(sub.y> 0)
            cout<<"Subtraction of Complex No. ="<<sub.x<<" + "<<sub.y<<"i"<<endl;
        else
            cout<<"Subtraction of Complex No. ="<<sub.x<<" - "<<(-1)*sub.y<<"i"<<endl;
    }

    friend void operator*(complex &a,complex &b)
    {
        complex mul;
        mul.x=(a.x*b.x)-(a.y*b.y);
        mul.y=(a.x*b.y)+(b.x*a.y);
        if(mul.y> 0)
            cout<<"Multiplication of Complex No. ="<<mul.x<<" + "<<mul.y<<"i"<<endl;
        else
            cout<<"Multiplication of Complex No. ="<<mul.x<<" - "<<(-1)*mul.y<<"i"<<endl;
    }
};

int main()
{
    char des;
    char ch;
    complex s1,s2;
    operator>>(s1,s2);
    operator<<(s1,s2);
    do
    {
        cout<<"Choose Operation:\n"
                "+ : Addition\n"
                "- : Subtraction\n"
                "* : Multiplication\n"
                "Enter Choice:";cin>>ch;
            
        switch(ch)
        {
            case '+':s1+s2; break;
        
            case '-':s1-s2; break;

            case '*':s1*s2; break;

            default:cout<<"Invalid Choice!\n";
        }
        cout<<"Do you want to continue (y/n) :"; cin>>des;
    
    } while (des=='y');
    return 0;
}
