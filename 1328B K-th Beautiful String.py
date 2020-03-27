"""
1328B - K-string Beatiful String
"""
def lexi(n,k):
    answer = ""
    max=int(n*(n-1)/2)
    b1=n-2
    b2=n-1
    found=False
    K=1
    m = 0
    if k!=1:
        while found==False:
            for i in range(m):
                b2-=1
                K+=1
                if K==k:
                    found=True
                    break
                if b2==b1+1:
                    b2=n-1
            if found==True:
                break
            m+=1
            b1-=1
            K+=1
            if K==k:
                found=True
    for _ in range(n):
        answer+="a"
    print(answer[:b1]+answer[b1].replace('a','b')+answer[b1+1:b2]+answer[b2].replace('a','b')+answer[b2+1:])


t=int(input())
inp=[list(map(int,input().split())) for _ in range(t)]
count=1
for N,K in inp:
    #print(f'_{count}_')
    lexi(N,K)
    count+=1

"""
#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    cin>>t;
    long long a[100000],i,n,k,s;

    for(i=0;i<100000;i++)
    {
        a[i]=((i+1)*(i+2))/2;
       // cout<<a[i]<<" ";
    }
   while(t--)
   {
      int d,e;
       cin>>n>>k;
       for(i=0;i<100000;i++)
       {
           if(a[i]>=k)
           {
               s=a[i]-k;
               break;
           }
       }
       d=n-(i+2);
       e=n-(i+1)+s;
       for(i=0;i<n;i++)
       {
           if(i==d or i==e)
           cout<<"b";
           else
           cout<<"a";
       }
       cout<<"\n";

   }


}

"""