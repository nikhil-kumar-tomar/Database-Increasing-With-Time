#include<iostream>
#include<string>
#include<map>
#include<list>
#include<fstream>
#include <cmath>
#include<vector>
#include<sstream>
using namespace std;
// int main(){
//     string x;
//     cout << "Enter your line here: ";
//     getline(cin,x);
//     cout << x;
//     return 0;
// }

// int main(){
//     int intNumber=40;
//     float floatNumber=30.78;
//     double doubleNumber=45.1234;
//     bool boolean=true;
//     char charName='u';
//     cout << intNumber<<endl;
//     cout << floatNumber<<endl;
//     cout << doubleNumber<<endl;
//     cout<<boolean<<endl;
//     cout<<charName<<endl;
//     return 0;
// }

// int main(){
//     char x[2][2][2]={
//         {{'a','b'},{'a','b'}},{{'a','b'},{'l','b'}}
//     };
//     cout<<x[1][1][0];
//     return 0;
// }

// int main(){
//     map<int, string> roll_a_p;
//     roll_a_p[12]="Present";
//     roll_a_p[13]="India";
//     roll_a_p[14]="Present";
//     for (auto iter=roll_a_p.begin(); iter!=roll_a_p.end();iter++){
//         cout<<(*iter).first<<"    "<<(*iter).second<<"\n";
//     }
//     return 0;
// }

// int main(){
//     int rows=100;
//     for (int x=rows;x>0;x--){
//         cout<<"*"<<string(x,' ')<<"*"<<endl;
//             }
//     return 0;

// }

// program for calucluate for square root

// void sq_rt(double x,double y){
//     double base;
//     base=pow((x+y),0.5);
//     cout<<base;
// }

// int main(){
//     int x,y;
//     cout<<"Enter x: ";
//     cin>>x;
//     cout<<"Enter y: ";
//     cin>>y;
//     sq_rt(x,y);
//     return 0;
// }

// print max and min number among the three given numbers
// factorial of a number using functions name, factorial

// void maxim(double x, double y, double z){
//     if (x>y && x>z){
//         cout<<"Largest is "<<x<<endl;
//     }
//     else if (y>x && y>z){
//         cout<<"Largest is "<<y<<endl;
//     }
//     else if(z>x && z>y){
//         cout<<"Largest is "<<z<<endl;
//     }
// }

// void minim(double x, double y, double z){
//     if (x<y && x<z){
//         cout<<"Minimum is "<<x<<endl;
//     }
//     else if (y<x && y<z){
//         cout<<"Minimum is "<<y<<endl;
//     }
//     else if(z<x && z<y){
//         cout<<"Minimums is "<<z<<endl;
//     }
// }
// int main(){
//     int a=110,b=9234,c=80;
//     maxim(a,b,c);
//     minim(a,b,c);
//     return 0;
// }


// void factorial(int a){
//     long long unsigned int fact=1;
//     for (int i=a;i>0;i--){
//         fact*=i;
//     }
//     cout<<fact;
// }

// int main(){
//     factorial(6);
//     return 0;
// }

// int main(){
//     string deleteline;
//     string line;

//     ifstream fin;
//     fin.open("E:\\Creative Works\\Visual Works\\Learning Works\\C++ FIles\\Homework\\Data.csv");
//     ofstream temp;
//     temp.open("E:\\Creative Works\\Visual Works\\Learning Works\\C++ FIles\\Homework\\temp.csv");
//     cout << "Which line do you want to remove? ";
//     cin >> deleteline;
//     while (getline(fin,line))
//     {
//         if (line != deleteline)
//         {
//         temp << line << endl;
//         }
//     }

//     temp.close();
//     fin.close();
//     remove("example.txt");
//     rename("temp.txt","example.txt");

//     return 0;
// }
// class nick{
//     public:
//         string lelo;
//         string name(){
//             cout<<lelo;
//         }
// };
// int main(){
//     nick n1;
//     n1.lelo="Nice";
//     cout<<n1.name();
//     return 0;
// }

// int main(){
//     int a=10;
//     int *ptr=&a;
//     cout<<ptr<<endl;
//     cout<<*ptr<<endl;

//     return 0;
// }


// class rectangle{
//     public:
//         int length,breadth;
//         void setdim(int a,int b){
//             length=a;
//             breadth=b;
//         }
//         int area(){
//             return length*breadth;
//         }
// };

// int main(){

//     rectangle op;
//     op.setdim(4,5);
//     cout<<op.area();
//     return 0;
// }


// class Employee{
//     public:
//         float sal,number_hours_day;
//         void getinfo(int salary,int hours_day){
//             sal=salary;
//             number_hours_day=hours_day;
//         }
//     private:
//         void AddSal(){
//             if (sal<500){
//                 sal+=10;
//             }
//         }
//         void AddWork(){
//             if (number_hours_day>6){
//                 sal+=5;
//             }
//         }
//     public:
//         int Finalsal(){
//             AddSal();
//             AddWork();
//             return sal;
//         }

// };  

// int main(){

//     Employee p;
//     p.getinfo(10,10);
//     cout<<p.Finalsal();
//     return 0;
// }
