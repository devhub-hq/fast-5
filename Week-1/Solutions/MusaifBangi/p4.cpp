#include<iostream>
#include <vector>

using namespace std;
void funnySum(int arr[],int n,int x){
  int odds = 0;
  int evens = 0;
   bool possible = false;
  for(int i=0;i<n;i++)
  {
    if(arr[i]%2 == 0) evens ++;
    else odds++;
  }
   for (int k = 1; k <= odds; k += 2) {
        if (x - k >= 0 && x - k <= evens) {
            possible = true;
            break;
        }
    }

    if (possible) cout << "YES";
    else cout << "NO";
    


}
int main()
{
    int arr[] ={1,2,3,4};
    int N = sizeof(arr)/sizeof(arr[0]);
    int X = 3;
    funnySum(arr,N,X);


    return 0;
}