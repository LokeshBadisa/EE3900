#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <complex.h>
#include "fftheader.h"











int main(){
    
    //Define Signal Sequence
    double x[8] = {1,2,3,4,4,3,2,1};

    //Calculating FFT
    fft(x,8);

    return 0;
}
