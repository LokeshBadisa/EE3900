#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <complex.h>
#include "fftheader.h"
#include <time.h>










int main(){
    
    //Define Signal Sequence
    double x[8] = {1,2,3,4,4,3,2,1};
clock_t t;
   t = clock();

    //Calculating FFT
    fft(x,8);
    
t = clock() - t;

FILE *fp = fopen("ffttimemat.dat", "w");
	if (!fp) {
		printf("Couldn't open file\n");
	}
	fprintf(fp, "%f\n", ((double)t)/CLOCKS_PER_SEC);
	fclose(fp);

    return 0;
}
