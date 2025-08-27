#include<iostream>
using namespace std;
int findMissing(int arr[],int n)
{
    int naturalSum = (n*(n+1))/2;
    int allSum = 0;
    for(int i=0;i<n;i++)
    {
        allSum +=arr[i];
    }
    return naturalSum - allSum;

}
int main()
{
   int arr[] = {1,2,5,3};
   int n = sizeof(arr)/sizeof(arr[0]);
    cout<<"missing one:"<<findMissing(arr,n+1);
    return 0;
}