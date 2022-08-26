#include <stdio.h>
#include <math.h>
#include<stdlib.h>
#include "header.h"


#define pi 3.14159
  
int main(){

int N=14;

double *xn = readData("xn.dat",20);


double *hn = readData("hn.dat",N);


double Xr[N];
double Xi[N];
for(int k=0;k<N;k++){
	for(int n=0;n<N;n++){
		Xr[k]+=xn[n]*cos(2*pi*n*k/N);
        Xi[k]+=xn[n]*sin(-2*pi*n*k/N);
}
printf("%lf \n",Xr[k]);
}
printf("\n");

double Hr[N];
double Hi[N];
for(int k=0;k<N;k++){
	for(int n=0;n<N;n++){
		Hr[k]+=hn[n]*cos(2*pi*n*k/N);
        Hi[k]+=hn[n]*sin(-2*pi*n*k/N);
}
printf("%lf \n",Hr[k]);
}

printf("\n");

//Y[k] through multiplication of X[k] and H[k]
double *Yr = (double *)malloc(N*sizeof(double));
double *Yi = (double *)malloc(N*sizeof(double));
for(int k=0;k<N;k++){
    Yr[k] = Xr[k]*Hr[k]-Xi[k]*Hi[k];
    Yi[k] = Xi[k]*Hr[k]+Xr[k]*Hi[k];
}
createDat("ykrealthroughmult.dat",N,Yr);
createDat("ykimagthroughmult.dat",N,Yi);
for(int k=0;k<N;k++){
    Yr[k] /= N;
}
createDat("ykthroughmultforgraph.dat",N,Yr);
free(xn);
free(hn);
free(Yr);
free(Yi);
    return 0;
}