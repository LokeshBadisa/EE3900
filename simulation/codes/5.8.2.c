#include <stdio.h>
#include <math.h>
#include "header.h"
#include <stdlib.h>

int main(){
int n = 14;

double *h = readData("hnthroughdef.dat",n+2);

int nh=n+2;
double *x = readData("xn.dat",5);

int nx = 5;
double *y=(double *)malloc((nx+nh-1)*sizeof(double));
for(int i=0;i<nx+nh-1;i++){
    y[i]=0;
}


for (int k=0;k<nx+nh-1;k++){
	for(int j=0;j<nx;j++){
		if (k-j >= 0 && k-j < nh){
			y[k]+=x[j]*h[k-j];
        }
    }
}

for(int i=0;i<nx+nh-1;i++){
printf("%lf\n",y[i]);
}
createDat("ynthroughconvolution.dat",nx+nh-1,y);

free(x);
free(y);
free(h);
return 0;
}