#include <stdio.h>
#include <math.h>
#include "header.h"
#include <stdlib.h>

int main(){
int n = 16;
double *h = (double *)malloc((n)*sizeof(double));
double hn1[n];
double hn2[n];

for(int i=0;i<n;i++){
if(i==n-2 || i==n-1){
hn1[i]=0;
}
else{
    hn1[i]=pow(-0.5,i);
}
}

for(int i=0;i<n;i++){
if(i==0 || i==1){
hn2[i]=0;
}
else{
    hn2[i]=pow(-0.5,i-2);
}
}
for(int i=0;i<n;i++){
h[i]=hn1[i]+hn2[i];
}
createDat("hnthroughun.dat",n,h);


free(h);
return 0;
}