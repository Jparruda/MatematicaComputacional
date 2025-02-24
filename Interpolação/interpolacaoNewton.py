import matplotlib.pyplot as plt

def diferencas_divididas(x_pontos, y_pontos):
    """
    Calcula os coeficientes de diferenças divididas para o polinômio de Newton.

    Parâmetros:
        x_pontos: Lista dos pontos x conhecidos.
        y_pontos: Lista dos pontos y correspondentes.

    Retorna:
        Lista dos coeficientes b_i.
    """
    n = len(x_pontos)
    tabela = [y_pontos[:] ]  # Inicializa a tabela de diferenças divididas

    for j in range(1, n):
        linha = []
        for i in range(n - j):
            diferenca = (tabela[j - 1][i + 1] - tabela[j - 1][i]) / (x_pontos[i + j] - x_pontos[i])
            linha.append(diferenca)
        tabela.append(linha)

    # Retorna a primeira coluna (coeficientes b_i)
    return [linha[0] for linha in tabela]


def interpolacao_newton(x_pontos, y_pontos, x):
    """
    Calcula o valor interpolado no ponto x usando o método de Newton.

    Parâmetros:
        x_pontos: Lista dos pontos x conhecidos.
        y_pontos: Lista dos pontos y correspondentes.
        x: Ponto onde queremos estimar P(x).

    Retorna:
        O valor interpolado P(x).
    """
    coeficientes = diferencas_divididas(x_pontos, y_pontos)
    n = len(x_pontos)
    P_x = coeficientes[0]  # Primeiro coeficiente é b_0
    termo_produto = 1  # Termo inicial do produto

    for i in range(1, n):
        termo_produto *= (x - x_pontos[i - 1])
        P_x += coeficientes[i] * termo_produto  # Soma os termos de Newton

    return P_x


def visualizar_interpolacao_newton(x_pontos, y_pontos):
    """
    Gera um gráfico comparando os pontos conhecidos com o polinômio interpolador.

    Parâmetros:
        x_pontos: Lista dos pontos x conhecidos.
        y_pontos: Lista dos pontos y correspondentes.
    """
    # Gera pontos intermediários para a curva
    x_vals = [min(x_pontos) + i * (max(x_pontos) - min(x_pontos)) / 100 for i in range(101)]
    y_vals = [interpolacao_newton(x_pontos, y_pontos, x) for x in x_vals]

    # Plota os pontos conhecidos
    plt.scatter(x_pontos, y_pontos, color='red', label="Pontos conhecidos", zorder=3)
    
    # Plota a curva do polinômio interpolador
    plt.plot(x_vals, y_vals, color='blue', linestyle='-', label="Polinômio interpolador")

    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Interpolação de Newton")
    plt.legend()
    plt.grid(True)
    plt.show()


# 🔹 Exemplo de uso
x_pontos = [1, 2, 3, 4]
y_pontos = [1, 4, 9, 16]  # f(x) = x^2

# Exemplo de interpolação em um ponto específico
x_interpolar = 2.5
resultado = interpolacao_newton(x_pontos, y_pontos, x_interpolar)
print(f"P({x_interpolar}) = {resultado:.6f}")

# Gera o gráfico
visualizar_interpolacao_newton(x_pontos, y_pontos)
