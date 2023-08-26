/*
EXPERIMENT - 5

Write a function template for selection sort that inputs, sorts and outputs an integer arr and a
float arr.
*/

#include<iostream>
using namespace std;

template <typename T>
void f_sort()
{
    T arr[25];
    int n;
    cout<<"Enter the No. of Elements : "<<endl;
    cin>>n;
    for(int i=0;i<n;i++)
    {
        cout<<"Enter Element "<<i+1<<" : ";
        cin>>arr[i];
    }
    cout<<"------Unsorted Array------\n";
    for (int i=0;i<n;i++)
    {
        cout<<arr[i]<<" ";
    }
    cout<<endl;
    for(int i=0;i<n;i++)
    {
        T temp;
        for(int j=i;j<n;j++)
        {
            if(arr[i]>arr[j])
            {
                temp=arr[i];
                arr[i]=arr[j];
                arr[j]=temp;
            }
        }
    }
    cout<<"\n------Sorted Array------\n";
    for (int i=0;i<n;i++)
    {
        cout<<arr[i]<<" ";
    }
    cout<<endl;
}

int main()
{
    cout<<"----ARRAY FOR INTs----\n";
    f_sort<int>();
    cout<<"----ARRAY FOR FLOATs----\n";
    f_sort<float>();
    return 0;
}