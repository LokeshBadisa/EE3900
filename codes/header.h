double *readData(char *file, int size) ;
void createDat(char *file, int count,double *y);

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