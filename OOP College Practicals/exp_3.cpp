/*
EXPERIMENT 3:

Imagine a publishing company which does marketing for book and audio cassette versions.
Create a class publication that stores the title (a string) and price (type float) of publications.
From this class derive two classes: book which adds a page count (type int) and tape which adds
a playing time in minutes (type float).
Write a program that instantiates the book and tape class, allows user to enter data and displays
the data members. If an exception is caught, replace all the data member values with zero
values.
*/
#include<iostream>
#include<string.h>
using namespace std;

class Publication
{
    protected:
    string title;
    float price;
    public:
    void SetZero()
    {
        title="000";
        price=0.0;
    }

    void InData()
    {
        cout<<"Enter Title : ";
        cin>>title;
        cout<<"Enter Price : ";
        cin>>price;
    }

    void OutData()
    {
        cout<<"Name of Book : "<<title<<endl
            <<"Price : "<<price<<endl;
    }
};

class Book : public Publication
{
    int page_count;
    public:
    void SetZero()
    {
        page_count=0;
        Publication::SetZero();
    }

    void InData()
    {
        Publication::InData();
        cout<<"Enter Number of Pages : ";cin>>page_count;
        try
        {
            if(price<0.0)
                throw(0.0);
            if(page_count<0)
                throw(0);
        }
        catch(int x)
        {
            cout<<"Exception : PAGE COUNT cannot be negative !"<<endl 
                <<"SETTING ALL VALUES TO ZERO !\n";
            SetZero();
        }
        catch(double x)
        {
            cout<<"Exception : PRICE cannot be negative !"<<endl 
                <<"SETTING ALL VALUES TO ZERO !\n";
            SetZero();
        }
    }

    void OutData()
    {
        cout<<"-------------------------------------------------"<<endl;
        Publication::OutData();
        cout<<"Page Count : "<<page_count<<endl;
    }
};

class Tape : public Publication
{
    float playing_time;
    public:
    void SetZero()
    {
        playing_time=0.0;
        Publication::SetZero();
    }

    void InData()
    {
        Publication::InData();
        cout<<"Enter Tape Playing Time (in Minutes) : ";cin>>playing_time;
        try
        {
            if(price<0.0)
                throw(0.0);
            if(playing_time<0.0)
                throw(0);
        }
        catch(int x)
        {
            cout<<"Exception : PLAYING TIME cannot be negative !"<<endl 
                <<"SETTING ALL VALUES TO ZERO !\n";
            SetZero();
        }
        catch(double x)
        {
            cout<<"Exception : PRICE cannot be negative !"<<endl 
                <<"SETTING ALL VALUES TO ZERO !\n";
            SetZero();
        }
    }

    void OutData()
    {
        cout<<"-------------------------------------------------"<<endl;
        Publication::OutData();
        cout<<"Playing Time : "<<playing_time<<" minutes\n";
    }
};

int main()
{
    Tape t1;
    Book b1;
    cout<<"Enter Data for Tape :\n";
    t1.InData();
    t1.OutData();
    cout<<"-------------------------------------------------"<<endl
        <<"Enter Data for Book :\n";
    b1.InData();
    b1.OutData();
    return 0;
}