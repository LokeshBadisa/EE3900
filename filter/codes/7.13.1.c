#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include "fftheader.h"

int main(){
    double x={1,2,3,4,2,1,0,0};
    fft(x,8);
    return 0;
}