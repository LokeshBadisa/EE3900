import numpy as np

def I(N):
    return np.identity(N)


def w(N):
    return np.exp(-1j*2*np.pi/N)


def D(N):
    list=[]
    for i in range(0,N):
        list.append(pow(w(2*N),i))
    return np.diag(list)


def e(k,N):
    e=np.zeros([N,len(k)])
    for i in range(0,len(k)):
                e[k[i]-1,i]=1
    return e


def P(N):
    evenlist=[]
    oddlist=[]
    for i in range(1,N+1):
        if(i%2==0):
            oddlist.append(int(i))
        else:
            evenlist.append(int(i))
        print(evenlist,oddlist)
    return np.concatenate((e(evenlist,int(N)),e(oddlist,int(N))),axis=1)


def F(N):
    if N==1:
        return np.ones(1)
    else:
        A1=np.concatenate((I(int(N/2)),D(int(N/2))),axis=1)
        A2=np.concatenate((I(int(N/2)),-D(int(N/2))),axis=1)
        A=np.concatenate((A1,A2))
        if N==2:
            B1=[1,0]
            B2=[0,1]
        else:
            B1=np.concatenate((F(int(N/2)),np.zeros((int(N/2),int(N/2)),dtype=int,order='C')),axis=1)
            B2=np.concatenate(((np.zeros(((int(N/2),int(N/2))),dtype=int,order='C'),(F(int(N/2))))),axis=1)
        B=np.concatenate((B1,B2))
        print(A.shape)
        print(B.shape)
        A=np.matmul(A,B)
        A=np.matmul(A,P(N))
        return A

print(F(int(4)))
