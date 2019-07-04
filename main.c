#include <stdio.h>
int main()
{
    int t,k;
    scanf("%d",&t);
    char c[26];
    for(k=0;k<26;k++)
        c[k] = 97+25-k; 
    while(t--){
        int n,i,j;
        scanf("%d",&n);
        char s[n];
        scanf("%s",s);
        if(n%2==0)
            for(i=0;i<n;i=i+2){
                char s1;
                    s1 = s[i+1];
                    s[i+1]=s[i];
                    s[i]=s1;
            }
        else{
            for(i=0;i<n-1;i=i+2){
                char s1;
                    s1 = s[i+1];
                    s[i+1]=s[i];
                    s[i]=s1;
            }
        }
        for(i=0;i<n;i++)
        {   
            int d = (int)s[i]-97;
            printf("%c",c[d]);
        }
        printf("\n");
    }
    return 0;
}
