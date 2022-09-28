#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <complex.h>
#include <time.h>
#include "header.h"
 
double PI;
typedef double complex cplx;
 
cplx *fft(cplx *signal, int N) {
	if (N == 1) {
		return signal;
	}
	cplx *f1 = malloc(N/2 * sizeof(*f1));
	cplx *f2 = malloc(N/2 * sizeof(*f2));
	for (int i = 0; i < N/2; i++) {
		f1[i] = signal[2*i];
		f2[i] = signal[2*i + 1];
	}
	cplx *F1 = fft(f1, N/2);
	cplx *F2 = fft(f2, N/2);
	cplx *X = malloc(N * sizeof(*X));
	for (int i = 0; i < N/2; i++) {
		X[i] = 	F1[i] + cexp(-2 * I * M_PI * i / N) * F2[i];
		X[i + N/2] = F1[i] - cexp(-2 * I * M_PI * i / N) * F2[i];
	}
	return X;
}
 
cplx *ifft(cplx *X, int N) {
	if (N == 1) {
		return X;
	}
	cplx *F1 = malloc(N/2 * sizeof(*F1));
	cplx *F2 = malloc(N/2 * sizeof(*F2));
	for (int i = 0; i < N/2; i++) {
		F1[i] = X[2*i];
		F2[i] = X[2*i + 1];
	}
	cplx *f1 = fft(F1, N/2);
	cplx *f2 = fft(F2, N/2);
	cplx *x = malloc(N * sizeof(*x));
	for (int i = 0; i < N/2; i++) {
		x[i] = 	0.5 * (f1[i] + cexp(2 * I * M_PI * i / N) * f2[i]);
		x[i + N/2] = 0.5 * (f1[i] - cexp(2 * I * M_PI * i / N) * f2[i]);
	}
	return x;
}

void timer(double *totalsignal,int length1){
	FILE *fp = fopen("timeforfft.dat", "w");
	for(int k=5000;k< length1;k+=1000){
          int size = (int)round(length1/k);
          cplx *a = malloc(size*sizeof(cplx));
		  cplx *H = malloc(size*sizeof(cplx));
		  cplx *X = malloc(size*sizeof(cplx));
		  cplx *H1 = malloc(size*sizeof(cplx));
		  cplx *Y = malloc(size*sizeof(cplx));
          for(int z=0;z<size;z++){
            a[z]=totalsignal[z+k];
			H[z]=h(z);
          }
          clock_t t;
          t = clock();
          X=fft(a,size);
		  H1=fft(H,size);
		  for (int i = 0; i < size; i++)
			Y[i] = X[i] * H1[i];
		  ifft(Y,size);
          t = clock() - t;
          fprintf(fp, "%d %f\n", size,((double)t)/CLOCKS_PER_SEC);      
		  free(a)   ;
		  free(H)   ;
		  free(X)   ;
		  free(H1)   ;
		  free(Y)   ;

}
fclose(fp);
}


int main()
{
	PI = atan2(1, 1) * 4;
 

double *length=readData("signal_length.dat",1);

int length1=(int) *length;
double *totalsignal=readData("input_signal.dat",length1);

timer(totalsignal,length1);


//free(length);
free(totalsignal);
	return 0;
}