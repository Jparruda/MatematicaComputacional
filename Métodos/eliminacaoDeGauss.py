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
A = [
    [128, 2.5, 0.2, 28.1, 4, 0.1, 1, 0.02, 0.5],
    [371, 10.0, 1.3, 77.9, 17, 0.9, 7, 0.15, 0.8],
    [300, 8.0, 3.1, 58.6, 16, 1.0, 648, 0.13, 0.8],
    [77, 0.6, 0.1, 18.4, 17, 3.7, 2, 0.06, 0.1],
    [15, 1.1, 0.2, 3.1, 3, 0.5, 3, 0.04, 0.2],
    [68, 2.0, 2.1, 12.3, 6, 0.6, 13, 0.09, 0.4],
    [118, 25.7, 0.9, 0, 20, 0.8, 30, 0.03, 0.2],
    [275, 29.9, 16.3, 0, 2, 2.8, 51, 0.08, 6.7],
    [262, 32.1, 13.9, 0, 18, 1.3, 62, 0.09, 3.3]
]
b = [5756, 401, 98.8, 782.8, 344, 27, 1824, 2.84, 35.8]

resultado = eliminacao_gauss(A, b)
print(resultado)