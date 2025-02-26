import random
import math
import matplotlib.pyplot as plt

def gerar_dados(n, x_min, x_max, ruido_min, ruido_max):
    """Gera dados aleatórios seguindo a função y = e^x + ruído."""
    random.seed(42)  # Garantir reprodutibilidade
    x_values = [x_min + i * (x_max - x_min) / (n - 1) for i in range(n)]
    y_values = [math.exp(x) + random.uniform(ruido_min, ruido_max) for x in x_values]
    return x_values, y_values

def ajuste_linear(x, y):
    """Ajusta uma reta y = ax + b pelo método dos mínimos quadrados."""
    n = len(x)
    sum_x = sum(x)
    sum_y = sum(y)
    sum_x2 = sum(xi**2 for xi in x)
    sum_xy = sum(xi * yi for xi, yi in zip(x, y))

    a = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x**2)
    b = (sum_y - a * sum_x) / n
    return a, b

def ajuste_exponencial(x, y):
    """Ajusta uma função exponencial y = A * e^(Bx) usando transformação logarítmica."""
    min_y = min(y)
    
    # Evita valores negativos ou zero para o logaritmo
    if min_y <= 0:
        y = [yi - min_y + 1 for yi in y]

    log_y = [math.log(yi) for yi in y]

    # Aplicar ajuste linear em ln(y) = Bx + ln(A)
    B, ln_A = ajuste_linear(x, log_y)
    A = math.exp(ln_A)
    return A, B

def plotar_grafico(x, y, a, b, A, B):
    """Plota os pontos originais e os ajustes linear e exponencial."""
    y_linear = [a * xi + b for xi in x]
    y_exponential = [A * math.exp(B * xi) for xi in x]

    plt.scatter(x, y, label="Dados Originais", color="blue")
    plt.plot(x, y_linear, label="Ajuste Linear", color="red")
    plt.plot(x, y_exponential, label="Ajuste Exponencial", color="green")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.show()

# Testes
if __name__ == "__main__":
    # Gerar dados de teste
    x_vals, y_vals = gerar_dados(n=21, x_min=0, x_max=20, ruido_min=-5, ruido_max=5)
    
    # Aplicar ajustes
    a_linear, b_linear = ajuste_linear(x_vals, y_vals)
    A_exp, B_exp = ajuste_exponencial(x_vals, y_vals)
    
    # Exibir resultados
    print(f"Ajuste Linear: y = {a_linear:.4f}x + {b_linear:.4f}")
    print(f"Ajuste Exponencial: y = {A_exp:.4f} * e^({B_exp:.4f}x)")

    # Gerar gráfico
    plotar_grafico(x_vals, y_vals, a_linear, b_linear, A_exp, B_exp)
