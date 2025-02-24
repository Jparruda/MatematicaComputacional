import matplotlib.pyplot as plt

def interpolacao_lagrange(x_pontos, y_pontos, x):
    """
    Calcula o valor interpolado no ponto x usando o método de Lagrange.

    Parâmetros:
        x_pontos: Lista dos pontos x conhecidos.
        y_pontos: Lista dos pontos y correspondentes.
        x: Ponto onde queremos estimar P(x).

    Retorna:
        O valor interpolado P(x).
    """
    n = len(x_pontos)
    P_x = 0  # Inicializa o polinômio interpolado

    for i in range(n):
        L_i = 1  # Inicializa o termo base L_i(x)
        for j in range(n):
            if i != j:
                L_i *= (x - x_pontos[j]) / (x_pontos[i] - x_pontos[j])  # Calcula L_i(x)

        P_x += y_pontos[i] * L_i  # Soma os termos ponderados

    return P_x


def visualizar_interpolacao(x_pontos, y_pontos):
    """
    Gera um gráfico comparando os pontos conhecidos com o polinômio interpolador.

    Parâmetros:
        x_pontos: Lista dos pontos x conhecidos.
        y_pontos: Lista dos pontos y correspondentes.
    """
    # Gera pontos intermediários para a curva
    x_vals = [min(x_pontos) + i * (max(x_pontos) - min(x_pontos)) / 100 for i in range(101)]
    y_vals = [interpolacao_lagrange(x_pontos, y_pontos, x) for x in x_vals]

    # Plota os pontos conhecidos
    plt.scatter(x_pontos, y_pontos, color='red', label="Pontos conhecidos", zorder=3)
    
    # Plota a curva do polinômio interpolador
    plt.plot(x_vals, y_vals, color='blue', linestyle='-', label="Polinômio interpolador")

    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Interpolação de Lagrange")
    plt.legend()
    plt.grid(True)
    plt.show()


# 🔹 Exemplo de uso
x_pontos = [1, 2, 3, 4]
y_pontos = [1, 4, 9, 16]  # f(x) = x^2

# Exemplo de interpolação em um ponto específico
x_interpolar = 2.5
resultado = interpolacao_lagrange(x_pontos, y_pontos, x_interpolar)
print(f"P({x_interpolar}) = {resultado:.6f}")

# Gera o gráfico
visualizar_interpolacao(x_pontos, y_pontos)
