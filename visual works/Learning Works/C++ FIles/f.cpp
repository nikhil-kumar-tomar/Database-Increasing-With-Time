#include <iostream>
#include <string>
#include <cmath>
#include <bits/stdc++.h>
# define my_sizeof(type) ((char *)(&type+1)-(char*)(&type))
using namespace std;

// int main() {
//   int d,sum;
//   double e;
//   char p;
//   string la;
//   la="HEllo WOrld";
//   p='A';
//   e=15.5;
//   d=1;
//   sum=d+p;
//   cout << "Hello World!" <<endl; //endl is for end the line as well as "\n" is same.
//   /* this is a multi
//   line command and we are using it */
//   cout<<"My world"<<endl;
//   cout<<d<<endl;
//   cout<<e<<endl;
//   cout<<p<<endl;
//   cout<<la<<endl;
//   cout<<sum<<endl;
//   return 0;
// }

// int main(){
//   double x,y;
//   cout <<"Type your number: ";
//   cin >> x;
//   cout<<"Enter another number: ";
//   cin>>y;
//   x=x+y;
//   x=x*1E9;
//   cout<<"Your number is: "<< x;
//   return 0;
// }



// int main(){
//   int a,b,c;
//   a=9;
//   b=8;
//   cout<<(a<=b && a>=b);
// }


/*&& for and, || for or, ! aplied outside like cout<<!(a<=b && a>=b);! makes true to false and vice versa
>=,<=,>,<,== boolean things
cout<<x, like why << right? its for taking big data from x and passing it to cout thats why mouth is opened towards x
string concatation works here, append is just like python works with strings as well here, x="ok", y="nice" x.append(y), x will be "oknice"

.length() or .size() used as len
calling opbjects is simple string x ="Hellow" then cout << x[0] will return 'H', Just like Python

cin >>x for assigning input to x, but spaces will be left by this method for that. use getline()
getline(cin,x) taking all the input even spaces and assigning to x

<cmath> for sqrt(), round(), log() etc and max() and min() are also available

abs(x)	Returns the absolute value of x
acos(x)	Returns the arccosine of x
asin(x)	Returns the arcsine of x
atan(x)	Returns the arctangent of x
cbrt(x)	Returns the cube root of x
ceil(x)	Returns the value of x rounded up to its nearest integer
cos(x)	Returns the cosine of x
cosh(x)	Returns the hyperbolic cosine of x
exp(x)	Returns the value of Ex
expm1(x)	Returns ex -1
fabs(x)	Returns the absolute value of a floating x
fdim(x, y)	Returns the positive difference between x and y
floor(x)	Returns the value of x rounded down to its nearest integer
hypot(x, y)	Returns sqrt(x2 +y2) without intermediate overflow or underflow
fma(x, y, z)	Returns x*y+z without losing precision
fmax(x, y)	Returns the highest value of a floating x and y
fmin(x, y)	Returns the lowest value of a floating x and y
fmod(x, y)	Returns the floating point remainder of x/y
pow(x, y)	Returns the value of x to the power of y
sin(x)	Returns the sine of x (x is in radians)
sinh(x)	Returns the hyperbolic sine of a double value
tan(x)	Returns the tangent of an angle
tanh(x)	Returns the hyperbolic tangent of a double value


Conditions.
if(conditions){
  [Code]
}
else|No parenthesis are used here|{
  code
}

While loops are simeple as well
while(conditions){
  code goes here;
  if(){
    break;
  }
  else{
    break;
  }
}

do {
  // code block to be executed once
}
while (condition);
do/while loops run code one time and then check condition and run them until condition is fulfilled


void function(parameters){
  //code for this function goes here
}

// void means function does not have to return a value for example cout<<function() won't work

*/
 //New Programs ahead :)

//  int main(){
//   string myString = "Hello";
//   myString[0]='L';
//   cout<< myString;
//  }

// int main(){
//   int x,y,mx,mn,sm,srt;
//   x=989234;
//   y=312313;
//   mx=max(x,y);
//   mn=min(x,y);
//   srt=sqrt(x);
//   cout <<mx<<endl;
//   cout <<mn<<endl;
//   cout<<srt<<endl;

//   return 0;
// } 

// int main(){
//   string x;
//   cout <<"What's Your name: ";
//   getline(cin,x);
//   if (x=="nikhil"){
//     cout <<"Welcome " << x;
//   }
//   else if(x=="ankur"){
//     cout <<"Welcome " << x;
//   }
//   else{
//     cout << "Get the Damn OUt of this program " << x;
//   }
// }

// int main(){
//   int x;
//   cout<<"Type Your number: ";
//   cin>>x;
//   int day = x;
//   switch (day){
//   case 9:
//     cout <<"Welcome";
//     break;
  
//   default:
//     cout<<"Shutup this is default";
//     break;
//   } 
// }

// int main(){
//   int i=0;
//   while (i<5){
//     cout<<i<<endl;
//     if (i>3){
//       break;
//     }
//     i++;
//   }
//   return 0;
// }

// multidimensional arrays 
// int main(){

//   string lame[2][2][2]={{{"nice","noice"},{"ag","rt"}},{{"nice","noice"},{"nice","noice"}}};
//   cout<<lame[0][1][0];
//   return 0;
// }

//for List elements and len function is also made inside it
// void list_elements(int mynumbers[]){
//   int size = mynumbers-*(&mynumbers + 1);
//   for (int i=0;i<=size;i++){
//     cout<<i<<endl;
//   }
// }
// ///////////////////////////////////////////////////////

// int main(){
//   int mals=100000;
//   int size=mals+1;
//   cout << size;
// }

// if you are puting if conditions again and again its better to use (else if) rather than mulitple if conditions to save time and resources.

