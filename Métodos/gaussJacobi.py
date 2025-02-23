def gauss_jacobi(A, b, x0=None, tol=1e-6, max_iter=100):
    """
    Resolve um sistema linear Ax = b usando o método iterativo de Gauss-Jacobi.

    Parâmetros:
        A: Matriz dos coeficientes (lista de listas).
        b: Vetor dos termos independentes (lista).
        x0: Vetor inicial (opcional, padrão é 0).
        tol: Tolerância para convergência (padrão 1e-6).
        max_iter: Número máximo de iterações (padrão 100).

    Retorna:
        x: Solução aproximada do sistema.
    """
    n = len(A)

    # Se x0 não for fornecido, inicializa como vetor zero
    if x0 is None:
        x0 = [0] * n

    x = x0[:]  # Inicializa x com os valores de x0
    x_new = x[:]  # Vetor auxiliar para armazenar novos valores

    for k in range(max_iter):
        for i in range(n):
            soma = sum(A[i][j] * x[j] for j in range(n) if j != i)  # Soma sem o termo diagonal
            x_new[i] = (b[i] - soma) / A[i][i]  # Atualiza x[i]
        
        # Critério de parada: se a variação for menor que a tolerância
        erro = max(abs(x_new[i] - x[i]) for i in range(n))
        if erro < tol:
            print(f"Convergiu em {k+1} iterações.")
            return x_new

        x[:] = x_new  # Atualiza x para a próxima iteração

    print("Número máximo de iterações atingido.")
    return x_new


# 🔹 Exemplo de uso
A = [[10, -1, 2], 
     [-1, 11, -1], 
     [2, -1, 10]]

b = [6, 25, -11]

# Chute inicial (opcional)
x0 = [0, 0, 0]

solucao = gauss_jacobi(A, b, x0)
print("\nSolução encontrada:", ["{:.6f}".format(valor) for valor in solucao])
