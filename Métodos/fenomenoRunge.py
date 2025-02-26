import matplotlib.pyplot as plt

def funcao_runge(x):
    """
    Função de Runge: f(x) = 1 / (1 + 25x^2)
    """
    return 1 / (1 + 25 * x ** 2)

def interpolacao_lagrange(x_vals, y_vals, x_interp):
    """
    Interpola os pontos (x_vals, y_vals) usando o polinômio de Lagrange.
    Retorna os valores interpolados para x_interp.
    """
    def lagrange(x, x_vals, y_vals):
        n = len(x_vals)
        soma = 0
        for i in range(n):
            termo = y_vals[i]
            for j in range(n):
                if i != j:
                    termo *= (x - x_vals[j]) / (x_vals[i] - x_vals[j])
            soma += termo
        return soma

    return [lagrange(x, x_vals, y_vals) for x in x_interp]

def visualizar_runge(n_pontos=10):
    """
    Plota a função de Runge e sua interpolação polinomial de grau (n_pontos - 1).
    """
    import numpy as np

    # Gera pontos igualmente espaçados
    x_pontos = np.linspace(-1, 1, n_pontos)
    y_pontos = [funcao_runge(x) for x in x_pontos]

    # Gera pontos para interpolação e função real
    x_interp = np.linspace(-1, 1, 200)
    y_interp = interpolacao_lagrange(x_pontos, y_pontos, x_interp)
    y_real = [funcao_runge(x) for x in x_interp]

    # Plotando os gráficos
    plt.figure(figsize=(8, 5))
    plt.plot(x_interp, y_real, label="Função de Runge (Real)", color="black", linestyle="dashed")
    plt.plot(x_interp, y_interp, label=f"Interpolação Polinomial (n={n_pontos})", color="red")
    plt.scatter(x_pontos, y_pontos, color="blue", label="Pontos Interpolados")

    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("Fenômeno de Runge")
    plt.legend()
    plt.grid()
    plt.show()

# Testando com diferentes números de pontos
if __name__ == "__main__":
    visualizar_runge(n_pontos=10)  # Teste com 10 pontos
