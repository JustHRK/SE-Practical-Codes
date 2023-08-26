#include<iostream>
#include<fstream>
using namespace std;

int main()
{
    char giveData[200];
    ofstream OutFile;
    OutFile.open("test.txt");
    cout<<"Enter Data to feed in the file (Character limit - 200) :\n";
    fgets(giveData,200,stdin);
    OutFile<<giveData;
    OutFile.close();

    char getData[200];
    ifstream InFile;
    InFile.open("test.txt");
    InFile.get(getData,200);
    
    cout<<"output Data\n";
    cout<<getData;
    InFile.close();

    return 0;
}   
