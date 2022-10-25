//Libraries Used
#include<iostream>
#include<string>
#include<sstream>
#include<cmath>
#include<algorithm>
#include<list>
#include<vector>
#include<cctype>
#include<map>
#include<fstream>
using namespace std;
 
// cube root program //


// int main(){
//     while (true){
//         char choic;
//         double num,sq_rt;
//         cout <<"Please Enter your number: ";
//         cin>>num;
//         sq_rt=cbrt(num);
//         cout <<"cube root of "<<num<<" is "<<sq_rt<<endl;
//         cout << "Do you want to do more operations (Y/N): ";
//         cin >> choic;
//         choic = toupper(choic);
//         if (choic == 'N')
//         {
//             cout<<"\nOkay have a nice day :)";
//             break;
//         }
//         else {
//             continue;
//         }
//     }
//     return 0;
// }

// end cube root programs//

//odd even program//

// void odd_even(int x)
// {
//     if (x % 2 == 0)
//     {
//         cout << x << " is an even number"<<endl<<endl;
//     }
//     else
//     {
//         cout << x << " is an odd number"<<endl<<endl;
//     }
// }

// int main(){
//     while (true){
//         char choic;
//         int num;
//         cout <<"Please Enter your number: ";
//         cin>>num;
//         odd_even(num);
//         cout << "Do you want to do more operations (Y/N): ";
//         cin >> choic;
//         choic = toupper(choic);
//         if (choic == 'N')
//         {
//             cout<<"\nOkay have a nice day :)";
//             break;
//         }
//         else {
//             continue;
//         }
//     }
//     return 0;

// }

// end Odd even Program// 

// Square root Program//


// int main(){
//     while (true){
//         char choic;
//         double num,sq_rt;
//         cout <<"Please Enter your number: ";
//         cin>>num;
//         sq_rt=sqrt(num);
//         cout <<"square root of "<<num<<" is "<<sq_rt<<endl;
//         cout << "Do you want to do more operations (Y/N): ";
//         cin >> choic;
//         choic = toupper(choic);
//         if (choic == 'N')
//         {
//             cout<<"\nOkay have a nice day :)";
//             break;
//         }
//         else {
//             continue;
//         }
//     }
//     return 0;
// }

// end square root progarm //

// Swaping program //


// void swap_var(int x,int y){
//     int l,n;
//     cout <<"Current first num "<<x<<"   ";
//     cout<<"Current second num "<<y<<endl;
//     l=x;
//     n=y;
//     y=l;
//     x=n;
//     cout <<"After swap first num "<<x<<"    ";
//     cout<<"After swap second num "<<y<<endl;
// }


// int main(){
//     while (true){
//         char choic;
//         double num_1,num_2,sq_rt;
//         cout <<"Please Enter your first number: ";
//         cin>>num_1;
//         cout <<"Please Enter your second number: ";
//         cin>>num_2;
//         swap_var(num_1,num_2);
//         cout << "Do you want to do more operations (Y/N): ";
//         cin >> choic;
//         choic = toupper(choic);
//         if (choic == 'N')
//         {
//             cout<<"\nOkay have a nice day :)";
//             break;
//         }
//         else {
//             continue;
//         }
//     }
//     return 0;
// }

// end Swap Program//

//(a+b)^2 formula

// int main(){
//     double a,b,result;
//     cout <<"Program for (a+b)^2 formula"<<endl;
//     cout <<"Enter your first number: ";
//     cin>>a;
//     cout <<"Enter your second number: ";
//     cin>>b;
//     result=pow(a,2)+pow(b,2)+2*a*b;
//     cout <<result;
//     return 0;
// }

//name,address, phonenumber

// int main(){
//     string name,address;
//     long long int phone_number;
//     cout<<"Enter your name here: ";
//     getline(cin,name);
//     cout<<"Enter your address here: ";
//     getline(cin,address);
//     cout<<"Enter your phone number here: ";
//     cin>>phone_number;
//     cout<<"\n";
//     cout <<"Your name is: "<<name<<endl;
//     cout<<"Your address is: "<<address<<endl;
//     cout<<"Your phone number is: "<<phone_number<<endl;
// }

// int main(){
//     int intNumber=30;
//     float floatNumber=30.78;
//     double doubleNumber=45.1234;
//     bool boolean=true;
//     char charName='u';
//     cout<<intNumber<<endl;
//     cout<<floatNumber<<endl;
//     cout<<doubleNumber<<endl;
//     cout<<boolean<<endl;
//     cout<<charName<<endl;
//     return 0;
// }

// Assignment 2 starts here.

// Triangle program
// int main(){
//     float a,b,c,s,result;
//     cout <<"Enter your first side: ";
//     cin>>a;
//     cout <<"Enter your second side: ";
//     cin>>b;
//     cout <<"Enter your third side: ";
//     cin>>c;
//     s=(a+b+c)/2;
//     result=(sqrt(s*(s-a)*(s-b)*(s-c)));
//     cout<<"area of this triangle is: "<<result;

//     return 0;
// }

// dist between coordinates (2)
// int main(){
//     float a,b,c,d,result;
//     cout <<"Enter your first coordinate: ";
//     cin>>a;
//     cout <<"Enter your second coordinate: ";
//     cin>>b;
//     cout <<"Enter your third coordinate: ";
//     cin>>c;
//     cout <<"Enter your fourth coordinate: ";
//     cin>>d;
//     result=sqrt(pow((c-a),2)+pow((d-b),2));
//     cout<<"Distance between these points is : "<<result;
//     return 0;
// }

// (3) output of area of triangles with coordinates
// int main(){
//     float a,b,c,d,e,f,side_1,side_2,side_3,result,s;
//     cout <<"Enter your first coordinate: ";
//     cin>>a;
//     cout <<"Enter your second coordinate: ";
//     cin>>b;
//     cout <<"Enter your third coordinate: ";
//     cin>>c;
//     cout <<"Enter your fourth coordinate: ";
//     cin>>d;
//     cout <<"Enter your fifth coordinate: ";
//     cin>>e;
//     cout <<"Enter your sixth coordinate: ";
//     cin>>f;
//     side_1=sqrt(pow((c-a),2)+pow((d-b),2));
//     side_2=sqrt(pow((e-a),2)+pow((f-b),2));
//     side_3=sqrt(pow((e-c),2)+pow((f-d),2));
//     s=(side_1+side_2+side_3)/2;
//     result=(sqrt(s*(s-side_1)*(s-side_2)*(s-side_3)));
//     cout<<"area of this triangle is: "<<result;
//     return 0;
// }

//(4) slope of a normal line

// int main(){
//     float a,b,c,result;
//     cout <<"Enter your first num: ";
//     cin>>a;
//     cout <<"Enter your second num: ";
//     cin>>b;
//     cout <<"Enter your third num: ";
//     cin>>c;
//     result=-(a/b);
//     cout<<"slope of these points is : "<<result;
//     return 0;
// }

// (5) dist between line cx+dy+e=0 and point a,b

// int main(){
//     float a,b,c,d,e,result;
//     cout <<"Enter your first coordinate: ";
//     cin>>a;
//     cout <<"Enter your second coordinate: ";
//     cin>>b;
//     cout <<"Enter your third coordinate: ";
//     cin>>c;
//     cout <<"Enter your fourth coordinate: ";
//     cin>>d;
//     cout <<"Enter your fifth coordinate: ";
//     cin>>e;
//     result=fabs(c*a+d*b+e)/sqrt(pow(c,2)+pow(d,2));
//     cout<<"Distance between this line and point is "<<result;
//     return 0;

// }

// centre and radius of a circle

// int main(){
//     float a,b,c,d,e,centre,radius;
//     cout <<"Enter your first num: ";
//     cin>>a;
//     cout <<"Enter your second num: ";
//     cin>>b;
//     cout <<"Enter your third num: ";
//     cin>>c;
//     cout<<"Centre is ("<<a/2<<","<<b/2<<")"<<endl;
//     radius=sqrt(pow(a/2,2)+pow(b/2,2)-c);
//     cout <<"Radius is "<<radius;
//     return 0;
// }

// Program for intersection lines points
 
// int main(){
//     float a,b,c,p,q,r,x,y;
//     cout <<"Enter your first num: ";
//     cin>>a;
//     cout <<"Enter your second num: ";
//     cin>>b;
//     cout <<"Enter your third num: ";
//     cin>>c;
//     cout <<"Enter your fourth num: ";
//     cin>>p;
//     cout <<"Enter your fifth num: ";
//     cin>>q;
//     cout <<"Enter your sixth num: ";
//     cin>>r;
//     x=(b*r-q*c)/(a*q-p*b);
//     y=(p*c-a*r)/(a*q-p*b);
//     cout <<"Coordinates of intersection are ("<<x<<","<<y<<")"<<endl;
//     return 0;
// }

// program for angle of triangle

//(8)
// int main(){
//     double a,b,c,angle;
//     cout <<"Enter your first side: ";
//     cin>>a;
//     cout <<"Enter your second side: ";
//     cin>>b;
//     cout <<"Enter your third side: ";
//     cin>>c;
//     angle=acos((pow(b,2)+pow(c,2)-pow(a,2))/(2*b*c));
//     cout<<"Angle of this triangle in radian is "<<angle<<endl;
//     cout<<"Angle of this triangle in degree is "<<floor(angle*180/3.14)<<endl;
//     return 0;
// }

// Hardest program yet question 9

// int main(){
//     float a,b,c,d,e,f,g,h,rad,cent_x,cent_y,cent_z,cent_plane_dis,circl_rad,circl_area;
//     cout<<"Enter for plane ax+by+cz+d=0"<<endl;
//     cout <<"Enter your a: ";
//     cin>>a;
//     cout <<"Enter your b: ";
//     cin>>b;
//     cout <<"Enter your c: ";
//     cin>>c;
//     cout <<"Enter your d: ";
//     cin>>d;
//     cout<<"Enter for Sphere x^2+y^2+z^2+ex+fy+gz+h=0"<<endl;
//     cout <<"Enter your e: ";
//     cin>>e;
//     cout <<"Enter your f: ";
//     cin>>f;
//     cout <<"Enter your g: ";
//     cin>>g;
//     cout <<"Enter your h: ";
//     cin>>h;    
//     rad=sqrt(-h+pow((e/2),2)+pow((f/2),2)+pow((g/2),2));
//     cent_x=-e/2;
//     cent_y=-f/2;
//     cent_z=-g/2;
//     cent_plane_dis=fabs(a*cent_x+b*cent_y+c*cent_z+d)/sqrt(pow(a,2)+pow(b,2)+pow(c,2));
//     circl_rad=sqrt(pow(rad,2)-pow(cent_plane_dis,2));
//     circl_area=3.14*pow(circl_rad,2);
//     cout<<circl_area;
//     //centre of points is also e/2 and f/2 and g/2
//     return 0;
// }

// int main(){
//     float h,k,r,s,cent_pt,chord_len;
//     cout <<"Enter your x coordinate for circle: ";
//     cin>>h;
//     cout <<"Enter your y coordinate for circle: ";
//     cin>>k;
//     cout <<"Enter radius: ";
//     cin>>r;
//     cout <<"Enter your x for line: ";
//     cin>>s;
//     //cent_pt=sqrt(pow((s-h),2)+pow(k,2));
//     cent_pt=s-h;
//     chord_len=2*sqrt(pow(r,2)-pow(cent_pt,2));
//     cout<<chord_len;
    
//     return 0;
// }

// Assignment 3 Starts here
//question 1

//  int main(){
//     int a,b,c;
//     cout<<"Enter Your first num: ";
//     cin>>a;
//     cout<<"Enter your sec num: ";
//     cin>>b;
//     cout<<"Enter your third num: ";
//     cin>>c;
//     cout<<"Maximum number is "<<max({a,b,c});
    
//     return 0;
//  }

//question 2 
//  int main(){
//     int a,b,c,d;
//     cout<<"Enter Your first num: ";
//     cin>>a;
//     cout<<"Enter your sec num: ";
//     cin>>b;
//     cout<<"Enter your third num: ";
//     cin>>c;
//     cout<<"Enter your fourth num: ";
//     cin>>d;
//     cout<<"Maximum number is "<<max({a,b,c,d});
    
//     return 0;
//  }

//question 3
//  int main(){
//     int a,b;
//     cout<<"Enter Your first num: ";
//     cin>>a;
//     cout<<"Enter your sec num: ";
//     cin>>b;
//     cout<<"Numbers are: "<<endl<<max({a,b})<<endl<<min({a,b});
    
//     return 0;
//  }

//question 4
//  int main(){
//     int a,b,c;
//     cout<<"Enter Your first side: ";
//     cin>>a;
//     cout<<"Enter your sec side: ";
//     cin>>b;
//     cout<<"Enter your third side: ";
//     cin>>c;
//     if(pow(a,2)==pow(b,2)+pow(c,2) || pow(b,2)==pow(a,2)+pow(c,2) || pow(c,2)==pow(b,2)+pow(a,2) ){
//         cout<<"Triangle is right angled";
//     }
//     else{
//         cout<<"Triangle is not right angled";
//     }
    
//     return 0;
//  }

// question 5
//  int main(){
//     float a,b,c;
//     cout<<"Enter Your first num: ";
//     cin>>a;
//     cout<<"Enter your sec num: ";
//     cin>>b;
//     cout<<"Enter your third num: ";
//     cin>>c;
//     cout<<"Slope of line is "<<(-a/b)<<endl;
//     if (b==0){
//         cout<<"line is Vertical"<<endl;
//     }
//     else{
//         cout<<"line is not Vertical"<<endl;
//     }

//     return 0;
//  }

// question 6

//  int main(){
//     float a,b,c,x1,x2,d,real,img;
//     cout<<"Enter Your first num: ";
//     cin>>a;
//     cout<<"Enter your sec num: ";
//     cin>>b;
//     cout<<"Enter your third num: ";
//     cin>>c;
//     d=pow(b,2)-(4*a*c);
//     if (d>0){
//         x1=(-b+sqrt(d))/(2*a);
//         x2=(-b-sqrt(d))/(2*a);
//         cout<<x1<<endl<<x2;
//     }
//     else if (d==0){
//         x1=(-b+sqrt(d))/(2*a);
//         cout<<x1;
//     }
//     else if (d<0){
//         real= -b/(2*a);
//         img =sqrt(-d)/(2*a);
//         cout<<real<<endl;
//         cout<<img<<endl;
//         cout<<"-"<<img<<endl; 
//     }
//     else{
//         cout<<"No valid roots here";
//     }

//     return 0;
//  }

// question 7

//  int main(){
//     float a,b,c,x1,x2,d,real,img;
//     cout<<"Enter Your first num: ";
//     cin>>a;
//     cout<<"Enter your sec num: ";
//     cin>>b;
//     cout<<"Enter your third num: ";
//     cin>>c;
//     d=pow(b,2)-(4*a*c);
//     if (d>0){
//         x1=(-b+sqrt(d))/(2*a);
//         x2=(-b-sqrt(d))/(2*a);
//         cout<<x1<<endl<<x2;
//     }
//     else if (d==0){
//         x1=(-b+sqrt(d))/(2*a);
//         cout<<x1;
//     }
//     else if (d<0){
//         real= -b/(2*a);
//         img =sqrt(-d)/(2*a);
//         cout<<real<<"+"<<img<<"i"<<endl;
//         cout<<real<<"-"<<img<<"i"<<endl; 

//     }
//     else{
//         cout<<"No valid roots here";
//     }

//     return 0;
//  }

//question 8

//  int main(){
//     int a,b,c;
//     cout<<"Enter Your first num: ";
//     cin>>a;
//     cout<<"Enter your sec num: ";
//     cin>>b;
//     cout<<"Enter your third num: ";
//     cin>>c;
//     if (a==b){
//         cout<<"Unique number is "<<c;
//     }
//     else if (a==c){
//         cout<<"Unique number is "<<b;
//     }
//     else if(b==c){
//         cout<<"Unique number is "<<a;
//     }
//     else {
//         cout<<"No unique number here";
//     }
//     return 0;
//  }

// quewstion 9

//  int main(){
//     int a,b,c,d,x;
//     list<int> list1;
//     cout<<"Enter Your first num: ";
//     cin>>a;
//     cout<<"Enter your sec num: ";
//     cin>>b;
//     cout<<"Enter your third num: ";
//     cin>>c;
//     cout<<"Enter your fourth num: ";
//     cin>>d;
//     cout<<"Enter your Finding num: ";
//     cin>>x;
//     list1={a,b,c,d};
//     for (int i: list1){
//         if (i==x){
//             if (i==a){
//                 cout<<"x is equal to a";
//             }
//             if (i==b){
//                 cout<<"x is equal to b";
//             }            
//             if (i==c){
//                 cout<<"x is equal to c";
//             }
//         }
//     }
//     return 0;
//  }

// question 10

//  int main(){
//     int a,b,c,d,x,l;
//     l=0;
//     list<int> list1;
//     cout<<"Enter Your first num: ";
//     cin>>a;
//     cout<<"Enter your sec num: ";
//     cin>>b;
//     cout<<"Enter your third num: ";
//     cin>>c;
//     cout<<"Enter your fourth num: ";
//     cin>>d;
//     cout<<"Enter your Finding num: ";
//     cin>>x;
//     list1={a,b,c,d};
//     for (int i:list1){
//         if (i==x){
//             l++;
//         }
//     }
//     cout<<l;
//     return 0;
//  }

// question 11

//  int main(){
//     int a,b,c,l;
//     list<int> list1;
//     cout<<"Enter Your first num: ";
//     cin>>a;
//     cout<<"Enter your sec num: ";
//     cin>>b;
//     cout<<"Enter your third num: ";
//     cin>>c;
//     list1={a,b,c};
//     for (int i:list1){
//         if (a>b && a<c || b>a && c<a){
//             l=a;
//         }
//         else if (b>a && b<c || a>b && c<b){
//             l=b;
//         }
//         else if (c>b && c<a || b>c && a<c){
//             l=c;
//         }
//     }
//     cout<<"Number is: "<<l;
//     return 0;
//  }

// question 12

// int main(){
//     float p,q,r,a,b,c,dist,cent_pt,chord_len,area;
//     cout <<"Enter your x coordinate for circle: ";
//     cin>>p;
//     cout <<"Enter your y coordinate for circle: ";
//     cin>>q;
//     cout <<"Enter radius: ";
//     cin>>r;
//     cout<<"ax+by+c=0"<<endl;
//     cout <<"Enter your a for line: ";
//     cin>>a;
//     cout <<"Enter your b for line: ";
//     cin>>b;
//     cout <<"Enter your c for line: ";
//     cin>>c;
//     dist = (fabs(a * p + b * q + c))/(sqrt(pow(a,2) + pow(b,2)));
//     if (r>dist){
//         cout<<"Line and circle Intersects"<<endl;
//         chord_len=2*(sqrt(pow(r,2)-pow(dist,2)));
//         area=(chord_len*dist)/2;
//         cout<<"Area of Triangle is: "<<area;
//     }
//     else {
//         cout<<"no intersection";
//     }
//     return 0;
// }

// Simple calculator using switch
// void sum(){
//     int x, y, z;
//     cout << "Enter your first number: ";
//     cin >> x;
//     cout << "Enter your second number: ";
//     cin >> y;
//     z = x + y;
//     cout << "Your number is " << z << endl<<endl;   
// }

// void diff(){
//     int x, y, z;
//     cout << "Enter your first number: ";
//     cin >> x;
//     cout << "Enter your second number: ";
//     cin >> y;
//     z = x - y;
//     cout << "Your number is " << z << endl<<endl;
// }
// void mult(){
//     int x,y,z;
//     cout << "Enter your first number: ";
//     cin >> x;
//     cout << "Enter your second number: ";
//     cin >> y;
//     z = x * y;
//     cout << "Your number is " << z << endl<<endl;
// }
// void divi(){
//     int x,y,z;
//     cout << "Enter your first number: ";
//     cin >> x;
//     cout << "Enter your second number: ";
//     cin >> y;
//     z = x / y;
//     cout << "Your number is " << z << endl<<endl;
// }

// int main(){
//     int inp;
//     cout << "\n1.Sum\n2.Diff\n3.Multiply\n4.Division\n\n";
//     cout << "Enter your choice: ";
//     cin >> inp;
//     switch(inp){
//         case 1:
//             sum();
//             break;
//         case 2:
//             diff();
//             break;
//         case 3:
//             mult();
//             break;
//         case 4:
//             divi();
//             break;
//         default:
//             cout<<"Not a valid input"<<endl;
//     }
//     return 0;
// }
// simple caluclator end

// Sum of first 10 natural numbers
// int main(){
//     int y=0;
//     for(int x=1;x<=10;x++){
//         y+=x;
//     }
//     cout<<y;
//     return 0;
// }

//Output design
// int main(){ 
//     map<int, string> roll_a_p;
//     int inp,roll;
//     char choic;
//     while (true){
//         cout<<"**************************************************** Program For Attendance **************************************************** "<<endl;
//         cout<<"                                                 1. Add Attendance of children"<<endl;
//         cout<<"                                                 2. Remove Attendance of children"<<endl;
//         cout<<"                                                 3. Check Attendance of children"<<endl;
//         cout<<"                                                 4. Exit"<<endl;
//         cout<<"Enter your choice: ";
//         cin>>inp;
//         if (inp==1){
//             cout<<"                                                    Add Attendance of children"<<endl;
//             cout<<"Enter Roll no: ";
//             cin>>roll;
//             cout<<"Mark Present for "<<roll<<" (Y/N): ";
//             cin>>choic;
//             choic=toupper(choic);
//             if (choic=='Y'){
//                 roll_a_p[roll]="Present";
//                 cout<<roll<<" Marked Present"<<endl;
//             }
//             else{
//                 cout<<"Nothing changed"<<endl;
//             }
//         }
//         else if(inp==2){
//             cout<<"                                                    Remove Attendance of children"<<endl;
//             cout<<"Enter Roll no: ";
//             cin>>roll;
//             cout<<"Mark Absent for "<<roll<<" (Y/N): ";
//             cin>>choic;
//             choic=toupper(choic);
//             if (choic=='Y'){
//                 roll_a_p[roll]="Absent";
//                 cout<<roll<<" Marked Absent"<<endl;
//             }
//             else{
//                 cout<<"Nothing changed"<<endl;
//             }
//         }
//         else if (inp==3){
//             cout<<"                                                    Check Attendance of children"<<endl;
//             cout<<"Enter Roll no: ";
//             cin>>roll;
//             for (auto iter=roll_a_p.begin(); iter!=roll_a_p.end();iter++){
//                 if(roll==(*iter).first){
//                     cout<<(*iter).first<<" is "<<(*iter).second<<endl<<endl;
//                     break;
//                 }
//            }

//         }
//         else if (inp==4){
//             cout<<"                                                    Exit"<<endl;
//             cout<<"-----------------------------------------------Have a Nice Day-----------------------------------------------"<<endl;
//             break;
//     }
//     }
//     return 0;
// }

//sum of five numbers ones digit
// int main(){
//     int a,b,c,d,e,z;
//     z=0;
//     list<int> list1;
//     cout<<"Enter your first number: ";
//     cin>>a;
//     cout<<"Enter your second number: ";
//     cin>>b;
//     cout<<"Enter your third number: ";
//     cin>>c;
//     cout<<"Enter your fourth number: ";
//     cin>>d;
//     cout<<"Enter your fifth number: ";
//     cin>>e;

//     list1={a,b,c,d,e};
//     for (auto i: list1){
//         int ones=i%10;
//         z+=ones;
//     }
//     cout<<z;
//     return 0;
// }

// Second digit sum
// int main(){
//     int a,b,c,d,e,z;
//     z=0;
//     list<int> list1;
//     cout<<"Enter your first number: ";
//     cin>>a;
//     cout<<"Enter your second number: ";
//     cin>>b;
//     cout<<"Enter your third number: ";
//     cin>>c;
//     cout<<"Enter your fourth number: ";
//     cin>>d;
//     cout<<"Enter your fifth number: ";
//     cin>>e;

//     list1={a,b,c,d,e};
//     for (auto i: list1){
//         int no_ones_dig=i/10;
//         int ones=no_ones_dig%10;
//         z+=ones;
//     }
//     cout<<z;
//     return 0;
// }

// Sum after removing last digit
// int main(){
//     int a,b,c,d,e,z;
//     z=0;
//     list<int> list1;
//     cout<<"Enter your first number: ";
//     cin>>a;
//     cout<<"Enter your second number: ";
//     cin>>b;
//     cout<<"Enter your third number: ";
//     cin>>c;
//     cout<<"Enter your fourth number: ";
//     cin>>d;
//     cout<<"Enter your fifth number: ";
//     cin>>e;

//     list1={a,b,c,d,e};
//     for (auto i: list1){
//         int no_ones_dig=i/10;
//         z+=no_ones_dig;
//     }
//     cout<<z;
//     return 0;
// }

// sum of number after removing second last digit
// int main(){
//     int a,b,c,d,e,z;
//     z=0;
//     list<int> list1;
//     cout<<"Enter your first number: ";
//     cin>>a;
//     cout<<"Enter your second number: ";
//     cin>>b;
//     cout<<"Enter your third number: ";
//     cin>>c;
//     cout<<"Enter your fourth number: ";
//     cin>>d;
//     cout<<"Enter your fifth number: ";
//     cin>>e;
//     list1={a,b,c,d,e};
//     for (auto i: list1){
//         int temp1=i%10;
//         temp1=i%10;    
//         i=i/10;
//         int temp2=i%10;       
//         i=i-temp2+temp1;
//         z+=i;
//     }
//     cout<<z;
//     return 0;
// }

//Sum of product of last two digits 
// int main(){
//     int a,b,c,d,e,z;
//     z=0;
//     list<int> list1;
//     cout<<"Enter your first number: ";
//     cin>>a;
//     cout<<"Enter your second number: ";
//     cin>>b;
//     cout<<"Enter your third number: ";
//     cin>>c;
//     cout<<"Enter your fourth number: ";
//     cin>>d;
//     cout<<"Enter your fifth number: ";
//     cin>>e;
//     list1={a,b,c,d,e};
//     for (auto i: list1){
//         int ones=i%10;//first digit
//         int no_ones_dig=i/10;
//         int lones=no_ones_dig%10;
//         z+=ones*lones;
//     }
//     cout<<z;
//     return 0;
// }


// sum of reversing the last two digits numbers
// int main(){
//     int a,b,c,d,e,z;
//     z=0;
//     list<int> list1;
//     cout<<"Enter your first number: ";
//     cin>>a;
//     cout<<"Enter your second number: ";
//     cin>>b;
//     cout<<"Enter your third number: ";
//     cin>>c;
//     cout<<"Enter your fourth number: ";
//     cin>>d;
//     cout<<"Enter your fifth number: ";
//     cin>>e;
//     list1={a,b,c,d,e};
//     for (auto i: list1){
//         int ones=i%10;//first digit
//         int no_ones_dig=i/10;
//         int lones=no_ones_dig%10;
//         //cout<<ones<<lones<<endl;
//         string ones1=to_string(ones);
//         string lones1=to_string(lones);
//         string nice=ones1+lones1;
//         int noice=stoi(nice);
//         cout<<noice<<endl;
//         if (i>=100){
//             noice+=i-ones;
//         }
//         z+=noice;
//     }
//     cout<<z;
//     return 0;
// }


// last even number
// int main(){
//     int a,b,c,d,e,z;
//     z=0;
//     list<int> list1,list2;
//     cout<<"Enter your first number: ";
//     cin>>a;
//     cout<<"Enter your second number: ";
//     cin>>b;
//     cout<<"Enter your third number: ";
//     cin>>c;
//     cout<<"Enter your fourth number: ";
//     cin>>d;
//     cout<<"Enter your fifth number: ";
//     cin>>e;
//     list1={a,b,c,d,e};
//     list2={};
//     for (auto i: list1){
//         if(i%2==0){
//             list2.push_back(i);
//         }
//     }
//     cout<<list2.back();
//     return 0;
// }


// Sum of number * elements
// int main(){
//     int a,b,c,d,e,z,l=1;
//     z=0;
//     list<int> list1;
//     cout<<"Enter your first number: ";
//     cin>>a;
//     cout<<"Enter your second number: ";
//     cin>>b;
//     cout<<"Enter your third number: ";
//     cin>>c;
//     cout<<"Enter your fourth number: ";
//     cin>>d;
//     cout<<"Enter your fifth number: ";
//     cin>>e;
//     list1={a,b,c,d,e};
//     for (auto i: list1){
//         z+=l*i;
//         l++;
//     }    
//     cout<<z;
//     return 0;
// }

// Sum of odd numbers
// int main(){
//     int a,b,c,d,e,z;
//     z=0;
//     list<int> list1,list2;
//     cout<<"Enter your first number: ";
//     cin>>a;
//     cout<<"Enter your second number: ";
//     cin>>b;
//     cout<<"Enter your third number: ";
//     cin>>c;
//     cout<<"Enter your fourth number: ";
//     cin>>d;
//     cout<<"Enter your fifth number: ";
//     cin>>e;
//     list1={a,b,c,d,e};
//     list2={};
//     for (auto i: list1){
//         if(i%2!=0){
//             list2.push_back(i);
//         }
//     }
//     for(auto i: list2){
//         z+=i;
//     }
//     cout<<z;
//     return 0;
// }


// No of odd numbers

// int main(){
//     int a,b,c,d,e,z;
//     z=0;
//     list<int> list1,list2;
//     cout<<"Enter your first number: ";
//     cin>>a;
//     cout<<"Enter your second number: ";
//     cin>>b;
//     cout<<"Enter your third number: ";
//     cin>>c;
//     cout<<"Enter your fourth number: ";
//     cin>>d;
//     cout<<"Enter your fifth number: ";
//     cin>>e;
//     list1={a,b,c,d,e};
//     list2={};
//     for (auto i: list1){
//         if(i%2!=0){
//             list2.push_back(i);
//         }
//     }
//     for(auto i: list2){
//         z++;
//     }
//     cout<<z;
//     return 0;
// }



// Hotel Program

// int main(){
//     int choic;
//     cout<<"**************************************************** Program For Hotel Booking **************************************************** "<<endl<<endl;
//     cout<<"**************************************************** Choose Your location    ****************************************************"<<endl;
//     cout<<"                                                     1. New York "<<endl;
//     cout<<"                                                     2. Paris "<<endl;
//     cout<<"                                                     3. Mumbai "<<endl;
//     cout<<"Enter your choice: ";
//     cin>>choic;
//     if (choic==1){
//         int choice;
//         cout<<"**************************************************** Welcome to New York Booking Portal ****************************************************"<<endl<<endl;
//         cout<<"**************************************************** Choose Your Room Type ****************************************************: "<<endl;
//         cout<<"                                                     1. Deluxe"<<endl;
//         cout<<"                                                     2. Suite"<<endl;
//         cout<<"                                                     3. Penthouse"<<endl;
//         cout<<"Enter your choice: ";
//         cin>>choice;
//         if(choice==1){
//             string in_day,out_day;
//             int Num_day,peop_ent,room_ent;
//             double total_amt,gst_amt;
//             cout<<"Deluxe Room selected"<<endl;
//             cout<<"Choose your Checkin Day(DD/MM/YY): ";
//             cin>>in_day;
//             cout<<"Choose your checkout Day(DD/MM/YY): ";
//             cin>>out_day;
//             cout<<"Number of Day you are planning to stay: ";
//             cin>>Num_day;
//             cout<<"Enter No of People Entering: ";
//             cin>>peop_ent;
//             cout<<"Enter no of Rooms you will be requiring: ";
//             cin>>room_ent;
//             total_amt=Num_day*(room_ent*300)+150*peop_ent;
//             gst_amt=total_amt*18/100;
//             cout<<"Your Staying cost will be: "<<"$ "<<total_amt<<endl;
//             cout<<"Additional GST Cost of 18%:  "<<"$ "<<gst_amt<<endl;
//             cout<<"Total cost (including gst): "<<"$ "<<gst_amt+total_amt<<endl;
//         }
//         else if(choice==2){
//             string in_day,out_day;
//             int Num_day,peop_ent,room_ent;
//             double total_amt,gst_amt;
//             cout<<"Suite selected"<<endl;
//             cout<<"Choose your Checkin Day(DD/MM/YY): ";
//             cin>>in_day;
//             cout<<"Choose your checkout Day(DD/MM/YY): ";
//             cin>>out_day;
//             cout<<"Number of Day you are planning to stay: ";
//             cin>>Num_day;
//             cout<<"Enter No of People Entering: ";
//             cin>>peop_ent;
//             cout<<"Enter no of Rooms you will be requiring: ";
//             cin>>room_ent;
//             total_amt=Num_day*(room_ent*400)+250*peop_ent;
//             gst_amt=total_amt*18/100;
//             cout<<"Your Staying cost will be: "<<"$ "<<total_amt<<endl;
//             cout<<"Additional GST Cost of 18%:  "<<"$ "<<gst_amt<<endl;
//             cout<<"Total cost (including gst): "<<"$ "<<gst_amt+total_amt<<endl;
//         }
//         else if(choice==3){
//             string in_day,out_day;
//             int Num_day,peop_ent,room_ent;
//             double total_amt,gst_amt;
//             cout<<"Penthouse selected"<<endl;
//             cout<<"Choose your Checkin Day(DD/MM/YY): ";
//             cin>>in_day;
//             cout<<"Choose your checkout Day(DD/MM/YY): ";
//             cin>>out_day;
//             cout<<"Number of Day you are planning to stay: ";
//             cin>>Num_day;
//             cout<<"Enter No of People Entering: ";
//             cin>>peop_ent;
//             cout<<"Enter no of Rooms you will be requiring: ";
//             cin>>room_ent;
//             total_amt=Num_day*(room_ent*400)+250*peop_ent;
//             gst_amt=total_amt*18/100;
//             cout<<"Your Staying cost will be: "<<"$ "<<total_amt<<endl;
//             cout<<"Additional GST Cost of 18%:  "<<"$ "<<gst_amt<<endl;
//             cout<<"Total cost (including gst): "<<"$ "<<gst_amt+total_amt<<endl;
//         }
//         else{
//             cout<<"Choice not available"<<endl;
//         }

//     }
//     else if (choic==2){
//         int choice;
//         cout<<"**************************************************** Welcome to Paris Booking Portal ****************************************************"<<endl<<endl;
//         cout<<"**************************************************** Choose Your Room Type ****************************************************: "<<endl;
//         cout<<"                                                     1. Deluxe"<<endl;
//         cout<<"                                                     2. Suite"<<endl;
//         cout<<"                                                     3. Penthouse"<<endl;
//         cout<<"Enter your choice: ";
//         cin>>choice;
//         if(choice==1){
//             string in_day,out_day;
//             int Num_day,peop_ent,room_ent;
//             double total_amt,gst_amt;
//             cout<<"Deluxe Room selected"<<endl;
//             cout<<"Choose your Checkin Day(DD/MM/YY): ";
//             cin>>in_day;
//             cout<<"Choose your checkout Day(DD/MM/YY): ";
//             cin>>out_day;
//             cout<<"Number of Day you are planning to stay: ";
//             cin>>Num_day;
//             cout<<"Enter No of People Entering: ";
//             cin>>peop_ent;
//             cout<<"Enter no of Rooms you will be requiring: ";
//             cin>>room_ent;
//             total_amt=Num_day*(room_ent*350)+200*peop_ent;
//             gst_amt=total_amt*18/100;
//             cout<<"Your Staying cost will be: "<<"$ "<<total_amt<<endl;
//             cout<<"Additional GST Cost of 18%:  "<<"$ "<<gst_amt<<endl;
//             cout<<"Total cost (including gst): "<<"$ "<<gst_amt+total_amt<<endl;
//         }
//         else if(choice==2){
//             string in_day,out_day;
//             int Num_day,peop_ent,room_ent;
//             double total_amt,gst_amt;
//             cout<<"Suite selected"<<endl;
//             cout<<"Choose your Checkin Day(DD/MM/YY): ";
//             cin>>in_day;
//             cout<<"Choose your checkout Day(DD/MM/YY): ";
//             cin>>out_day;
//             cout<<"Number of Day you are planning to stay: ";
//             cin>>Num_day;
//             cout<<"Enter No of People Entering: ";
//             cin>>peop_ent;
//             cout<<"Enter no of Rooms you will be requiring: ";
//             cin>>room_ent;
//             total_amt=Num_day*(room_ent*450)+300*peop_ent;
//             gst_amt=total_amt*18/100;
//             cout<<"Your Staying cost will be: "<<"$ "<<total_amt<<endl;
//             cout<<"Additional GST Cost of 18%:  "<<"$ "<<gst_amt<<endl;
//             cout<<"Total cost (including gst): "<<"$ "<<gst_amt+total_amt<<endl;
//         }
//         else if(choice==3){
//             string in_day,out_day;
//             int Num_day,peop_ent,room_ent;
//             double total_amt,gst_amt;
//             cout<<"Penthouse selected"<<endl;
//             cout<<"Choose your Checkin Day(DD/MM/YY): ";
//             cin>>in_day;
//             cout<<"Choose your checkout Day(DD/MM/YY): ";
//             cin>>out_day;
//             cout<<"Number of Day you are planning to stay: ";
//             cin>>Num_day;
//             cout<<"Enter No of People Entering: ";
//             cin>>peop_ent;
//             cout<<"Enter no of Rooms you will be requiring: ";
//             cin>>room_ent;
//             total_amt=Num_day*(room_ent*450)+300*peop_ent;
//             gst_amt=total_amt*18/100;
//             cout<<"Your Staying cost will be: "<<"$ "<<total_amt<<endl;
//             cout<<"Additional GST Cost of 18%:  "<<"$ "<<gst_amt<<endl;
//             cout<<"Total cost (including gst): "<<"$ "<<gst_amt+total_amt<<endl;
//         }
//         else{
//             cout<<"Choice not available"<<endl;
//         }

//     }
//     else if (choic==3){
//         int choice;
//         cout<<"**************************************************** Welcome to Mumbai Booking Portal ****************************************************"<<endl<<endl;
//         cout<<"**************************************************** Choose Your Room Type ****************************************************: "<<endl;
//         cout<<"                                                     1. Deluxe"<<endl;
//         cout<<"                                                     2. Suite"<<endl;
//         cout<<"                                                     3. Penthouse"<<endl;
//         cout<<"Enter your choice: ";
//         cin>>choice;
//         if(choice==1){
//             string in_day,out_day;
//             int Num_day,peop_ent,room_ent;
//             double total_amt,gst_amt;
//             cout<<"Deluxe Room selected"<<endl;
//             cout<<"Choose your Checkin Day(DD/MM/YY): ";
//             cin>>in_day;
//             cout<<"Choose your checkout Day(DD/MM/YY): ";
//             cin>>out_day;
//             cout<<"Number of Day you are planning to stay: ";
//             cin>>Num_day;
//             cout<<"Enter No of People Entering: ";
//             cin>>peop_ent;
//             cout<<"Enter no of Rooms you will be requiring: ";
//             cin>>room_ent;
//             total_amt=Num_day*(room_ent*400)+250*peop_ent;
//             gst_amt=total_amt*18/100;
//             cout<<"Your Staying cost will be: "<<"$ "<<total_amt<<endl;
//             cout<<"Additional GST Cost of 18%:  "<<"$ "<<gst_amt<<endl;
//             cout<<"Total cost (including gst): "<<"$ "<<gst_amt+total_amt<<endl;
//         }
//         else if(choice==2){
//             string in_day,out_day;
//             int Num_day,peop_ent,room_ent;
//             double total_amt,gst_amt;
//             cout<<"Suite selected"<<endl;
//             cout<<"Choose your Checkin Day(DD/MM/YY): ";
//             cin>>in_day;
//             cout<<"Choose your checkout Day(DD/MM/YY): ";
//             cin>>out_day;
//             cout<<"Number of Day you are planning to stay: ";
//             cin>>Num_day;
//             cout<<"Enter No of People Entering: ";
//             cin>>peop_ent;
//             cout<<"Enter no of Rooms you will be requiring: ";
//             cin>>room_ent;
//             total_amt=Num_day*(room_ent*500)+350*peop_ent;
//             gst_amt=total_amt*18/100;
//             cout<<"Your Staying cost will be: "<<"$ "<<total_amt<<endl;
//             cout<<"Additional GST Cost of 18%:  "<<"$ "<<gst_amt<<endl;
//             cout<<"Total cost (including gst): "<<"$ "<<gst_amt+total_amt<<endl;
//         }
//         else if(choice==3){
//             string in_day,out_day;
//             int Num_day,peop_ent,room_ent;
//             double total_amt,gst_amt;
//             cout<<"Penthouse selected"<<endl;
//             cout<<"Choose your Checkin Day(DD/MM/YY): ";
//             cin>>in_day;
//             cout<<"Choose your checkout Day(DD/MM/YY): ";
//             cin>>out_day;
//             cout<<"Number of Day you are planning to stay: ";
//             cin>>Num_day;
//             cout<<"Enter No of People Entering: ";
//             cin>>peop_ent;
//             cout<<"Enter no of Rooms you will be requiring: ";
//             cin>>room_ent;
//             total_amt=Num_day*(room_ent*600)+450*peop_ent;
//             gst_amt=total_amt*18/100;
//             cout<<"Your Staying cost will be: "<<"$ "<<total_amt<<endl;
//             cout<<"Additional GST Cost of 18%:  "<<"$ "<<gst_amt<<endl;
//             cout<<"Total cost (including gst): "<<"$ "<<gst_amt+total_amt<<endl;
//         }
//         else{
//             cout<<"Choice not available"<<endl;
//         }
//     }
//     else{
//         cout<<"Choice not available"<<endl;
//     }

//     return 0;
// }

// Assignment 5 Starts here

//SOlid rectangel
// int main(){
//     int rows,columns;
//     cout<<"Enter the number: ";
//     cin>>rows;
//     cout<<"Enter number of columns: ";
//     cin>>columns;
//     for (int i=1;i<=rows;i++){
//     for (int x=1;x<=columns;x++){
//         cout<<"*";
//         }
//     cout<<endl;
//     }
//     return 0;
// }

// Rigth angle pyramid
// int main(){
//     int rows,columns;
//     cout<<"Enter the number: ";
//     cin>>rows;
//     for (int i=1;i<=rows;i++){
//         for (int x=1;x<=i;x++){
//                 cout<<"*";
//         }
//     cout<<endl;
//     }
//     return 0;
// }

// Hollow Rectangle
// int main(){
//     int rows,columns;
//     cout<<"Enter the number: ";
//     cin>>rows;
//     cout<<"Enter number of columns: ";
//     cin>>columns;
//     for (int i=1;i<=rows;i++){
//         if (i==1){
//             for(int x=1;x<=columns;x++){
//                 cout<<"*";
//             }
//         }
//         else if (i==rows){
//             for(int x=1;x<=columns;x++){
//                 cout<<"*";
//             }
//         }
//         else{
//             for(int x=1;x<=1;x++){
//                 for(int x=1;x<=1;x++){
//                     cout<<"*";
//                     for(int l=0;l<=columns-3;l++){
//                         cout<<" ";
//                     }
//                     cout<<"*";
//                 }
//             }
//         }
//     cout<<endl;
//     }
//     return 0;
// }

// Inverted Rigth angle pyramid
// int main(){
//     int rows,columns;
//     cout<<"Enter the number: ";
//     cin>>rows;
//     for (int i=rows;i>=0;i--){
//         for (int x=1;x<=i;x++){
//                 cout<<"*";
//         }
//     cout<<endl;
//     }
//     return 0;
// }


// Hollow right angle ivnerted
// int main(){
//     int rows;
//     cout<<"Enter the number: ";
//     cin>>rows;
//     for (int x=0;x<=rows+2;x++){
//             cout<<"*";
//     }
//     cout<<endl;
//     for (int x=rows;x>0;x--){
//         cout<<"*"<<string(x,' ')<<"*"<<endl;
//     }
//     cout<<"*";
//     return 0;
// }



//centeresd pyramid
// int main(){
//     int rows,k;
//     cout<<"Enter the number: ";
//     cin>>rows;
//     k=2*rows-2;
//     for (int x=0;x<rows;x++){
//         for (int j=0;j<k;j++){
//             cout<<" ";
//         }
//         --k;
//         for (int j = 0; j <= x; j++) {
//             cout << "* ";
//         }
//     cout<<endl;
//     }
//     return 0;
// } 


// Inverted pyramids
// int main(){
//     int rows,k;
//     cout<<"Enter the number: ";
//     cin>>rows;
//     k=2*rows-2;
//     for (int x=rows;x>=0;x--){
//         for (int j=k;j>0;j--){
//             cout<<" ";
//         }
//         ++k;
//         for (int j = 0; j <= x; j++) {
//             cout << "* ";
//         }
//     cout<<endl;
//     }
//     return 0;
// }



// Hollow pyramid
// int main(){
//     int rows,k,l=2;
//     cout<<"Enter the number: ";
//     cin>>rows;
//     k=2*rows-2;
//     for (int x=0;x<rows;x++){
//         for (int j=0;j<k;j++){
//             cout<<" ";
//         }
//         --k;
//         if (x<2){
//         for (int j = 0; j <= x; j++) {
//             cout << "* ";
//         }
//         }
//         else{
//             for (int j = 0; j <1; j++) {
//             cout <<"* "<<string(l,' ')<<"*";
//             l=l+2;
//         }
//         }
//     cout<<endl;
//     if(x==rows-1){
//         cout <<string(k,' ');
//         for (int j = 0; j <= x+1; j++) {
//             cout <<"* ";
//         }   
//         }
//     }
//     return 0;
// } 


// number right angle pyramid
// int main(){
//     int rows,columns;
//     cout<<"Enter the number: ";
//     cin>>rows;
//     for (int i=1;i<=rows;i++){
//         for (int x=1;x<=i;x++){
//                 cout<<x<<" ";
//         }
//     cout<<endl;
//     }
//     return 0;
// }
 
// inverted number pyramid
// int main(){
//     int rows,columns;
//     cout<<"Enter the number: ";
//     cin>>rows;
//     for (int i=rows;i>=0;i--){
//         for (int x=1;x<=i;x++){
//                 cout<<x<<" ";
//         }
//     cout<<endl;
//     }
//     return 0;
// }

// Hollow number half pyramid
// int main(){
//     int rows,z;
//     cout<<"Enter numbers: ";
//     cin>>rows;
//     int l=1;
//     z=1;
//     for (int x=0;x<rows-1;x++){
//         if (x==0){
//             cout<<l<<endl;
//         }
//         else{
//         cout<<l<<string(z,' ')<<x+1<<endl;
//         z=z+2;
//         }
//     }
//     for (int x=0;x<rows;x++){
//         if(x==0){
//             cout<<l<<" ";
//         }
//         else{
//         cout<<x+1<<" ";
//         }
//     }

//     return 0;
// }

// full number pyramid

// int main(){
//     int rows,k,l;
//     cout<<"Enter the number : ";
//     cin>>rows;
//     rows=rows*2;
//     k=2*rows-2;
//     k=k/2;
//     int n=1;
//     for (int x=0;x<rows;x++){
//     if(x%2==0){
//         for (int j=0;j<k;j++){
//             cout<<" ";
//         }
//         k=k-2;
//         for (int j = 1; j <= x+1; j++) {
//             if(j<n){
//                 if(j==1){
//                         cout<<n<<" ";
//                     }
//                 else{
//                     cout<<n+j-1<<" ";
//                 }
//             }
//             else if(j==n){
//                 l=n+j-1;
//                 cout<<l<<" ";
//             }
//             else if(j>n){
//                 --l;
//                 cout<<l<<" ";

//             }
            
//         }
//     cout<<endl;
//     n++;
//     }
//     else{
//         continue;
//     }
//     }
//     return 0;
// }


// Hollow full number pyramid

// int main(){
//     int rows,k,l=2,n=2;
//     cout<<"Enter the number: ";
//     cin>>rows;
//     k=2*rows-2;
//     for (int x=0;x<rows-1;x++){
//         for (int j=0;j<k;j++){
//             cout<<" ";
//         }
//         --k;
//         if (x<2){
//         for (int j = 1; j <= x+1; j++) {
//             cout << j<<" ";
//         }
//         }
//         else{
//             for (int j = 0; j <1; j++) {
//             ++n;
//             cout <<1<<" "<<string(l,' ')<<n;
//             l=l+2;
//         }
//         }
//     cout<<endl;
//     if(x==rows-2){
//         cout <<string(k,' ');
//         for (int j = 1; j <= x+2; j++) {
//             cout <<j<<" ";
//         }   
//         }
//     }
//     return 0;
// } 

// Number pyramid stars

// int main(){
//     int rows,l=2,y;
//     cout<<"Enter the number: ";
//     cin>>rows;
//     y=rows;
//     for (int x=1;x<=rows;x++){
//             cout<<x<<" ";
//     }
//     cout<<endl;
//     for (int x=rows;x>2;x--){
//         cout<<l<<string(y,' ')<<rows<<endl;
//         ++l;
//         y=y-2;
//     }
//     cout<<rows;
//     return 0;
// }


// full Diamond

// int main(){
//     int rows,k,space;
//     cout<<"Enter the number: ";
//     cin>>rows;
//     k=2*rows-2;
//     space=rows-1;
//         for (int x=0;x<rows;x++){
//         cout<<string(space,' ');
//         for (int j=0;j<k;j++){
//             cout<<" ";
//         }
//         --k;
//         for (int j = 0; j <= x; j++) {
//             cout << "* ";
//         }
//     cout<<endl;
//     }
//     k=2*rows-2;
//     for (int x=rows;x>=0;x--){
//         for (int j=k;j>0;j--){
//             cout<<" ";
//         }
//         ++k;
//         for (int j = 0; j < x; j++) {
//             cout << "* ";
//         }
//     cout<<endl;
//     }
//     return 0;
// }


// Hollow diamnond

// int main(){
//     int rows,k,l=2,space;
//     cout<<"Enter the number: ";
//     cin>>rows;
//     k=2*rows-2;
//     space=rows-1;
//     for (int x=0;x<rows;x++){
//         cout<<string(space,' ');
//         for (int j=0;j<k;j++){
//             cout<<" ";
//         }
//         --k;
//         if (x<2){
//         for (int j = 0; j <= x; j++) {
//             cout << "* ";
//         }
//         }
//         else{
//             for (int j = 0; j <1; j++) {
//             cout <<"* "<<string(l,' ')<<"*";
//             l=l+2;
//         }
//         }
//     cout<<endl;
//     }
//     // The upside down
//     k=2*rows-2;
//     l=rows+2;
//     for (int x=rows;x>0;x--){
//         for (int j=k;j>0;j--){
//         cout<<" ";
//         }
//         ++k;
//         if(l>0){
//         for (int j = 0; j <1; j++) {
//         cout <<"*"<<string(l,' ')<<"*";
//         }
//         }
//         else{
//             cout<<"*";
//         }
//     cout<<endl;
//     l=l-2;
//     }
//     return 0;
// } 


// Half diamond 

// int main(){
//     int rows,columns;
//     cout<<"Enter the number: ";
//     cin>>rows;
//     for (int i=1;i<=rows;i++){
//         for (int x=1;x<=i;x++){
//                 cout<<"*";
//         }
//     cout<<endl;
//     }
//     for (int i=rows;i>=0;i--){
//     for (int x=1;x<=i;x++){
//             cout<<"*";
//     }
//     cout<<endl;
//     }

//     return 0;
// }



// Tax calculator application
// double taxcalculator(double income, double savings){
//     double total,tax=0;
//     total=savings+income;
//     if (savings>=100000){
//         total=total-100000;
//     }
//     else {
//         total=total-savings;
//     }
//     //slab 0
//     if (total<=100000){
//         tax+=0;
//     }
//     //slab 1
//     else if (total>100000 && total<=200000){
//         tax+=0+(total-100000)*0.1;
//     }
//     //slab 2
//     else if (total>200000 && total<=500000){
//         tax+=0+10000+(total-200000)*0.2;
//     }
//     //slab 3
//     else if (total>500000){
//         tax+=0+10000+60000+(total-500000)*0.3;
//     }
//     return tax;
// }
// int main(){
//     double income,savings;
//     cout<<"Enter your total income: ";
//     cin>>income;
//     cout<<"Enter your savings: ";
//     cin>>savings;
//     if (savings>=0 && income>=0){
//     cout<<"Your Net Tax is "<<taxcalculator(income,savings);
//     }
//     else{
//         cout<<"Value entered are not workable";
//     }
//     return 0;
//     }



// Student management system

void add_data(){
    int roll_no;
    string name,regis_no;
    // file pointer
    fstream fout;
    // opens an existing csv file or creates a new file.
    fout.open("Data.csv", ios::app);
    cout<<"Enter roll No: ";
    cin>>roll_no;
    cout<<"Enter name: ";
    cin.ignore();
    getline(cin,name);
    cout<<"Enter Registration No: ";
    cin>>regis_no;
    fout<<"\n"<<roll_no<<','<<name<<','<<regis_no;
    cout<<"Data added succesfully";
    fout.close();
}

void read_selected_data(){
    int roll_no,roll2,count=0;
    string name,regis_no;
    // file pointer
    fstream fin;
    // opens an existing csv file or creates a new file.
    fin.open("Data.csv", ios::in);
    cout<<"Enter roll No: ";
    cin>>roll_no;
    vector<string> row;
    string line, word, temp;
  
    while (!fin.eof()) {
  
        row.clear();
  
        getline(fin, line);
  
        // used for breaking words
        stringstream s(line);
        // read every column data of a row and
        // store it in a string variable, 'word'
        while (getline(s, word, ',')) {
            // add all the column data
            // of a row to a vector
            row.push_back(word);
        }
  
        // convert string to integer for comparision
        roll2=stoi(row[0]);
  
        // Compare the roll number
        if (roll2 == roll_no) {
  
            // Print the found data
            count = 1;
            cout << "Details Available Below: \n" ;
            cout << "Roll no: " << row[0] << "\n";
            cout << "Name: " << row[1] << "\n";
            cout << "Registration No: " << row[2] << "\n";
            break;
        }
    }
    if (count == 0)
        cout << "Record not found\n";
    fin.close();
}

void read_all_data(){
    int roll_no,roll2,count=0;
    string name,regis_no;
    // file pointer
    fstream fin;
    // opens an existing csv file or creates a new file.
    fin.open("Data.csv", ios::in);
    vector<string> row;
    string line, word, temp;
    cout<<"Roll no      Name        Registration No"<<endl;
    while (!fin.eof()) {
  
        row.clear();
  
        getline(fin, line);
  
        // used for breaking words
        stringstream s(line);
        // read every column data of a row and
        // store it in a string variable, 'word'
        while (getline(s, word, ',')) {
            // add all the column data
            // of a row to a vector
            row.push_back(word);
        }
        cout << row[0];
        cout << "           "<<row[1];
        cout << "           " << row[2] << "\n";
    }
    fin.close();
}


int main(){
    read_all_data();
    return 0;
}