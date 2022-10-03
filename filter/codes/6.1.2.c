#include <stdio.h>
#include <math.h>
#include<stdlib.h>
#include "header.h"


#define pi 3.14159
  
int main(){

int N=8;

double *xn = readData("xn.dat",14);


double *hn = readData("hn.dat",N);


double *Xr=(double*)malloc(N*sizeof(double));
double Xi[N];

for(int k=0;k<N;k++){
	for(int n=0;n<N;n++){
		Xr[k]+=xn[n]*cos(2*pi*n*k/N);
        Xi[k]+=xn[n]*sin(-2*pi*n*k/N);
}
printf("%lf \n",Xr[k]);
}

printf("\n");

double *Hr=(double*)malloc(N*sizeof(double));
double Hi[N];
for(int k=0;k<N;k++){
	for(int n=0;n<N;n++){
		Hr[k]+=hn[n]*cos(2*pi*n*k/N);
        Hi[k]+=hn[n]*sin(-2*pi*n*k/N);
}
printf("%lf \n",Hr[k]);
}

createDat("xkreal.dat",N,Xr);
createDat("hkreal.dat",N,Hr);
free(Xr);
free(Hr);
free(xn);
free(hn);


	
    return 0;
}