def eliminacao_gauss (matriz, b):
    n=len(b)
    
    for i in range (0, n):
        for j in range (i+1, n):
            if matriz[i][i]==0:
                raise ValueError("Divisão por zero, mude a ordem das equações")
            m=matriz[j][i]/matriz[i][i]
            matriz[j][i]=0
            for k in range (i+1, n):
                matriz[j][k] = matriz[j][k]-m*matriz[i][k]
            b[j] = b[j]-m*b[i]
    
    
    x=[0.0]*(n)
    x[n-1]=b[n-1]/matriz[n-1][n-1]
    for i in range (n-2, -1, -1):
        s=0
        for j in range (i+1, n):
            s=s+matriz[i][j]*x[j]
        x[i]=(b[i]-s)/matriz[i][i]
    return x

A = [[2, 1, -1], [-3, -1, 2], [-2, 1, 2]]
b = [8, -11, -3]

print(eliminacao_gauss(A, b))