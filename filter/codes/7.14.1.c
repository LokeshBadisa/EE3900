#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include "header.h"
#include <time.h>

int main(){

FILE *fp = fopen("timeforconvolution.dat", "w");

double *length=readData("signal_length.dat",1);

int length1=(int) *length;
double *totalsignal=readData("input_signal.dat",length1);

for(int k=10000;k< length1;k+=1000){
          double size = length1/k;
          double a[(int)round(size)];
          for(int z=0;z<size;z++){
            a[z]=totalsignal[z+k];
          }
          clock_t t;
          t = clock();
          convolve(a,round(size));
          t = clock() - t;
          fprintf(fp, "%f %f\n", size,((double)t)/CLOCKS_PER_SEC);         
}

fclose(fp);
free(length);
free(totalsignal);
return 0;
}