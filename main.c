#include <stdio.h>
#include <string.h>
int main(void) {
	int t;
	scanf("%d", &t);
	while(t--){
	    float n;
	    scanf("%f", &n);
	    int n1 = n;
	    char a[1001];
	    scanf("%s", &a);
	    float q = 0;
	    for(int i = 0; i<n1; i++)
	        if(a[i]=='P')
	        q++;
	   float attendance = q/n;
	    int count = 0;
	    
	    for(int i = 2; i<n1-2 && attendance < 0.75; i++ ){
	    if(a[i]== 'A' && (a[i+2] == 'P' || a[i+1] == 'P') && (a[i-2]== 'P' || a[i-1]== 'P')  ){
	    count++;
	    q++;
	    attendance = q/n;
	    }
	    }
	    if(attendance<0.75)
	    printf("-1\n");
	    else
	    printf("%d\n", count);   
	}
	return 0;
}
