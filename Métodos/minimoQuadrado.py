import matplotlib.pyplot as plt

def least_squares_fit(x_values, y_values):
    """
    Realiza o ajuste de curva pelo método dos mínimos quadrados.

    Args:
        x_values: Lista com os valores de x.
        y_values: Lista com os valores de y.

    Returns:
        Uma tupla contendo os coeficientes a e b da reta de melhor ajuste (y = ax + b).
    """
    n = len(x_values)
    sum_x = sum(x_values)
    sum_y = sum(y_values)
    sum_xy = sum(x * y for x, y in zip(x_values, y_values))
    sum_x_squared = sum(x**2 for x in x_values)

    a = (n * sum_xy - sum_x * sum_y) / (n * sum_x_squared - sum_x**2)
    b = (sum_y - a * sum_x) / n
    return a, b

def plot_least_squares_fit(x_values, y_values):
    """
    Realiza o ajuste de curva pelo método dos mínimos quadrados e plota o gráfico.

    Args:
        x_values: Lista com os valores de x.
        y_values: Lista com os valores de y.
    """
    a, b = least_squares_fit(x_values, y_values)

    plt.figure(figsize=(8, 6))
    plt.scatter(x_values, y_values, label="Dados", color="blue")
    plt.plot(x_values, [a * x + b for x in x_values], label=f"Ajuste: y = {a:.2f}x + {b:.2f}", color="red")
    plt.title("Ajuste de Curva por Mínimos Quadrados")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True)
    plt.show()

# Exemplo de uso
x_data = [-1.0, -0.75, -0.6, -0.5, -0.3, 0, 0.2, 0.4, 0.5, 0.7, 1.0]
y_data = [2.05, 1.153, 0.45, 0.4, 0.5, 0, 0.2, 0.6, 0.512, 1.2, 2.05]

plot_least_squares_fit(x_data, y_data)