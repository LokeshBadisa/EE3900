#include <stdio.h>
#include <stdlib.h>

double *readData(char *file, int size) ;


// Reads data from file into array and returns the array
double *readData(char *file, int size) {
	double *data = (double *)malloc(size * sizeof(double));
	FILE *fp = fopen(file, "r");
	if (!fp) {
		printf("Couldn't open file\n");
		return NULL;
	}
	for (int i = 0; i < size; i++) {
		fscanf(fp, "%lf", &data[i]);
	}
	fclose(fp);
	return data;
}

void createDat(char *file, int count,double *y) {
	FILE *fp = fopen(file, "w");
	if (!fp) {
		printf("Couldn't open file\n");
		return;
	}
	for (int i = 0; i < count; i++) {
		fprintf(fp, "%lf\n", y[i]);
	}
	fclose(fp);
	return;
}


int main(){
double *y=(double *)malloc(20*sizeof(double));
double k=20;
double *x = readData("xn.dat",5);

y[0] = x[0];
y[1] = -0.5*y[0]+x[1];

for(int n=2;n<k-1;n++){
	if (n < 6){
		y[n] = -0.5*y[n-1]+x[n]+x[n-2];
		}
	else if( n > 5 && n < 8){
		y[n] = -0.5*y[n-1]+x[n-2];
	}
	else y[n] = -0.5*y[n-1];
}
for (int i=0;i<k-1;i++){
	printf("%lf\n",y[i]);
}

createDat("yn.dat",20,y);
free(x);
free(y);
	return 0;
}

