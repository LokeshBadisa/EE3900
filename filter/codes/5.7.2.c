#include <stdio.h>
#include "header.h"
#include <stdlib.h>
#include <math.h>

int main(){

int n = 14;
double *h = (double *)malloc((n+2)*sizeof(double));   


for(int i=0;i<n+2;i++){
h[i]=hnthroughdef(i);
printf("%lf",h[i]);
}


createDat("hnthroughdef.dat",n+2,h);
free(h);

    return 0;
}