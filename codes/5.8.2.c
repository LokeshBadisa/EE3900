#include <stdio.h>
#include <math.h>
#include "header.h"
#include <stdlib.h>

int main(){
int n = 14;
//n = np.arange(14)
//fn=pow(-0.5,n)
double hn1[n+2];
double hn2[n+2];

for(int i=0;i<n+2;i++){
if(i==n || i==n+1){
hn1[i]=0;
}
else{
    hn1[i]=pow(-0.5,i);
}
}

for(int i=0;i<n+2;i++){
if(i==0 || i==1){
hn2[i]=0;
}
else{
    hn2[i]=pow(-0.5,i-2);
}
}

//hn1=np.pad(fn, (0,2), 'constant', constant_values=(0))
//hn2=np.pad(fn, (2,0), 'constant', constant_values=(0))
//h = hn1+hn2
double *h = (double *)malloc((n+2)*sizeof(double));
for(int i=0;i<n+2;i++){
h[i]=hn1[i]+hn2[i];
}

int nh=n+2;
double *x = readData("xn.dat",5);
//x=np.array([1.0,2.0,3.0,4.0,2.0,1.0])
int nx = 5;
double *y=(double *)malloc((nx+nh-1)*sizeof(double));
for(int i=0;i<nx+nh-1;i++){
    y[i]=0;
}

//y = np.zeros(nx+nh-1)

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
createDat("ynconv.dat",nx+nh-1,y);
createDat("hn.dat",n+2,h);
//print(y)
free(x);
free(y);
free(h);
return 0;
}