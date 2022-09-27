#include<iostream>
#include<string>
#include<cmath>
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

