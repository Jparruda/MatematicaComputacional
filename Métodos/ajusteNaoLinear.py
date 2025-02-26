import matplotlib.pyplot as plt

def least_squares_fit_quadratic(x_values, y_values):
    """
    Realiza o ajuste de curva quadrática pelo método dos mínimos quadrados.

    Args:
        x_values: Lista com os valores de x.
        y_values: Lista com os valores de y.

    Returns:
        Uma tupla contendo os coeficientes a, b e c da parábola de melhor ajuste (y = ax^2 + bx + c).
    """
    n = len(x_values)
    sum_x = sum(x_values)
    sum_y = sum(y_values)
    sum_x2 = sum(x**2 for x in x_values)
    sum_x3 = sum(x**3 for x in x_values)
    sum_x4 = sum(x**4 for x in x_values)
    sum_xy = sum(x * y for x, y in zip(x_values, y_values))
    sum_x2y = sum(x**2 * y for x, y in zip(x_values, y_values))

    matrix_a = [[sum_x4, sum_x3, sum_x2],
                [sum_x3, sum_x2, sum_x],
                [sum_x2, sum_x, n]]
    matrix_b = [sum_x2y, sum_xy, sum_y]

    # Resolver o sistema de equações lineares (usando eliminação gaussiana)
    a, b, c = solve_linear_system(matrix_a, matrix_b)
    return a, b, c

def solve_linear_system(matrix_a, matrix_b):
    """
    Resolve um sistema de equações lineares usando eliminação gaussiana.

    Args:
        matrix_a: Matriz dos coeficientes.
        matrix_b: Vetor dos termos independentes.

    Returns:
        Uma lista com as soluções do sistema.
    """
    n = len(matrix_b)
    matrix_a_augmented = [row[:] + [matrix_b[i]] for i, row in enumerate(matrix_a)]

    # Eliminação gaussiana
    for i in range(n):
        pivot = matrix_a_augmented[i][i]
        for j in range(i, n + 1):
            matrix_a_augmented[i][j] /= pivot
        for j in range(i + 1, n):
            factor = matrix_a_augmented[j][i]
            for k in range(i, n + 1):
                matrix_a_augmented[j][k] -= factor * matrix_a_augmented[i][k]

    # Substituição retroativa
    solution = [0] * n
    for i in range(n - 1, -1, -1):
        solution[i] = matrix_a_augmented[i][n]
        for j in range(i + 1, n):
            solution[i] -= matrix_a_augmented[i][j] * solution[j]
    return solution

def plot_quadratic_fit(x_values, y_values):
    """
    Realiza o ajuste de curva quadrática e plota o gráfico.

    Args:
        x_values: Lista com os valores de x.
        y_values: Lista com os valores de y.
    """
    a, b, c = least_squares_fit_quadratic(x_values, y_values)

    plt.figure(figsize=(8, 6))
    plt.scatter(x_values, y_values, label="Dados", color="blue")
    
    x_fit = [min(x_values) + (max(x_values) - min(x_values)) * i / 99 for i in range(100)] # Cria pontos para plotar a curva ajustada
    plt.plot(x_fit, [a * x**2 + b * x + c for x in x_fit], label=f"Ajuste: y = {a:.2f}x^2 + {b:.2f}x + {c:.2f}", color="red")
    
    plt.title("Ajuste de Curva Quadrática por Mínimos Quadrados")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True)
    plt.show()

# Dados fornecidos
x_data = [-1.0, -0.75, -0.6, -0.5, -0.3, 0, 0.2, 0.4, 0.5, 0.7, 1.0]
y_data = [2.05, 1.153, 0.45, 0.4, 0.5, 0, 0.2, 0.6, 0.512, 1.2, 2.05]

# Plotar o gráfico com os dados fornecidos
plot_quadratic_fit(x_data, y_data)