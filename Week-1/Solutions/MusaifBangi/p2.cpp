#include<iostream>
using namespace std;
bool canPowerUp(int n)
{
  if(n == 1)
  return true;
  if(n % 2 == 1)
  return false;

  return canPowerUp(n/2);

}
int main()
{
    cout<<"Enter amount: ";
    int n ;
    cin>>n;
    if(n<1)
    cout<<"Boom Boom";

    else
    cout<<canPowerUp(n);
    return 0;
}