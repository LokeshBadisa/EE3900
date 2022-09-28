double *readData(char *file, int size) ;
void createDat(char *file, int count,double *y);
double delta(int n);
double hnthroughdef(int n);

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

//Creates a Data file
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

//Unit Step Sequence
double u(int n){
	if(n>=0){
	  return 1;
}
	else {
	 return 0;  
	}
}

//Calculating h(n) through given definition
double h(int n){
	return pow(-0.5,n) * u(n) + pow(-0.5,n-2) * u(n-2);
}

void convolve(double x[], int n) { 
	double a[n];
	for (int i = 0; i < n; i++){
		 for (int j = 0; j <= i; j++){ 
			a[i] += h(j)*x[i - j];
		 }
	}
}