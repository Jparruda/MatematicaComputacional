def eliminacao_gauss(matriz, b):
    """
    Implementa a eliminação de Gauss para resolver um sistema linear.

    Args:
        matriz: Uma lista de listas representando a matriz dos coeficientes.
        b: Uma lista representando o vetor dos termos independentes.

    Returns:
        Uma lista representando a solução do sistema.
    """

    n = len(b)

    for k in range(n):
        # Encontrar o pivô
        pivot = max(matriz[k][k:], key=abs)
        indice_pivot = matriz[k].index(pivot)

        # Trocar linhas (pivotamento parcial)
        matriz[k], matriz[indice_pivot] = matriz[indice_pivot], matriz[k]
        b[k], b[indice_pivot] = b[indice_pivot], b[k]

        # Eliminação
        for i in range(k + 1, n):
            fator = matriz[i][k] / matriz[k][k]
            for j in range(k, n):
                matriz[i][j] -= fator * matriz[k][j]
            b[i] -= fator * b[k]

    # Substituição retroativa
    x = [0] * n
    for i in range(n - 1, -1, -1):
        s = sum(matriz[i][j] * x[j] for j in range(i + 1, n))
        x[i] = (b[i] - s) / matriz[i][i]

    return x

# Exemplo de uso
A = [[2, 1, -1], [-3, -1, 2], [-2, 1, 2]]
b = [8, -11, -3]

resultado = eliminacao_gauss(A, b)
print(resultado)