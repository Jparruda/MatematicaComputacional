def imprime_matriz(nome, M):
    """Imprime a matriz formatada."""
    print(f"\nMatriz {nome}:")
    for linha in M:
        print(["{:.2f}".format(valor) for valor in linha])

def fatoracao_lu(A):
    """Decompõe a matriz A em L e U sem usar NumPy."""
    n = len(A)

    # Inicializa L como identidade e U como uma cópia de A
    L = [[0.0] * n for _ in range(n)]
    U = [[A[i][j] for j in range(n)] for i in range(n)]

    for i in range(n):
        L[i][i] = 1  # Diagonal de L sempre é 1

        for j in range(i+1, n):
            if U[i][i] == 0:
                raise ValueError("Pivot nulo encontrado. Reordene as linhas para evitar divisão por zero.")

            fator = U[j][i] / U[i][i]
            L[j][i] = fator

            for k in range(i, n):
                U[j][k] -= fator * U[i][k]

    imprime_matriz("L", L)
    imprime_matriz("U", U)
    
    return L, U


def substituicao_direta(L, b):
    """Resolve L * Y = B por substituição direta."""
    n = len(b)
    Y = [0] * n

    for i in range(n):
        soma = sum(L[i][j] * Y[j] for j in range(i))
        Y[i] = (b[i] - soma) / L[i][i]

    print("\nVetor Y:", ["{:.2f}".format(valor) for valor in Y])
    return Y


def substituicao_retroativa(U, Y):
    """Resolve U * X = Y por substituição retroativa."""
    n = len(Y)
    X = [0] * n

    for i in range(n-1, -1, -1):
        soma = sum(U[i][j] * X[j] for j in range(i+1, n))
        X[i] = (Y[i] - soma) / U[i][i]

    print("\nVetor X:", ["{:.2f}".format(valor) for valor in X])
    return X


def resolve_sistema_lu(A, b):
    """Resolve o sistema A * X = B usando fatoração LU."""
    L, U = fatoracao_lu(A)
    Y = substituicao_direta(L, b)
    X = substituicao_retroativa(U, Y)
    return X


# 🔹 Exemplo de uso
A = [[2, 1, -1], 
     [-3, -1, 2], 
     [-2, 1, 2]]

b = [8, -11, -3]

resultado = resolve_sistema_lu(A, b)
