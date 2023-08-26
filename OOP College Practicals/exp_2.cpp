/*
EXPERIMENT 2: 

Develop a program in C++ to create a database of student’s information system containing the
following information: Name, Roll number, Class, Division, Date of Birth, Blood group,
Contact address, Telephone number, Driving license no. and other. Construct the database with
suitable member functions. Make use of constructor, default constructor, copy constructor,
destructor, static member functions, friend class, this pointer, inline code and dynamic memory
allocation operators-new and delete as well as exception handling.
*/
#include <iostream>
#include<string>
using namespace std;

class data
{   
    private:
    string name;
    int roll;
    char div;   
    string dob;
    long long int ph;
    string adr;
    string bg;
    string lic;
    static int c;
    
    public:
    data()
    {
        name="0";
        roll=0;
        div='0';
        dob="0";
        ph=0;
        adr="0";
        bg="0";
        lic="0";
        c++;
    }
    
    void getdata()
    {
        cout<<"Enter Name : ";cin>>name;
        cout<<"Enter Roll : ";cin>>roll;
        cout<<"Enter Div : ";cin>>div;
        cout<<"Enter DOB : ";cin>>dob;
        cout<<"Enter Phone : ";cin>>ph;
        cout<<"Enter Address : ";cin>>adr;
        cout<<"Enter Blood Group : ";cin>>bg;
        cout<<"Enter Licesence No. : ";cin>>lic;
    }
    
    void show()
    {
        cout<<"Enter Name : "<<name<<endl<<
            "Roll : "<<roll<<endl<<
            "Div : "<<div<<endl<<
            "DOB : "<<dob<<endl<<
            "Phone : "<<ph<<endl<<
            "Address : "<<adr<<endl<<
            "Blood Group : "<<bg<<endl<<
            "License No. : "<<lic<<endl;
    }
    
    static int getcount()
    {
        return c;
    }
    data (data& obj)
    {   
        this->name=obj.name;
        this->roll=obj.roll;
        this->div=obj.div;
        this->dob=obj.dob;
        this->ph=obj.ph;
        this->adr=obj.adr;
        this->bg=obj.bg;
        this->lic=obj.lic;
        cout<<"--------------------------"<<endl;
        cout<<"Copy Constructor implemented\n";
        cout<<"--------------------------"<<endl;
    }
    
    data(string name,int roll,char div,string dob,long long int ph,string adr,string bg,string lic)
    {
        cout<<"--------------------------"<<endl;
        cout<<"Parametrized Constructor\n";
        cout<<"--------------------------"<<endl;
        this->name=name;
        this->roll=roll;
        this->div=div;
        this->dob=dob;
        this->ph=ph;
        this->adr=adr;
        this->bg=bg;
        this->lic=lic;
        c++;
    }
    
    ~data()
    {   
        cout<<"--------------------------"<<endl;
        cout<<"Destructor Called.\n";
        cout<<"--------------------------"<<endl;
    }
    
};

int data :: c=0;

int main()
{
    int num;
    data d1;
    d1.show();
    // delete d1;
    data *d2=new data("Hashal",35,'B',"29 July 2003",8485019612,"Akudi","O +ve","HX845UIW");
    d2->show();
    data *d3=new data(*d2);
    d3->show();
    delete d2;
    cout<<"Enter Size of Database: ";cin>>num;
    data dx[num];
    for( int i=0;i<num;i++)
    {
        dx[i].getdata();
    }
    for( int i=0;i< num;i++)
    {
        dx[i].show();
    }
    return 0;
}
