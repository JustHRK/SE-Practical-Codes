/*
EXPERIMENT -7

Write a program in C++ to use map associative container. The keys will be the names of states
and the values will be the populations of the states. When the program runs, the user is
prompted to type the name of a state. The program then looks in the map, using the state name
as an index and returns the population of the state.
*/

#include<iostream>
#include<map>
using namespace std;

int main()
{
    map<string ,int> population;
    population.insert(make_pair("Maharashtra",26));
    population.insert(make_pair("Rajasthan",6));
    population.insert(make_pair("Bihar",50));
    population.insert(make_pair("Uttar Pradesh",60));
    population.insert(make_pair("Karnataka",14));
    population.insert(make_pair("Arunachal Pradesh",16));
    population.insert(make_pair("Assam",26));
    population.insert(make_pair("Kerla",6));

    char st[50];
    cout<<"Enter a state: ";
    cin.getline(st,50);
    
    auto it=population.end();
    it= population.find(st); 
    if(it!=population.end())
        cout << "Population of  "<< it->first <<" = " << it->second << endl; 
    else
        cout<<"Nope\n";
    return 0;
}