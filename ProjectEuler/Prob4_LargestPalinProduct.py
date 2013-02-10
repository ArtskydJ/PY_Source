#A palindromic number reads the same both ways.
#The largest palindrome made from the product of
#two 2-digit numbers is 9009 = 91*99.
#
#--- http://projecteuler.net/problem=4 ---
#
#Find the largest palindrome made from the product of two 3-digit numbers.

def palindrome(x):
    return True
####    a=(x%10);
####    b=((x%100)-a)/10;
####    c=((x%1000)-b-a)/100;
####    d=((x%10000)-c-b-a)/1000;
####    e=((x%100000)-d-c-b-a)/10000;
####    if (a==e && b==d)
####      cout << "That's a palindrome!" << endl;
####    else
####      cout << "That's no palindrome!" << endl;
####    //cout << "E=" << e << ", D=" << d << ", C=" << c << ", B=" << b << ", A=" << a;

x=0
for i in range(10,99):
    for j in range(10,99):
        if palindrome(i*j) :
            if (i*j)>x :
                x=(i*j)



####//Exercise 4.26 Palindrome Finder
#####include <iostream>
####//#include <iomanip>
####using namespace std;
####int a,b,c,d,e,x;
####int main()
####{
####  cout << "Type a 5 digit number.\nI will check if it is a palindrome.\n";
####  cin >> x;
####  if (9999<x<100000)
####    {
####    a=(x%10);
####    b=((x%100)-a)/10;
####    c=((x%1000)-b-a)/100;
####    d=((x%10000)-c-b-a)/1000;
####    e=((x%100000)-d-c-b-a)/10000;
####    if (a==e && b==d)
####      cout << "That's a palindrome!" << endl;
####    else
####      cout << "That's no palindrome!" << endl;
####    //cout << "E=" << e << ", D=" << d << ", C=" << c << ", B=" << b << ", A=" << a;
####    }
####  else
####    {
####    cout << "A 5 digit number you knucklehead!";
####    }
####  return a;
####}


####//Exercise 4.26 Number reverser
#####include <iostream>
####//#include <iomanip>
####using namespace std;
####int a[8];
####int b,c=0,t,x,y;
####int main()
####  {
####  cout << "Enter number: ";
####  cin >> x;
####  if (x<100000000)
####    {
####    b=0;
####    for (int n=1; n<x; n*=10)
####      {
####      a[b]=(((x%(n*10))-c)/n);
####      c+=a[b];
####      b++;
####      }
####    for  (int n=0; n<b; n++)
####      {
####      cout << a[n];
####      }
####    cout << endl;
####    }
####  else
####    {
####    cout << "Too big.";
####    y=0;
####    }
####  }
