#include<iostream>
using namespace std;
void repeating(string s)
{
    int freq[256] = {0};

    for(int i=0;i<s.size();i++)
    {
        int index = s[i];
       if(freq[index]>0)
       {
      cout<<"this is repeated: "<<s[i];
      return;
       }
       else freq[index]++;

    }
    cout<<"Everthing is fine";
}

int main()
{
    string s;
    cin >> s;
    repeating(s);

    return 0;
}