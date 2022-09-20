double complex **createComplMat(int m,int n);
void show(double complex **buf,int N);
double complex **typecastedMat(double x[],int N);
double complex **matmul(double complex **a, double complex **b, int m, int n, int p);
double complex **In(int N);
double complex **D(int N);
double complex **Dn(int N);
double complex w(int N);
double complex **P(int N);
double complex **concatenateMat(double complex **a,double complex **b,int M,int N,int n);
double complex **F(int N);
void fft(double x[],int N);

#define PI  atan(1)*4

void show(double complex **buf,int N) {
     printf("show entered");
	for (int i = 0; i < N; i++)
		if (!cimag(buf[i][0]))
			printf("%g \n", creal(buf[i][0]));
		else
			printf("(%g, %g) \n", creal(buf[i][0]), cimag(buf[i][0]));
}


double complex **createComplMat(int m,int n){
    printf("create complexmat entered at %d %d",m,n);
double complex **a;
 
a = (double complex**) malloc(m * sizeof( *a));
    
    for (int i=0; i<m; i++)
         a[i] = (double complex*)malloc(n * sizeof( *a[i]));
   
    for(int i=0;i<m;i++){
        for(int j=0;j<n;j++){
            a[i][j]=(double complex)0;
        }
    }
    printf("Ending createComplMat at %d %d",m,n);
 return a;
}


double complex **matmul(double complex **a, double complex **b, int m, int n, int p)
{
    printf("Matmul entered");
int i, j, k;
double complex **c, temp =0;
c = createComplMat(m,p);

 for(i=0;i<m;i++)
 {
  for(k=0;k<p;k++)
  {
    for(j=0;j<n;j++)
    {
	temp= temp+a[i][j]*b[j][k];
    }
	c[i][k]=temp;
	temp = 0;
  }
 }
return c;

}


double complex **In(int N){
    printf("In entered");
double complex **a = createComplMat(N,N);
    for(int i=0;i<N;i++){
        for(int j=0;j<N;j++){
            if(i==j) a[i][j]=(double complex)1;
        }
    }
    return a;
}

double complex w(int N){
    return cexp(-I * 2 * PI / N) ;
}

double complex **D(int N){
    printf("D entered");
double complex **a=createComplMat(N,N);
 for(int i=0;i<N;i++){
        for(int j=0;j<N;j++){
            if(i==j) {
                a[i][j]=cpow(w(2*N),i);
                break;
            }
        }
    }
    return a;
}


double complex **Dn(int N){
    printf("Dn entered");
double complex **a=createComplMat(N,N);
 for(int i=0;i<N;i++){
        for(int j=0;j<N;j++){
            if(i==j) {
                a[i][j]=-1*cpow(w(2*N),i);
                break;
            }
        }
    }
    return a;
}


double complex **P(int N){
    printf("P entered");
double complex **a=createComplMat(N,N);

int i=0;
int j=0;
while(i<=N){
a[i][j]=(double complex)1;
i=i+2;
j=j+1;
}

i=1;
while(i<=N){
   a[i][j]=(double complex)1;
i=i+2;
j=j+1; 
}
    return a;
}

double complex **concatenateMat(double complex **a,double complex **b,int M,int N,int n){
    printf("concatenateMat entered");
    if(n==0){
        //Side
        double complex **c=createComplMat(M,2*N);
        for(int i=0;i<M;i++){
            for(int j=0;j<N;j++){
                c[i][j]=a[i][j];
            }
        }
        for(int i=0;i<M;i++){
            for(int j=N;j<2*N;j++){
                c[i][j]=b[i][j-N];
            }
        }
        return c;
    }
    else{
        //Up-Down
        double complex **c=createComplMat(2*M,N);
        for(int i=0;i<M;i++){
            for(int j=0;j<N;j++){
                c[i][j]=a[i][j];
            }
        }
        for(int i=M;i<2*M;i++){
            for(int j=0;j<N;j++){
                c[i][j]=b[i-M][j];
            }
        }
    return c;
    }
}


double complex **F(int N){
    printf("F entered");
    if(N==1){
        double complex **c=createComplMat(1,1);
        c[0][0]=1;
         return c;
    }
    else{
        double complex **A1=concatenateMat(In(N/2),D(N/2),N/2,N/2,0);
        double complex **A2=concatenateMat(In(N/2),Dn(N/2),N/2,N/2,0);
        double complex **A=concatenateMat(A1,A2,N/2,N,1);
        double complex **B1=concatenateMat(F(N/2),createComplMat(N/2,N/2),N/2,N/2,0);
        double complex **B2=concatenateMat(createComplMat(N/2,N/2),F(N/2),N/2,N/2,0);
        double complex **B=concatenateMat(B1,B2,N/2,N,1);
        double complex **F=matmul(A,B,N,N,N);
        double complex **c=matmul(F,P(N),N,N,N);
     return c;
    }
}

double complex **typecastedMat(double x[],int N){
    printf("typecastedMat entered");
    double complex **x2=createComplMat(N,1);
        for(int i=0;i<N;i++){
            x2[i][0]=(double complex)x[i];			
        }
        return x2;
}
void fft(double x[],int N){
    printf("fft entered");
        double complex **c=matmul(F(N),typecastedMat(x,N),N,N,1);
        show(c,N);
}